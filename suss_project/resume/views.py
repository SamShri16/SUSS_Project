from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def resume_view(request):
    score = None

    if request.method == "POST":
        resume = request.POST['resume']
        skills = request.POST['skills'].split(',')

        count = sum(1 for s in skills if s.strip().lower() in resume.lower())
        score = (count / len(skills)) * 100

    return render(request, 'resume.html', {'score': score})