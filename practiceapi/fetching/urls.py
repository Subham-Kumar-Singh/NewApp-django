from django.urls import path
from . import views
urlpatterns = [
    # path('',views.Home),
    path('',views.Apifetch,name="Apifetch_func"),
]
