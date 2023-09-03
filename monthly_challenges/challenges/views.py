from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "bonkey bonkey bomp bomp",
    "february": "walk 10 min a day",
    "march": "learn django",
    "april": "go vegan for a month",
    "may": "walk 10 min a day",
    "june": "learn django",
    "july": "DO SOOO MANY HEAD-BOBS",
    "august":  "eat sorakaya",
    "september": "learn django",
    "october": " 🎶1 2 3 4 5 numberblocks 6 7 8 9 10 numberblocks!🎶 dont sing like that ",
    "november": "YOU SHOULD EAT CARROT CAKE ",
    "december": "EAT mutton biryani"
}
# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month value</h1>")
    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # *must pass request as a first argument for render*
        return render(request, "challenges/month.html", {
            "text": challenge_text,
            "month_name": month
        })

    except:
        raise Http404()
