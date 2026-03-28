from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('search')   # login success → search page
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')


from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def search_train(request):
    return render(request, 'search.html')

from .models import Train

def search_train(request):
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']

        trains = Train.objects.filter(
            source__iexact=source,
            destination__iexact=destination
        )

        return render(request, 'search.html', {'trains': trains})

    return render(request, 'search.html')



def search_train(request):
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']

        print("FROM:", source)
        print("TO:", destination)

        trains = Train.objects.filter(
            source__iexact=source,
            destination__iexact=destination
        )

        print("RESULT:", trains)

        return render(request, 'search.html', {'trains': trains})

    return render(request, 'search.html')



from .models import Train

def book_ticket(request, train_id):
    train = Train.objects.get(id=train_id)

    if request.method == 'POST':
        name = request.POST['name']

        if train.seats > 0:
            train.seats -= 1
            train.save()
            return render(request, 'success.html', {'name': name, 'train': train})
        else:
            return render(request, 'booking.html', {'train': train, 'error': 'No seats available'})

    return render(request, 'booking.html', {'train': train})


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')

