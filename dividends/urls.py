from django.urls import path

from . import views

urlpatterns = [
    path("", views.DividendList.as_view(), name="list"),
    path("create/", views.DividendCreate.as_view(), name="create"),
    path("<int:pk>/update/", views.DividendUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", views.DividendDelete.as_view(), name="delete"),
]
