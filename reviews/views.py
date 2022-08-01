from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def review(req):
    # if req.method == "POST":
    #     entered_username = req.POST["username"]
        
    #     if entered_username == "":
    #         return render(req, "reviews/review.html", {
    #             "has_error": True
    #         })
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank_you")
    form = ReviewForm()
        
    return render(req, "reviews/review.html", {
        "form": form
    })


def thank_you(req):
    return render(req, "reviews/thank_you.html")