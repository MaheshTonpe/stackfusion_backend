from django.urls import path 
from app.controllers.user_api import UserView


urlpatterns = [
    path("user/list/", UserView.as_view({"get": "list", "post": "create"})),
    path("user/<int:pk>/", UserView.as_view({"get": "retrieve", "put": "edit", "delete": "destroy"}))
]