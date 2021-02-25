# coding: utf-8
from django.conf.urls import url
from gramm.views import GrammarListView, GrammarDetailView


urlpatterns = [
    url(r'^$', GrammarListView.as_view(), name='list'),  # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
    url(r'^(?P<pk>\d+)/$', GrammarDetailView.as_view()),  # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

]