from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from forum import models
from forum import forms
from forum.views.base_forum_view import BaseForumView
from forum.view_decorators.show_view import sub_category_login_required


class SubCategoryView(BaseForumView):

    template_name = 'forum/sub_category.html'


    @method_decorator(sub_category_login_required)
    def dispatch(self, *args, **kwargs):
        return super(SubCategoryView, self).dispatch(*args, **kwargs)

    def get(self, request, id):
        return render(request, self.template_name, self._get_context(id, None, request.user))

    def post(self, request, id):
        form = forms.ThreadForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.sub_category = get_object_or_404(models.SubCategory, id=id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': form.instance.id}))

        return render(request, self.template_name, self._get_context(id, form, request.user))

    def _get_context(self, id, form, user):
        context = super(SubCategoryView, self)._get_context()
        context['sub_category'] = get_object_or_404(models.SubCategory, id=id)

        if not form:
            form = forms.ThreadForm(user)
        context['form'] = form
        return context
