from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^debts/$', views.DebtList.as_view()),
    # url(r'^debts/(?P<pk>[0-9]+)/$', views.debt_detail),
    url(r'^debts/(?P<pk>[0-9]+)/$', views.DebtDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^usersum/$', views.UserSumList.as_view()),
    url(r'^usersum/(?P<pk>[0-9]+)/$', views.UserSumDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)