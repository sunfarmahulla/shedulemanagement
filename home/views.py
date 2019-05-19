from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ScheduleList, FoodDetails



# Create your views here.

def home(request):
    schedule = ScheduleList.objects.all()
    return render(request, 'home.html', {'schedule': schedule})


def user_registration(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registerd')
            return redirect('/')
        # If the request params is valid save the data else return form with error
    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/account/login')
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})

def add_food(request):
    print("hello form submitted")
    user_id = request.POST["user_id"]
    food_name = request.POST["food_name"]
    DateTaker = request.POST["DateTaker"]
    TimeTaker = request.POST["TimeTaker"]
    schedule = ScheduleList(user_id=user_id, food_name=food_name, DateTaker=DateTaker, TimeTaker=TimeTaker )
    schedule.save()
    return render(request, 'home.html', {})


def ADDFood(request):

    return render(request, 'home.html', {})


def delete(request, id):
    schedule = ScheduleList.objects.get(pk=id)
    schedule.delete()
    return redirect('/')

def edit(request):
    print("hello form update")
    id = request.GET["id"]
    schedule = ScheduleList.objects.get(pk=id)
    schedule.food_name = request.GET["food"]
    schedule.DateTaker = request.GET["date"]
    schedule.TimeTaker = request.GET["time"]
    schedule.save()
    return render(request, "home.html", {})

def food_details(request):
    return render(request, 'FoodDetails.html', {})

def foodData(request):

    details = FoodDetails.objects.all()
    return render(request, 'FoodDetails.html', {'details': details})

def TodoList(request):
    return render(request, 'ToDoList.html')


