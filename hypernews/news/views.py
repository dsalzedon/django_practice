from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from django.conf import settings
import json

jpath = settings.JPATH


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class News(View):
    def get(self, request, news_link, *args, **kwargs):

        if news_link not in news_links:
            raise Http404
        else:
            for x in news_file:
                if x["link"] == int(news_link):
                    break
            return render(
                request,
                "news/index.html",
                context={"title": x["title"], "date": x["created"], "text": x["text"]},
            )


with open(jpath, "r") as jsonfile:
    news_file = json.load(jsonfile)
    news_links = [str(x["link"]) for x in news_file]
