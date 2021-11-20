from django.db import models
import datetime


class Post(models.Model):
    post_id = models.CharField(max_length=11, blank=False)
    post_url = models.CharField(max_length=100, blank=False)
    img_url = models.CharField(max_length=100, blank=False)
    keyword = models.CharField(max_length=50, blank=False, db_index=True)
    food_score = models.FloatField(default=0, db_index=True)
    scraped_date = models.DateTimeField(auto_now_add=True, db_index=True)
    posted_date = models.DateTimeField(default=datetime.datetime.now() - datetime.timedelta(days=365), db_index=True)
    post_text = models.TextField(default="", blank=True)
    insta_analysis = models.TextField(default="", blank=True)
    insta_analysis_food = models.BooleanField(default=False)
    is_ad = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post_id", "keyword"], name="unique post and keyword")
        ]
