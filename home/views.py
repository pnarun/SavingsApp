from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from home.models import user_register,savings,transactions
import requests,random,datetime
from django.contrib.auth.decorators import login_required

uname = ""
amount_to_be_paid = ""


def home_view(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('/home/')


def register(request,msg):
    global uname    
    if request.method == "POST":
        # if k :
        #     messages.success(request,"Username already exists...If it is not you then change the username")     
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        uname = username
        # msg = "Username already exists...If it is not you then change the username"
        check = None
        try:
            check = user_register.objects.get(username=username)
        except:
            check = None
        if check:
            # k = True
           # messages.success(request,"Username already exists...If it is not you then change the username")
            return HttpResponseRedirect("/home/registers/Username already exists")
            # return redirect('/home/registers')
        else:
            k = False
            user = user_register.objects.create(username=username,firstname=firstname,lastname=lastname,email=email,password=password,contact=contact)
            user.save()
            #  return render(request,'auth/login1.html',{'name':username})
            return redirect('/home/login1/You have successfully signed up')
    else:
        # k = False
       # user_form = UserRegisterForm()
        return render(request,'auth/signup.html',{'msg':msg})

# @login_required(login_url='/home/logins/')
def thankyou(request):
    return render(request,'thankyou.html')

# @login_required(login_url='/home/logins/')
def otp(request,msg):
    if request.method=="POST":
        # me = "Welcome to OTP portal"
        otp = request.POST.get('otp')
        with open("test.txt",'r') as f: 
            rn=f.readline()
            ts=f.readline()
        now=datetime.datetime.now()
        ki = str(now)
        ko = ki.split('.')
        date_time_obj1 = datetime.datetime.strptime(ko[0], '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        print(date_time_obj1)
        rn=int(rn)
        sec = (date_time_obj1-date_time_obj2).total_seconds()
        otp=int(otp)
        print(rn,otp)
        print(type(rn),type(otp))
        # print(len(rn),len(otp))
        if (sec > 40) :
            return HttpResponseRedirect('/home/otp/OTP has been expired')
        elif rn!=otp :
             return HttpResponseRedirect('/home/otp/Please enter valid OTP')
        else:
            return redirect('/home/thankyou/')
    else:
        return render(request,'auth/otp.html',{'msg':msg})
   # return render(request,'auth/otp.html',{'msg':msg})
   # return HttpResponseRedirect('/home/otp/Welcome to OTP portal')

# @login_required(login_url='/home/logins/')
def output(request):
    url = "https://www.fast2sms.com/dev/bulk"
    print(url)
    a = random.randint(100000,1000000)
    t = datetime.datetime.now()
    print(a)
    payload = "sender_id=FSTSMS&message=OTP for Daily-savings accont is "+str(a)+"&language=english&route=p&numbers=8660397320"
    headers = {
    'authorization': "9xKglUsrzcenHoFthGT567j4p1E2OX8qSBiudk3wVvZ0yfLYmCu6ITcFfYeKin4kaChPQHoBVNzZryl0",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    rn=str(a)
    ts=str(t)
    k = ts.split('.')
    # print(k[0])
    date_time_obj = datetime.datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S')
    print(date_time_obj)
    # print(k[0])
    with open("test.txt",'w+') as f:  
        f.write(str(a)+'\n')
        f.write(str(k[0]))
    print("DONE")
    #message = "OTP has been sent to your registered mobile number"
    #return render(request, 'otp.html', {'msg':message})
    return HttpResponseRedirect('/home/otp/OTP has been sent to your registered mobile number')

# def verify(request):
#     with open("test.txt",'r') as f:  
#         rn=f.readline()
#         ts=f.readline()
#     # print(rn,ts)
#     now=datetime.datetime.now()
#     ki = str(now)
#     ko = ki.split('.')
#     # print(now)
#     # print(ko)
#     date_time_obj1 = datetime.datetime.strptime(ko[0], '%Y-%m-%d %H:%M:%S')
#     date_time_obj2 = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
#     print(date_time_obj1)
#     rn=int(rn)
#     sec = (date_time_obj1-date_time_obj2).total_seconds()

#     if sec > 60:
#         if 



# def output(request):
#     url = "https://www.fast2sms.com/dev/bulk"
#     print(url)
#     a = random.randint(100000,1000000)
#     t = datetime.datetime.now()

#     print(a)
#     payload = "sender_id=FSTSMS&message=OTP for Daily-savings accont is "+str(a)+"&language=english&route=p&numbers=8660397320"
#     headers = {
#     'authorization': "9xKglUsrzcenHoFthGT567j4p1E2OX8qSBiudk3wVvZ0yfLYmCu6ITcFfYeKin4kaChPQHoBVNzZryl0",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     }
#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)
#     rn=str(a)
#     ts=str(t)
#     k = ts.split('.')
#     # print(k[0])
#     date_time_obj = datetime.datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S')
#     print(date_time_obj)
#     # print(k[0])
#     with open("test.txt",'w+') as f:  
#         f.write(str(a)+'\n')
#         f.write(str(k[0]))

#     print("DONE")
#     time.sleep(5)

#     with open("test.txt",'r') as f:  
#         rn=f.readline()
#         ts=f.readline()
#     # print(rn,ts)
#     now=datetime.datetime.now()
#     ki = str(now)
#     ko = ki.split('.')
#     # print(now)
#     # print(ko)
#     date_time_obj1 = datetime.datetime.strptime(ko[0], '%Y-%m-%d %H:%M:%S')
#     date_time_obj2 = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
#     print(date_time_obj1)
#     rn=int(rn)

#     print((date_time_obj1-date_time_obj2).total_seconds())
#     return render(request, 'auth/otp.html',{'msg':a})


def user_login(request):
    global uname
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        uname = username
        user1=None
        try:
            user1 = user_register.objects.get(username=username,password=password)
        except:
            user1=None        
        if user1 :
            return redirect('/home/login2/')        
        else:
            messages.success(request,"Invalid Login Details given")
            return render(request,'auth/loginuser.html')
    else:
        return render(request,'auth/loginuser.html',{})

 
       

# @login_required(login_url='/home/logins/')
def login1(request,msg):
    global uname 
    if request.method == "POST":        
        MoneytobeSaved =request.POST.get('money_to_be_saved')
        deadline = request.POST.get('deadline')
        uname= request.POST.get('username')
        
        #return redirect('/home/login2/')
        date_format = "%Y-%m-%d"
        date = str(datetime.datetime.now())
        date = date.split(' ')
        a = datetime.datetime.strptime(date[0], date_format)
        b = datetime.datetime.strptime(deadline, date_format)
        delta = b-a
            # print(delta.days)
        if delta.days > 0:
            log = savings.objects.create(username=uname,money_to_be_saved=MoneytobeSaved,deadline=deadline)
            log.save()
                # return render(request, "auth/login1.html", {'value1': MoneytobeSaved, 'value2': deadline, 'choice': choice, 'key': 'True', 'name': uname})
            return redirect('/home/login2/')
        else:
            return HttpResponseRedirect('/home/login1/Invalid Deadline')
        #return redirect('/home/login2')

    else:
        # return HttpResponse("Invalid Login Details given")
        return render(request, 'auth/login1.html', {'name': uname,'msg':msg})
        # else:
        #     return render(request,'auth/login1.html')
        #return HttpResponse("Hello")
    # else:
    #      return HttpResponse("Invalid Login Details given")
    #     return render(request,'auth/login1.html',{'name':uname})
        # user = savings.objects.create(username=username,MoneytobeSaved=MoneytobeSaved,deadline=deadline)
        # user.save()
        
# @login_required(login_url='/home/logins/')
def payment(request,msg):
    if request.method == "POST" :          
        global uname,amount_to_be_paid
        nameoncard = request.POST.get('nameoncard')
        cardnumber = request.POST.get('cardnumber')
        expirymonth = request.POST.get('expirymonth')
        expiryyear = request.POST.get('expiryyear')
        date=str(datetime.datetime.now())
        k = date.split(' ')
        p = str(k[0])
        p=p.split('-')
        if (expiryyear == p[0] and expirymonth > p[1]) or (expiryyear > p[0]) :
            log = transactions.objects.create(username=uname, amountpaid=amount_to_be_paid)
            log.save()
            return redirect('/home/otp/ /')
        else:
            return HttpResponseRedirect('/home/payment/Your card is expired')
    else:
        return render(request,'auth/payment.html',{'msg':msg})

# @login_required(login_url='/home/logins/')
def login2(request):
    global uname,amount_to_be_paid 
    print(uname)
    value1 = "hi"
    value2 = 'hii'
    value3 = '456456'
    if request.method == "POST":
        amount = request.POST.get('amount_to_be_paid')
        uname= request.POST.get('username')
        amount_to_be_paid = amount
        # log = transactions.objects.create(username=uname, amountpaid=amount_to_be_paid)
        # log.save()
        return redirect('/home/payment/Card Details Please')
    else:
        return render(request, 'auth/login2.html', {'value1': value1, 'value2': value2, 'value3': value3,'name':uname})

# def otp(request):
#     if request.method == "POST":
#         otp = request.POST.get('otp')
#     else:
#         return render(request,'otp.html')