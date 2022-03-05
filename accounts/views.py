from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        mobile = request.POST['mobile']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # messages.info(request, "Username already exists")
                return JsonResponse({"status":"Username already exists"})
            elif User.objects.filter(email=email).exists():
                # messages.info(request, "Email already exists")
                return  JsonResponse({"status":"Email already exists"})
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User created')
                return  JsonResponse({"status":"User created"})
        else:
            print('Password not matched')
            return JsonResponse({"status":"Password not matched"})
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({"status":"user logged in successfully"})
        else:
            # messages.info(request, "Invalid details")
            # print("Invalid")

            return JsonResponse({"status":"Invalid credentials"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')