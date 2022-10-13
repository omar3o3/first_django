from django.urls import path
from django.urls import include
from .views import Home, Article

urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]
