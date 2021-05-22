from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #path('', include('leads.urls')),
    path('', include('user.urls')),
    #path('', include('UserDefault.urls')),
    #path('test1/<int:user>', views.UserRetrieve.as_view()),
]