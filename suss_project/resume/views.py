from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def resume_view(request):

    result = None

    if request.method == 'POST':
        resume = request.POST['resume'].lower()
        skills = request.POST['skills'].lower().split(',')

        count = sum(1 for s in skills if s.strip() in resume)
        score = (count / len(skills)) * 100 if skills else 0

        result = f"{round(score,2)} % match"

    return render(request, 'resume.html', {'result': result})
