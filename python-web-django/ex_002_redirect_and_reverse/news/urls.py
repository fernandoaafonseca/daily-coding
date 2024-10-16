from django.urls import path
from . import views


urlpatterns = [
    path('<int:page_num>', views.news_page_num_view, name='topic-page-num'),
    path('<str:topic>', views.news_page_view, name='topic-page'),
]
