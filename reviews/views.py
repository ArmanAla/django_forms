from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(req):
    if req.method == "POST":
        entered_username = req.POST["username"]
        
        if entered_username == "":
            return render(req, "reviews/review.html", {
                "has_error": True
            })
        print(entered_username)
        return HttpResponseRedirect("/thank_you")
        
    return render(req, "reviews/review.html", {
        "has__error": False
    })


def thank_you(req):
    return render(req, "reviews/thank_you.html")