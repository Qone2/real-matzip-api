from django.urls import path
from posts import views

urlpatterns = [
    path('posts', views.post_list),
    path('post/<int:pk>', views.post_detail),
    path('posts/<string:keyword>', views.post_list_keyword_query),
    path('posts/<string:keyword>/<float:food_score>', views.post_list_keyword_score_query),
    path('keywords', views.keyword_list),
    path('post/<string:keyword>/<string:post_id>', views.post_postid_keyword_query)
]
