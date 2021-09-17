from django.urls import path
from posts import views

urlpatterns = [
    path('posts', views.post_list),
    path('post/<int:pk>', views.post_detail),
    path('posts/<str:keyword>', views.post_list_keyword_query),
    path('posts/<str:keyword>/<int:food_score>', views.post_list_keyword_score_query),
    path('keywords', views.keyword_list),
    path('post/<str:keyword>/<str:post_id>', views.post_postid_keyword_query),
    path('not-crawled-yet', views.not_crawled_yet)
]
