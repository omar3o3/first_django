from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from django.shortcuts import render

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("welcome to my first django application")

    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog")


class Article(View):
    def get(self, request):
        articles = [
            {
                'title': "python is cool",
                'category': 'tech',
                'content': 'blah blah blah blah',
                'author': 'guido',
                'creation_date': datetime.now()
            },
            {
                'title': 'tesla goes bankrupt',
                'category': 'auto',
                'content': 'blah2 blah2 blah2 blah2',
                'author': 'elon musk',
                'creation_date': datetime.now()
            }
        ]

        return render(request, 'articles.html', {'articles': articles})
