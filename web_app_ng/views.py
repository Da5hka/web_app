from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .serializers import Paperserializer, NG_PPT_serializer, UserSerializer
from .models import data_2023, related_papers
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.core.mail import EmailMessage

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() #viewset deer REST deer haragdah heseg baina.
    authentication_classes = (TokenAuthentication, )

    def create(self, request):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                # Save the data
                serializer.save()

                response_data = {'message': 'User Created!!'}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaperViewSet(viewsets.ModelViewSet):
    serializer_class = Paperserializer
    queryset = data_2023.objects.all() #viewset deer REST deer haragdah heseg baina.
    authentication_classes = (TokenAuthentication, )
    #permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        QuerySetFilter = data_2023.objects.filter(is_approved=True)
        return QuerySetFilter
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_post = request.user.username
        #print(username)

        title = serializer.validated_data.get('title')
        if not title:
            return Response({'error': 'Title cannot be empty for a POST request.'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            if serializer.is_valid():
                # Save the data
                message_body = f" A new paper applicaton was submitted. Pls check and approve, Username: {username_post}"
                email_message = EmailMessage("Paper submission confirmation", message_body, to=['verifynog@gmail.com'])
                email_message.send()

                serializer.save()

                response_data = {'message': 'Data saved successfully. Pls wait admin approval'}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PptViewSet(viewsets.ModelViewSet):
    serializer_class = NG_PPT_serializer
    queryset = related_papers.objects.all() #viewset deer REST deer haragdah heseg baina.
    
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow all authenticated users to access the GET method
            return [IsAuthenticated()]
        elif self.request.method in ['POST', 'PUT', 'DELETE']:
            # Allow only admin users to access the POST, PUT, and DELETE methods
            return [IsAdminUser()]
        else:
            # For other methods, use the default permissions
            return super().get_permissions()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        custom_message = response.data.get('custom_message', 'Data saved successfully')

        return Response({'message': custom_message})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        custom_message = response.data.get('custom_message', 'Data saved successfully')

        return Response({'message': custom_message})
    
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        custom_message = response.data.get('custom_message', 'Data destroyed successfully')

        return Response({'message': custom_message})
       