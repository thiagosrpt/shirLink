from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('<str:uuid>', views.go, name="go")
]