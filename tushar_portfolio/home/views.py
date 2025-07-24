from django.shortcuts import render

print("THIS IS MY HOME.VIEWS.PY 00")
def home_view(request):
    return render(request, 'home.html')