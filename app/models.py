from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)  # CharField() -> 길이 제한있음
    content = models.TextField()  # Text Filed() 는 길이 제한이없음


# Create your models here.
