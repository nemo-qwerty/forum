from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
import views
import forms

urlpatterns = patterns(''
   , url(r'^$', views.IndexView.as_view(), name='index')
   , url(r'^account/login/$', #auth_views.login,
         views.LoginView.as_view(),
         { 'template_name' : 'forum/account/login.html', 'authentication_form': forms.AuthenticationForm},
         name='login')
   , url(r'^account/logout/$', views.logout_view, name='logout')

   , url(r'^account/registration/$',
         views.RegistrationView.as_view(template_name='forum/account/registration.html',), name='registration')

   , url(r'^(?P<id>\d+)/', views.SubCategoryView.as_view(), name='subcategory')

   # , url(r'^thread/(?P<id>\d+)/reply_to-(?P<post_id>\d+)/', views.ThreadView.as_view(), name='reply_to_post')
   # , url(r'^thread/(?P<id>\d+)/(?P<post_id>\d+)/', views.ThreadView.as_view(), name='reply_to_post')
   , url(r'^thread/(?P<id>\d+)/reply_to-(?P<reply_to>\d+)/$', views.ThreadView.as_view(), name='reply_to_post')
   , url(r'^thread/(?P<id>\d+)/', views.ThreadView.as_view(), name='thread')
)