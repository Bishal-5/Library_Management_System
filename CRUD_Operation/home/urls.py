from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('profile',views.profile, name="profile"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    path('employee/add', views.addEmployee, name="add"),
    path('employee/update/<int:id>', views.updateEmployee, name="updateEmployee"),
    path('employee/delete/<int:id>', views.deleteEmployee, name="deleteEmployee"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)