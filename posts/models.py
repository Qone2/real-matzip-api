from django.db import models


class Post(models.Model):
    post_id = models.CharField(max_length=11, blank=False)
    post_url = models.CharField(max_length=100, blank=False)
    img_url = models.CharField(max_length=100, blank=False)
    keyword = models.CharField(max_length=50, blank=False)
    food_score = models.FloatField(default=0)
    scraped_date = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField(default="")
    insta_analysis = models.TextField(default="")
    is_ad = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post_id", "keyword"], name="unique post and keyword")
        ]
        indexes = [
            models.Index(fields=["keyword"])
        ]
