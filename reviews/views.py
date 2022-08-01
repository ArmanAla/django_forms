from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def review(req):
    if req.method == "POST":
        form = ReviewForm(req.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank_you")
    else:
        form = ReviewForm()
        
    return render(req, "reviews/review.html", {
        "form": form
    })


def thank_you(req):
    return render(req, "reviews/thank_you.html")