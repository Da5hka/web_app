from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
#from django.core.validators import MaxValueValidator, MinValueValidator

# class Author(models.Model):
#     #Author_id = models.CharField(max_length=10, blank=True)
#     name = models.CharField(max_length=100, blank=True)
#     description_author = models.CharField(max_length=360, blank=True, null=True)
#     contact = models.CharField(max_length=50, blank=True, null=True)
#     profile = models.ImageField(upload_to='images_author/', height_field=None, width_field=None, max_length=256, blank=True, null=True)
#     # def __str__(self):
#     #     return f"{self.name} the Author"

class data_2023(models.Model): #model zarlasan
    
    title = models.CharField(max_length=100, unique=True, null=True, blank=False) 
    description =  models.TextField(max_length=360, blank=True, null=True)
    picture = models.ImageField(upload_to='images_data/', height_field=None, width_field=None, max_length=256, blank=True, null=True)

    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    cover = models.FileField(upload_to='covers/', blank=True, null=True)

    #number = models.OneToOneField(Author, null=True, blank=True, on_delete=models.CASCADE)
    Author_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class related_papers(models.Model):
    title_ng_papers = models.CharField(max_length=100, null=True, blank=False) 

    description_ng_papers =  models.TextField(max_length=360, blank=True, null=True)
    published_ng_papers = models.DateField(blank=True, null=True, default=None)
    is_published_ng_papers = models.BooleanField(default=False)

    attach_ng_papers = models.FileField(upload_to='covers_ng_papers/', blank=True, null=True)
    Author_id_ng_papers = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)