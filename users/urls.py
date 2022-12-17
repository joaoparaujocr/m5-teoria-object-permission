from django.urls import path

from . import views

urlpatterns = [
    path("computers/<int:computer_id>/", views.RetrieveComputerView.as_view()),
]
