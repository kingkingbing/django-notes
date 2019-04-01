from django.urls import path, re_path
from . import views

# namespace
app_name = 'blog'

urlpatterns = [
#    re_path(r'^$', views.index, name='index'),
    re_path(r'^tag/$',
        views.TagListView.as_view(), name='tag_list'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$',
        views.TagDetailView.as_view(), name='tag_detail'),
    re_path(r'^member/$',
        views.MemberListView.as_view(), name='member_list'),
    re_path(r'^member/(?P<pk>[0-9]+)/$',
        views.MemberDetailView.as_view(), name='member_detail'),
    re_path(r'^post/$',
        views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$',
        views.PostDetailView.as_view(), name='post_detail'),
]
