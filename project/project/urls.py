from copy import name

from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rest_framework.authtoken import views as authtoken_views
from Pentagram.views import comments, users, photos #, like

urlpatterns = [

    url (r'^api/v1/login/$', authtoken_views.obtain_auth_token),
    url(r'^api/v1/photos/$', photos, name='photos'),
    url(r'^api/v1/users/$', users, name='users'),
    #url(r'^api/photos/(?P<id_photo>[0-9]*)/like/$', like, name="like"),
    url(r'^api/photos/(?P<id_photo>[0-9]*)/comments/$', comments, name="comments"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login', auth_views.login, {'template_name': 'login.html'}, name = "login"),
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name = "homepage"),




   # url(r'^api/(?P<slug>[-_\w]*)/$', views.post_detail, name='post_detail'),
  #  url(r'^api/blog/$', views.post_list, name='post_list'),
   # url(r'^api/like-blog/$', views.like_count_blog, name='like_count_blog'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)