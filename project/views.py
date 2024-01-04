from sqlite3 import Time
from xmlrpc.client import DateTime
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from email.message import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as LL
from project.models import User,Driver,Updates,Report,Trip,Schedule
from project.forms import contactformemail
from datetime import datetime ,timedelta
import googlemaps
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . forms import MyfileuploadForm
import smtplib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request as ReqReq

from datetime import time
from googlesearch import search
keyy='AIzaSyAsUJ0P3eueaI2IdbInU6P4I6amqPyYHUI'
gmaps = googlemaps.Client(key=keyy)

# Create your views here.
def index(request):
    return render(request,'index.html')
def abouthome(request):
    return HttpResponse("Home page")
def add(request,a,b):
    return HttpResponse(a+b)
def myfirstpage(request):
    return render(request,'index.html')
@csrf_exempt
def login(request):
    
    if request.method == "POST":
        name=request.POST['name']
        pass1=request.POST['password']
        myuser = authenticate(request,username=name,password=pass1)
        if myuser is not None:
            LL(request, myuser)
            if myuser.is_authenticated and myuser.is_passenger==True :
                '''trips= Trip.objects.filter(DateTime.time() >datetime.now().time())
                print("***************************\n")
                print(len(trips))
                now = datetime.now().time()
                if trips.DateTime.time()>now:
                    print("driver 1\n")
                else:
                    print("driver 2\n")'''
                print("***************************\n")
                return redirect('PassengerHomePage') #Go to student home
            elif Driver.objects.filter(username=myuser.username):
                return redirect('DriverHomePage') #Go to  home
            elif myuser.is_authenticated and myuser.is_Admin==True :
                return redirect('AdminHomePage') #Go to  home
        else:
            messages.error(request,"Invalid email or password")
            return redirect('login')
    return render(request,'project/login.html')
def signup(request):
    if request.method == "POST" :
        name=request.POST['username']
        pass1=request.POST['pass1']
        email=request.POST['email']
        fname=request.POST.get('Fname')
        lname=request.POST.get('Lname')
        myuser=User.objects.create_user(name,email,pass1)
        myuser.first_name=fname
        myuser.email=email
        myuser.last_name=lname
        myuser.is_passenger=True
        myuser.save()
        messages.success(request,"succseful")
        LL(request, myuser)
        return redirect('login')
    messages.error(request,"not added")
    return render(request,'project/signup.html')
def DriverSignup(request):
    if request.method == "POST":
        email=request.POST.get('Demail')
        fname=request.POST.get('DFname')
        lname=request.POST.get('DLname')
        companyName=request.POST.get('companyname')
        phone=request.POST.get('Dhone')
        myuser=Driver.objects.create_user(username=fname+" "+lname,password="1111")
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.companyName=companyName
        myuser.phone=phone
        myuser.save()
        messages.success(request,"succseful")
        LL(request, myuser)
        return redirect('DriverFile')
    return render(request,'project/DriverSignup.html')
def AdminHomePage(request):
    return render(request,'project/AdminHomePage.html')
def AdminReports(request):
    reports=Report.objects.all()
    return render(request,'project/AdminReports.html',{'users':reports})
def AddNewDriver(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('pass')
        myuser=Driver.objects.create_user(username=name,password=password)
        myuser.its_ok=False
        myuser.certificate="no-photo-icon-22.jpg"      
        myuser.License="no-photo-icon-22.jpg"
        myuser.save()
        messages.success(request,"succseful")
        return redirect('AdminHomePage')
    return render(request,'project/AddNewDriver.html')  
# Request directions via public transit
def Busway(fromm,to):
     now = datetime.now()
     directions_result = gmaps.directions(fromm,to,mode="transit",departure_time=now)
     bus_num=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['short_name']
     bus_stations=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['name']
     bus_company=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['agencies'][0]['name']
     return [bus_num,bus_stations,bus_company]
def PassengerHomePage(request):
    if  request.method=='POST':
        fromm=request.POST.get('fromm')
        too=request.POST.get('tooo')
        request.session['fromm'] = fromm
        request.session['tooo'] = too
        print("***************************************\n\n\n")
        print(request.session['fromm'],request.session['tooo'] ) 
        print("***************************************\n\n\n")
        print(fromm,too) 
        print("***************************************\n\n\n")
        k=Busway(request.session['fromm'],request.session['tooo'])
        return redirect('PassengerGetDic',busnum=k[0],buscompany=k[2])
    return render(request,'project/PassengerHomePage.html')
@csrf_exempt
def PassengerGetDic(request,busnum,buscompany):
    hhelp="אוטובוס קרוב קו"
    result=list(search(request.session['tooo']+"  "+ request.session['fromm'] +  ' '+busnum +' '+hhelp))
    for i in result[:20]: 
        domain = urlparse(i).netloc
        print(domain.split('.')[0])
        if domain.split('.')[0]=='xn--4dbclabp0e':
            url=i
            break
    client = ReqReq(url, headers={"User-Agent" : "Mozilla/5.0"})
    page = urlopen(client).read()
    soup = BeautifulSoup(page, 'html.parser')
    k=soup.find_all("input")
    companies = [com.text for com in soup.find_all('b')]
    k=Busway(request.session['fromm'],request.session['tooo'])
    if request.method =='POST':
        user=request.user.username
        fr=request.POST.get('frfr')
        to=request.POST.get('toto')
        SFrom=request.POST.get('fromst')
        STo=request.POST.get('tost')
        Bus=request.POST.get('full_name')
        DTime=request.POST.get('deptime')
        a=DTime[11:13]
        b=DTime[14:16]
        c=DTime[17:19]
        hour=time(int(a),int(b),int(c))
        end=time(int(a)+1,int(b),int(c))
        obj=Schedule.objects.filter(From=fr,To=to,BusLine=busnum,Time__range=[hour,end])
        A=Trip(username=user,To=STo,Driver=obj[0].DriverName,From=SFrom,BusLine=Bus,DateTime=DTime)
        A.save()
        return redirect('PassengerHomePage')
    return render(request,'project/PassengerGetDic.html',{'busnum':busnum,'buscompany':buscompany,'busstation':k[1],'fromm':request.session['fromm'],'too':request.session['tooo'],'stations':companies})
@csrf_exempt
def PassengerProfile(request,id):
    user=get_object_or_404(User,id=id)
    return render(request,'project/PassengerProfile.html',{'user':user})
@csrf_exempt
def DriverFile(request):
    context = {
        'form':MyfileuploadForm()
    }
    if request.method == 'POST':
        driver=Driver(request.POST,request.FILES)
        if driver is not None:
            myuser=Driver.objects.get(username=request.user.username)
            license=request.FILES.get('License')
            Certificate=request.FILES.get('certificate')
            myuser.certificate=Certificate      
            myuser.License=license
            myuser.save()
            return redirect('login')
    return render(request,'project/DriverFile.html',context)
def DriverHomePage(request):
     return render(request,'project/DriverHomePage.html')
def Request(request):
    userList= Driver.objects.filter(is_ok=False)
    return render(request, 'project/Request.html', {'users': userList})
def PMyTrip(request):
    trips= Trip.objects.filter(username=request.user.username)
    return render(request,'project/PMyTrip.html',{'trips':trips})
def PassengerListForDriver(request,bus):
    trips= Trip.objects.filter(BusLine=bus)
    return render(request,'project/PassengerListForDriver.html',{'trips':trips})
def DriverDetails(request):
    user= Driver.objects.filter(is_ok=True)
    return render(request,'project/DriverDetails.html',{'users': user})
def details(request,id):
    user=get_object_or_404(Driver,id=id)
    return render(request,'project/detail.html',{'user':user})
def accept(request,id):
    user=get_object_or_404(Driver,id=id)
    user.is_ok=True
    user.save()
    return redirect('AdminHomePage')    
def DeleteOrder(request,id):
    obj=get_object_or_404(Trip,id=id)
    obj.delete()
    return redirect('PassengerHomePage')    
def decline(request,id):
    obj=get_object_or_404(Driver,id=id)
    obj.delete()
    return redirect('AdminHomePage')    
def logout_user(request):
    logout(request)
    return redirect('login')
def SendMail(request):
    if request.method=="POST":
        full_name = request.POST['full_name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
        subject,
        message,
        'from@emample.com',
        [email],
        fail_silently=False,        
        ) 
        return redirect('AdminHomePage')    
    return render(request,'project/SendMail.html')
def  deluser(request):
    user= User.objects.filter(is_passenger=True)
    return render(request,'project/deluser.html',{'users': user})
def delete(request,id):
    obj=User.objects.get(id=id)
    obj.delete()
    return redirect('deluser')
def Block(request,id):
    obj=Report.objects.get(id=id)
    A=User.objects.filter(username=obj.UserName)
    A.delete()
    obj.delete()
    return redirect('AdminHomePage')
def deleteDriver(request,id):
    obj=get_object_or_404(Driver,id=id)
    obj.delete()
    return redirect('DriverDetails') 
def logoutUser(request):
    logout(request)
    return redirect('login')
@csrf_exempt
def DriverNotification(request):
    if request.method == "POST":
        senderID=request.user.username
        message=request.POST.get('Notification')
        bussNum=request.POST.get('BusNum')
        A=Updates(senderID=senderID,BusLine=bussNum,message=message)
        A.save()
        return redirect('DriverHomePage')
    return render(request,'project/DriverNotification.html')
def NotificationByDriver(request):  
    return render(request,'project/NotificationByDriver.html')  
def PassengerNotification(request):
    if request.method == "POST":
        busline=request.POST.get('bus_line')
        user=Updates.objects.filter(BusLine=busline)
        return render(request,'project/NotificationByDriver.html',{'updates':user})
    return render(request,'project/PassengerNotification.html')
def DriverChangePassword(request,id):
    user=get_object_or_404(Driver,id=id)
    if request.method=="POST":
        old_pass=request.POST.get('full_name')
        new_pass=request.POST.get('email')
        cpass=request.POST.get('confirmPassword')
        user1 = authenticate(username=user.username,password=old_pass)
        if user1 is not None and new_pass==cpass:
            user1.set_password(new_pass)
            user1.save()
            return render(request,'project/DriverHomePage.html',{'user':user})
    return render(request,'project/DriverChangePassword.html',{'user':user})
def PassengerPassword(request,id):
    user=get_object_or_404(User,id=id)
    if request.method=="POST":
        old_pass=request.POST.get('full_name')
        new_pass=request.POST.get('email')
        cpass=request.POST.get('confirmPassword')
        user1 = authenticate(username=user.username,password=old_pass)
        if user1 is not None and new_pass==cpass:
            user1.set_password(new_pass)
            user1.save()
            return render(request,'project/PassengerHomePage.html',{'user':user})
    return render(request,'project/PassengerPassword.html',{'user':user})
def MyDrive(request):
    #trips=Trip.objects.all().values('BusLine').distinct()
    trips=Trip.objects.filter(Driver=request.user.username)
    return render(request,'project/MyDrive.html',{'trips':trips})
def PassenegrTripInfo(request,id):
    trip=get_object_or_404(Trip,id=id)
    return render(request,'project/PassenegrTripInfo.html',{'trip':trip})
def report(request,id):
    obj=Trip.objects.get(id=id)
    A=Report(UserName=obj.username)
    A.save()
    return redirect('DriverHomePage')
def endtrip(requedt,id):
    obj=get_object_or_404(Trip,id=id)
    obj.delete()
    return redirect('DriverHomePage')
def new_list(response):
    hhelp="אוטובוס קרוב קו"
    result=list(search(tooo+"ל"+ fromm +  BusNum +hhelp))
    print(result)
    url=result[2]
    client = Request(url, headers={"User-Agent" : "Mozilla/5.0"})
    page = urlopen(client).read()
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    k=soup.find_all("input")
    #print(k)
    companies = [com.text for com in soup.find_all('b')]
    return redirect('PassengerGetDic')
