from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created")
        return redirect('/login/')

    return render(request, 'register.html')