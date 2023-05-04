from django.http import HttpResponse
from django.shortcuts import render

articles = [
    {
        "id":1,
        "title":"First one",
        "description":"It works?"
    },
    {
        "id":2,
        "title":"Second one",
        "description":"It works!"
    }
]

# Create your views here.
def index(req):
    #return render(req, "news_blog/index.html", {"articles":articles})
    return render(req, "news_blog/news_list.html", {"articles":articles})

def get_by_id(req, id):
    for article in articles:
        if (article.id != id):
            continue
        return render(req, "news_blog/news_article.html", {"article":article})