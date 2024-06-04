from django.contrib import admin
from django.urls import path
from .views import *
app_name='core'
urlpatterns =[
    path('start/<category>/',start,name='start'),
    path('createFund/',create_fundraiser,name='create'),
    path('login/',sign_in,name='sign_in'),
    path('logout/',logout_page,name='logout'),
    path('register/',sign_up,name='sign_up'),
    path('reset/',reset_password,name='reset'),
    path('send/',send_email,name='send'),
    path('fundme/<id>/',showFundDetails,name='show'),
    path('donate/<id>/',donate,name='donate'),
]