from django.urls import path
from .views import index, results, register, loginPage, logoutUser, deleteUser, validateUsername

urlpatterns = [
    path('', index, name='index'),
    path('results/', results),
    path('register/', register, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name='logout'),
    path('delete/', deleteUser, name='delete'),
    path('validateUsername/', validateUsername, name="validateUsername"),
]