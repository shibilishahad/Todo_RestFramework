from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', Registration.as_view(), name='registration' ),
    path('logout/', Logout.as_view(), name='logout'),
    path('category/', CategoryListCreate.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestory.as_view(), name='category-retrieve-update-destory'),
    path('todo/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todo/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(), name='todo-retrieve-update-destroy'),
]
