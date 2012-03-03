from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'index'),
    # login
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    # profile
    url(r'^profile/$', 'profile'),
    url(r'^profile/info/$', 'profile_info_edit'),
    url(r'^profile/password/$', 'profile_password_edit'),
    url(r'^profile/edit/$', 'profile_edit'),
    # media
    url(r'^media/$', 'media'),
    url(r'^media/list/$', 'media_list'),
    url(r'^media/add/$', 'media_add'),
    url(r'^media/edit/(?P<upload_id>\d+)/$', 'media_edit'),
    url(r'^media/delete/$', 'media_delete'),
    # category
    url(r'^categories/$', 'category'),
    url(r'^categories/get_slug/$', 'category_get_slug'),
    url(r'^categories/list/$', 'category_list'),
    url(r'^categories/add/$', 'category_add'),
    url(r'^categories/edit/(?P<category_id>\d+)/$', 'category_edit'),
    url(r'^categories/delete/$', 'category_delete'),
)
