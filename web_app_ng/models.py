from django.db import models

class Author(models.Model):
    #Author_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=100, blank=True)
    # def __str__(self):
    #     return f"{self.name} the Author"

class data_2023(models.Model): #model zarlasan
    
    title = models.CharField(max_length=255, null=True, blank=False) 
    description =  models.TextField(max_length=256, blank=True, null=True)
    picture = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=256, blank=True, null=True)

    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    cover = models.FileField(upload_to='covers/', blank=True, null=True)

    #number = models.OneToOneField(Author, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title #object-iig string ruu conver hiij baiga heseg
    

