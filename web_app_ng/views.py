from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import Paperserializer, NG_PPT_serializer
from .models import data_2023, related_papers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

class PaperViewSet(viewsets.ModelViewSet):
    serializer_class = Paperserializer
    queryset = data_2023.objects.all() #viewset deer REST deer haragdah heseg baina.
    authentication_classes = (TokenAuthentication, )
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        if not title:
            return Response({'error': 'Title cannot be empty for a POST request.'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            if serializer.is_valid():
                # Save the data
                serializer.save()

                response_data = {'message': 'Data saved successfully'}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PptViewSet(viewsets.ModelViewSet):
    serializer_class = NG_PPT_serializer
    queryset = related_papers.objects.all() #viewset deer REST deer haragdah heseg baina.
    
    authentication_classes = (TokenAuthentication, )