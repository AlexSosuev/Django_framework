from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game/', views.game, name='game'),
    path('statistics/', views.statistics, name='statistics'),
    path('create/', views.create_authors, name='create'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("coin/<int:num>/", views.coin, name="coin"),
    path("cube/<int:num>/", views.cube, name="cube"),
    path("number/<int:num>/", views.number, name="number"),
    path("all_games/", views.all_games, name="all_games"),
    path("add_author/", views.add_author, name="add_author"),
]