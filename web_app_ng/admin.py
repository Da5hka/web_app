from django.contrib import admin
from .models import data_2023

# Register your models here.
#admin.site.register(data_2023)

@admin.register(data_2023)
class ngadmin(admin.ModelAdmin):
    #fields = ['title', 'description', 'picture', 'published', 'cover'] # Admin model heseg deer zarim hesgiig hide hiih option oruulhin tuld uuniig ashiglana.
    list_display = ('title', 'description')
    search_fields = ['title', 'description', 'published', 'cover'] #search hiied daraah utguud match bolj baihaar