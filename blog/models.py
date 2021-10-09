from django.db import models
from django.urls import reverse 
from django.conf import settings
from django.utils import timezone
from nepali_datetime_field.models import NepaliDateField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


def get_profile_image_filepath(self, filename):
    return 'post_image/' + str(self.pk) + '/post_image.png'

def get_default_profile_image():
    return "codingwithdk/dummy_robort.png"



class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now = True)
    post_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,related_name='blog_posts')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_profile_image_filename(self):
        return str(self.post_image)[str(self.post_image).index('post_image/' + str(self.pk) + "/"):]
    
    def get_absolute_url(self): # new
        return reverse('blog_detail', args=[str(self.id)])



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'comments')
    comment = RichTextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return self.comment[ :20]

    def get_absolute_url(self):
        return reverse('home')