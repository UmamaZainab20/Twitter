from django.forms import ModelForm
from .models import Comment

class Comment_Form(ModelForm):
    class Meta():
        model = Comment
        fields = ["user", "tweet","comment"]
        