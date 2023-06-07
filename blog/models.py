from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
    
class GroupsPosts(models.Model):
    name = models.CharField(max_length=100, null=False, default='')  
    
    def __str__(self):
        return self.name
        
    
class Post(models.Model):    
    rating = models.IntegerField(null=False, default=0, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupsPosts, on_delete=models.CASCADE)
    image = models.ImageField(null=True, default='', blank=True, upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=200)
    #text = models.TextField()
    content = HTMLField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)


    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    