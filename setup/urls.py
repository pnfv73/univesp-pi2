from django.contrib import admin
from django.urls import path, include
#from contas.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('allauth.urls')),
    #path('', index)
]
