from django.contrib import admin
from .models import data_2023, related_papers

# Register your models here.
#admin.site.register(data_2023)

@admin.register(data_2023)
class ngadmin(admin.ModelAdmin):
    #fields = ['title', 'description', 'picture', 'published', 'cover'] # Admin model heseg deer zarim hesgiig hide hiih option oruulhin tuld uuniig ashiglana.
    list_display = ('title', 'description' )
    search_fields = ['title', 'description', 'published', 'cover'] #search hiied daraah utguud match bolj baihaar

@admin.register(related_papers)
class ngadmin2(admin.ModelAdmin):
    list_display = ('title_ng_papers', 'description_ng_papers')
    search_fields = ['title_ng_papers', 'description_ng_papers', 'published_ng_papers', 'attach_ng_papers'] #search hiied daraah utguud match bolj baihaar

# admin.site.register(data_2023)
# admin.site.register(related_papers)