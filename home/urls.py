from django.contrib import admin
from django.urls import path

from .views import *
from home.views import home_view

urlpatterns = [
    path('', home_view),
    path('logins/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('registers/<msg>',register,name="register"),
    path('login1/<msg>',login1,name="login1"),
    path('login2/',login2,name="login2"),
    path('thankyou/',thankyou,name="thankyou"),
    path('payment/<msg>',payment,name="payment"),
    path('otp/<msg>/',otp,name="otp"),
   # path('output/',output,name="output"),
    path('output/', output, name='script'),
  #  path('otp/',otp,name="otp"),

]
