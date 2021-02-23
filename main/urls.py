from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.return_view, name='home'),
    path('about-us', views.return_view, name='about-us'),
    path('contact-us', views.return_view, name='contact-us'),
    path('winter-session', views.return_view, name='winter'),
    path('spring-session', views.return_view, name='spring'),
    path('summer-session', views.return_view, name="summer"),
]