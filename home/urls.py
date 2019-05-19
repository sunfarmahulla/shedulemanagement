from django.urls import path
from .views import home, user_registration, user_profile, edit, delete, add_food, ADDFood, food_details, TodoList, foodData


urlpatterns = [
    path('', home, name='home'),
    path('user-registration', user_registration, name='user_registration'),
    path('user-profile', user_profile, name='user_profile'),
    path('edit', edit, name='edit'),
    path('delete/<id>/', delete, name='delete'),
    path('add_food', add_food, name='add_food'),
    path('ADDFood', ADDFood, name='ADDFood'),
    path('food_details', food_details, name='food_details'),
    path('TodoList', TodoList, name='TodoList'),
    path('foodData', foodData, name="foodData")

]
