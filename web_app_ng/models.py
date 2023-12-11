from django.db import models

# Create your models here.
class data_2023(models.Model): #model zarlasan
    # NG = (
    #     (2019, 'NG1'),
    #     (2020, 'NG2')
    # )
    # Model deer baih data ymar baih gedeg heseg baina
    title = models.CharField(max_length=255, null=True, blank=False) 
    #jil = models.CharField(max_length=32, blank=True, null=True, choices=NG)
    description =  models.TextField(max_length=256, blank=True, null=True)
    picture = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=256, blank=True, null=True)

    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    cover = models.FileField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title #object-iig string ruu conver hiij baiga heseg