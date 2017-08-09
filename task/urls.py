from django.conf.urls import url
from task.views import TaskDetail, TaskList, UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^tasks/$', TaskList.as_view(), name='task-list'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', TaskDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)