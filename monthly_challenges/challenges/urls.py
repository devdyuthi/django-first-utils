from django.urls import path
from challenges import views


urlpatterns = [
    # "<>" is a placeholder format used in django
    path("", views.index, name="index"),  # ? /challenges/
    path("<int:month>", views.monthly_challenge_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")

]
