from django.urls import path
from .views import register, loginPage, logoutUser, deleteUser, livroCreateView, livrosListView, livroUpdateView, livroDeleteView

app_name = "livros"

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name='logout'),
    path('delete/', deleteUser, name='delete'),

    path('', livrosListView, name='home-livros'),
    path('cria/', livroCreateView, name='cria-livros'),
    path('atualiza/<int:pk>/', livroUpdateView, name='atualiza-livro'),
    path('apaga/<int:pk>/', livroDeleteView, name='apaga-livro'),
]
