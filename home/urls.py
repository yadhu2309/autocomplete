from django.urls import path, include
from home import views
urlpatterns = [
  
    path('', views.get_names),
    path('index/', views.home),

]