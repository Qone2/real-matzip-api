from django.urls import path
from posts import views

urlpatterns = [
    path('posts', views.post_list),
    path('post/<int:pk>', views.post_detail),
    path('posts/search-by/keyword', views.post_list_keyword_query),
    path('posts/search-by/keyword-and-score', views.post_list_keyword_score_query),
    path('keywords', views.keyword_list),
    path('post/search-by/post_id-and-keyword', views.post_postid_keyword_query)
]
