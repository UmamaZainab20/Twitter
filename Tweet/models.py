from django.db import models
from Users.models import User
# Create your models here.
class Tweet(models.Model):
    name= models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    # title = models.CharField(max_length=50, null=True)
    # id = models.IntegerField( null=True)
    content = models.CharField(max_length=100, null=True)
    # author_id = models.IntegerField(max_length=10, null=True)
    # retweet_count = models.IntegerField(max_length=1000)
    # like_count = models.IntegerField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add= True)
    shared_with = models.ManyToManyField(User, related_name= "Tweets")

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
     
    