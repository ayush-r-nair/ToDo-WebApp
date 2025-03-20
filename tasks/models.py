from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('food', 'Food'),
        ('office', 'Office'),
        ('sports', 'Sports'),
        ('entertainment','Entertainment'),
        ('other', 'Other'),
    ]
    
    title=models.CharField(max_length=75)
    desc=models.TextField()
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='other')
    date=models.DateTimeField(auto_now_add=True) #automatically will add date time stamp
    done=models.BooleanField(default=False)
    slug = models.SlugField(unique=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)# cascade one is used to delete all posts of the user 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1

            while Task.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title