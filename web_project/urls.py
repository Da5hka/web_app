from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
#from allauth.account.views import confirm_email as allauthemailconfirmation
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('web_app_ng.urls')),
    path('auth/', obtain_auth_token),
    #url(r'^api/rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$',allauthemailconfirmation,name='account_confirm_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
