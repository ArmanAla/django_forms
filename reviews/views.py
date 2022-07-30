from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(req):
    if req.method == "POST":
        entered_username = req.POST["username"]
        print(entered_username)
        return HttpResponseRedirect("/thank_you")
        
    return render(req, "reviews/review.html")


def thank_you(req):
    return render(req, "reviews/thank_you.html")