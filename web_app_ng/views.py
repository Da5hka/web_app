from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from .models import data_2023

class Another(View):

    data_papers = data_2023.objects.all() #filter tei data nemj bolno for example: data_2023.objects.filter(is_published=True)
    output = ''

    for papers in data_papers:

        output += f"We have {papers.title} papers with attach {papers.cover} {papers.published}. <br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('Hello') #end zarlagdsan baiga view-iig url-ru duudna
