from django.urls import path
from . import views

urlpatterns = [
    # ... other URLs
    path("ask/", views.ask_assistant, name="ask_assistant"),
]
