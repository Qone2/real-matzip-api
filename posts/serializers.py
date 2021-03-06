from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_id', 'post_url', 'img_url', 'keyword', 'food_score', 'scraped_date', 'posted_date', 'post_text',
                  'insta_analysis', 'insta_analysis_food', 'is_ad']
