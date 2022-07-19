from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Appointment, Docter, Patient

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def contact(request):
    return render(request,'app/contact.html')

def about(request):
    return render(request,'app/about.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'app/index1.html')

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['upassword']
        user = authenticate(username=u,password=p)
        
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {"error":error}
    return render(request,'app/login.html',d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('home')



def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Docter.objects.all()
    return render(request,'app/viewdoctor.html',{'doc':doc})

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    ddoc = Docter.objects.get(id=pid)
    ddoc.delete()
    return redirect('viewdoctor')       

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['aname']
        m = request.POST['amobile']
        asp = request.POST['aspecial']
        try:
            Docter.objects.create(name=n,mobile=m,special=asp)
            error="no"
        except:
            error="yes"
    d = {"error":error}
    return render(request,"app/add_doctor.html",d)

#-----------------------------------------------------------------


def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    return render(request,'app/view_patient.html',{'doc':doc})

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    ddoc = Patient.objects.get(id=pid)
    ddoc.delete()
    return redirect('viewpatient')       

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['aname']
        m = request.POST['amobile']
        agen = request.POST['agender']
        addres = request.POST['aaddress']
        try:
            Patient.objects.create(name=n,mobile=m,gender=agen,address=addres)
            error="no"
        except:
            error="yes"
    d = {"error":error}
    return render(request,"app/add_patient.html",d)


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appointment.objects.all()
    return render(request,'app/view_appointment.html',{'doc':doc})

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    ddoc = Appointment.objects.get(id=pid)
    ddoc.delete()
    return redirect('view_appointment')       

def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Docter.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        n = request.POST['docter']
        m = request.POST['patient']
        da = request.POST['adate']
        at = request.POST['atime']
        doctor2 = Docter.objects.filter(name=n).first()
        patient2 = Patient.objects.filter(name=m).first()
        try:
            Appointment.objects.create(docter=doctor2,patient=patient2,date=da,time=at)
            error="no"
        except:
            error="yes"
    d = {"doctor":doctor1, "patient":patient1,"error":error}
    return render(request,"app/add_appointment.html",d)
