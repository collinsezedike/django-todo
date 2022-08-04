from django.urls import path

from .views import (
	ListTodoAPIView,
	CreateTodoAPIView,
	UpdateTodoAPIView,
	DeleteTodoAPIView,
	)


urlpatterns = [
	path("", ListTodoAPIView.as_view(), name="todo-list"),
	path("create/", CreateTodoAPIView.as_view(), name="todo-create"),
	path("update/<int:pk>/", UpdateTodoAPIView.as_view(), name="todo-update"),
	path("delete/<int:pk>/", DeleteTodoAPIView.as_view(), name="todo-delete"),

]