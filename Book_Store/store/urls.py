from django.urls import path
from store import views

# Django rounting files
# URL Parameters --> 
urlpatterns = [
    path('',views.home, name="home"),
    path('addbook', views.addbook, name="addbook"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('parameter/<int:number>', views.parameter, name="parameter")
]