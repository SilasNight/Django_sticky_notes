from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("create/", views.create_note, name="Create"),
    path("update/<int:pk>/", views.update_note, name="Update"),
    path("list/", views.list_notes, name="List"),
    path("delete/<int:pk>", views.delete_note, name="Delete"),
    path("register_user/", views.register_user, name="Register_User"),
    path("login/", views.login, name="Login"),

]
