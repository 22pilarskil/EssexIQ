from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', views.return_view, name='home'),
    path('about-us', views.return_view, name='about-us'),
    path('contact-us', views.return_view, name='contact-us'),
    path('summer-session-2020', views.return_view, name="summer2020"),
    path('winter-session-2021', views.return_view, name='winter2021'),
    path('spring-session-2021', views.return_view, name='spring2021'),
    path('summer-session-2021', views.return_view, name="summer2021")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)