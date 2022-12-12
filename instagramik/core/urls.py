from django.urls import path, re_path
from .views import index, path_one, path_page_num, re_path_page_num



urlpatterns = [
    path('', index, name='index'),
    path('1/', path_one, name='path_one'),
    path('<int:page_num>/', path_page_num, name='path_page_num'),
    re_path(r'^(?P<page_num>\d+)/$', re_path_page_num, name='re_path_page_num')
]