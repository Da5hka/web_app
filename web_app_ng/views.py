from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NGserializer
from .models import data_2023
from rest_framework.authentication import TokenAuthentication

class Another(View):

    data_papers = data_2023.objects.all() #filter tei data nemj bolno for example: data_2023.objects.filter(is_published=True)
    output = ''

    for papers in data_papers:

        output += f"We have {papers.title} papers with attach {papers.cover} {papers.published}. <br>"

    def get(self, request):
        return HttpResponse(self.output)


#herwee temlate ashiglawal ingej ywna
# def first(request):
#    return render(request, 'temp.html') #end zarlagdsan baiga view-iig url-ru duudna


class NgViewSet(viewsets.ModelViewSet):
    serializer_class = NGserializer
    queryset = data_2023.objects.all() #viewset deer REST deer haragdah heseg baina.
    
    authentication_classes = (TokenAuthentication, )