from django.shortcuts import render

print("THIS IS MY RESUME.VIEWS.PY 00")
def resume_view(request):
    return render(request, 'resume.html')
