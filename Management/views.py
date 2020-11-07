import requests, json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Data, Location, Appointment, Hospital, Slot, Doctor, Volunteer, Phone
from types import SimpleNamespace
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
# Create your views here.

def index(request):
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    covidData = []
    for data in response.json():
        covidData.append(data)
    context = {
        "locations" : Location.objects.all(),
        "covidData" : covidData
    }
    return render(request, 'pages/index.html', context)


def loadHospitals(request):
    location = request.POST['area']
    local = Location.objects.get(pk=location)
    hospitals = []
    for h in Data.objects.filter(area=local):
        hospitals.append(h)
    context = {
        "hospitals" : hospitals
    }
    return render(request, 'pages/hospitals.html', context)



def loadData(request):
    state = request.POST['state']
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    
    districts = []
    for d in response.json()[state]['districtData']:
        districts.append(d)

    active = []
    deceased = []
    recovered = []
    for d in districts:
        active.append(response.json()[state]['districtData'][d]['active'])
    for d in districts:
        deceased.append(response.json()[state]['districtData'][d]['deceased'])        
    for d in districts:
        recovered.append(response.json()[state]['districtData'][d]['recovered'])

    context = {
        "dist": districts,
        "active": active,
        "dead": deceased,
        "rec": recovered
    }
    
    return render(request, "pages/loadData.html", context)

def login_view(request):
    if request.user.is_authenticated:
        hosp = []
        app = []
        for h in Hospital.objects.all():
            hosp.append(h)
        for a in Appointment.objects.filter(patient=request.user):
            app.append(a)
        context = {
                "name" : request.user.first_name + ' ' + request.user.last_name,
                "hospitals": hosp,
                "appointments": app
            }
        return render(request, "pages/welcome.html", context)
    else:
        if 'hospLog' in request.session:
            return redirect(login_hosp)
        elif 'volLog' in request.session:
            return redirect(login_vol)
        else:
            return render(request, "pages/login.html")

def signIn(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    elif 'hospLog' in request.session:
        return redirect(login_hosp)
    else:
        email = request.POST['emailLog']
        password = request.POST['pwd1']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(login_view)
        else:
            return render(request, "pages/login.html", context={"error": "Incorrect Details!"})

def register(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    else:
        if 'hospLog' in request.session:
            return redirect(login_hosp)
        else:
            return render(request, "pages/register.html")

def signUpUser(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    else:
        if 'hospLog' in request.session:
            return redirect(login_hosp)
        else:
            fname = request.POST['fnameReg1']
            lname = request.POST['lnameReg1']
            email = request.POST['emailReg1']
            phone = request.POST['phoneReg1']
            password = request.POST['pwdReg1']
            user = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email, password=password)
            phone = Phone.objects.create(user=user, phone=phone)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(login_view)
            else:
                return HttpResponse("Error in creating the account!")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        if not request.user.is_authenticated:
            return redirect(login_view)
    elif 'hospLog' in request.session:
        return redirect(logout_hosp)
    else:
        return render(request, "pages/login.html", context={"error": "User not logged in!"})

def signUpHospital(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    elif 'hospLog' in request.session:
        return redirect(login_hosp)
    else:
        count = 0
        for h in Hospital.objects.all():
            count += 1
        hp = count+1
        hID = 'NCR' + str(hp)
        #print(hID)
        name = request.POST.get('hospName')
        address = request.POST.get('hospAddress')
        phone = request.POST.get('hospPhone')
        password = request.POST.get('pwdReg2')
        if Hospital.objects.create( hID=hID, name=name, address=address, contact=phone, password=password):
            request.session['hospLog'] = hID
            print("reached")
            return redirect(login_hosp)
        else:
            return HttpResponse("Cannot register hospital")

def login_hosp(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    elif 'volLog' in request.session:
        return redirect(login_vol)
    else:
        slots = []
        doctors = []
        app = []
        if 'hospLog' in request.session:
            if request.session['hospLog']:
                for h in Hospital.objects.all():
                    if h.hID == request.session['hospLog']:
                        for s in Slot.objects.filter(hospital=h):
                            slots.append(s)
                        for d in Doctor.objects.filter(hospital=h):
                            doctors.append(d)  
                        for a in Appointment.objects.filter(hospital=h):
                            app.append(a)
                        context = {
                            "name": h,
                            "hid": h.hID,
                            "slots": slots,
                            "doctors": doctors,
                            "appointments": app
                        }
                return render(request, "pages/hospfunction.html", context)
            else:
                return redirect(logout_hosp)
        else:
            slots = []
            doctors = []
            app = []
            hID = request.POST.get('hospID')
            password = request.POST.get('pwd2')
            for h in Hospital.objects.all():
                if h.hID == hID and h.password == password:    
                    request.session['hospLog'] = hID     
                    for s in Slot.objects.filter(hospital=h):
                        slots.append(s)        
                    for d in Doctor.objects.filter(hospital=h):
                        doctors.append(d) 
                    for a in Appointment.objects.filter(hospital=h):
                            app.append(a) 
                    context  = {
                        "name": h,
                        "hid": hID,
                        "slots": slots,
                        "doctors": doctors,
                        "appointments": app
                         }
                    return render(request, "pages/hospfunction.html", context)
                
            return HttpResponse("Invalid Credentials")


def logout_hosp(request):
    if 'hospLog' in request.session:
        del request.session['hospLog']
        return redirect(login_view)
    else:
        return render(request, "pages/login.html", context={"error": "Hospital ID Not Logged In!"})


def addSlot(request):
    if 'hospLog' in request.session:
        hID = request.POST.get('hospitalID')
        h = Hospital.objects.get(hID=hID)
        time1 = request.POST.get('Timing1')
        max1 = request.POST.get('bookTiming1')
        time2 = request.POST.get('Timing2')
        max2 = request.POST.get('bookTiming2')
        time3 = request.POST.get('Timing3')
        max3 = request.POST.get('bookTiming3')
        
        if Slot.objects.create(hospital=h, timing1=time1, max_appointments1=max1, timing2=time2, max_appointments2=max2, timing3=time3, max_appointments3=max3, book1=0, book2=0, book3=0):
            return redirect(login_hosp)
        else:
            return HttpResponse("Cannot create slot!")

    else:
        return redirect(login_hosp)

def slotDel(request):
    if 'hospLog' in request.session:
        sID = request.POST.get('slotID')
        s = Slot.objects.get(pk=sID)
        s.delete()
        return redirect(login_hosp)
    else:
        return redirect(login_hosp)

def addDoc(request):
    if 'hospLog' in request.session:    
        name = request.POST.get('name')
        spec = request.POST.get('spec')
        hId = request.POST.get('hospitalID')
        h = Hospital.objects.get(hID=hId)
        slot = request.POST.get('slot')
        s = Slot.objects.get(pk=slot)
        fees = request.POST.get('fees')
        if Doctor.objects.create(doctor=name, hospital=h, spec=spec, slot=s, fees=fees):
            return redirect(login_hosp)
        else:
            return HttpResponse("Cannot add doctor.")
    else:
        return redirect(login_hosp)

def delDoc(request):
    if 'hospLog' in request.session:
        dID = request.POST.get('docID')
        d = Doctor.objects.get(pk=dID)
        d.delete()
        return redirect(login_hosp)
    else:
        return redirect(login_hosp)

def loadHosp(request):
    if request.user.is_authenticated:
        hosp = request.POST.get('hosp')
        h = Hospital.objects.get(pk=hosp)
        doc = []
        for d in Doctor.objects.filter(hospital=h):
            doc.append(d)
        context = {
            "doctors": doc,
            "hosp": hosp
        }
        return render(request, "pages/bookApp1.html", context)
    else:
        return redirect(login_view)

def loadDoc(request):
    if request.user.is_authenticated:
        slot = []
        hosp = request.POST.get('hosp')
        doc = request.POST.get('doc')
        d = Doctor.objects.get(pk=doc)
        for s in Slot.objects.all():
            if s == d.slot:
                if s.book1 < s.max_appointments1:
                    slot.append(s.timing1)
                if s.book2 < s.max_appointments2:
                    slot.append(s.timing2)
                if s.book3 < s.max_appointments3:
                    slot.append(s.timing3)
                if slot:
                    context = {
                        "doc": doc,
                        "slots": slot,
                        "hosp": hosp,
                        "sID": s.id
                    }
                else:
                    return HttpResponse("Daily Appointments Limit Reached!")
                return render(request, "pages/bookApp2.html", context)
    else:
        return redirect(login_view)

def bookSlot(request):
    if request.user.is_authenticated:
        hosp = request.POST.get('hosp')
        h = Hospital.objects.get(pk=hosp)
        doc = request.POST.get('doc')
        d = Doctor.objects.get(pk=doc)
        sID = request.POST.get('sid')
        s = Slot.objects.get(pk=sID)
        timing = request.POST.get('slot')
        if s.timing1 == timing:
            s.book1 += 1
        elif s.timing2 == timing:
            s.book2 += 1
        elif s.timing3 == timing:
            s.book3 += 1
        if Appointment.objects.create(patient=request.user, doc=d, hospital=h, slot=s, confirmation='Yes', timings=timing):
            hosp = []
            app = []
            for h in Hospital.objects.all():
                hosp.append(h)
            for a in Appointment.objects.filter(patient=request.user):
                app.append(a)
            context = {
                    "name" : request.user.first_name + ' ' + request.user.last_name,
                    "hospitals": hosp,
                    "appointments": app,
                    "success": "Successfully booked appointment!"
                }
            return render(request, "pages/welcome.html", context)
        else:
            return HttpResponse("Cannot book an appointment!")
    else:
        return redirect(login_view)

def compApp(request):
    if 'hospLog' in request.session:
        aId = request.POST.get('aid')
        print(aId)
        a = Appointment.objects.get(pk=aId)
        if a:
            print(a)
            a.complete = True
            a.save()
            return redirect(login_hosp)
        else:
            return HttpResponse("Could not find the appointment!")
    else:
        return redirect(login_view)

def signUpVol(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    elif 'hospLog' in request.session:
        return redirect(login_hosp)
    else:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        org = request.POST.get("org")
        contact = request.POST.get("volPhone")
        pwd = request.POST.get("pwd")
        v = Volunteer.objects.create(first=fname, last=lname, organization=org, contact=contact, password=pwd)
        if v:
            request.session['volLog'] = v.id
            return redirect(login_vol)
        else:
            return HttpResponse("Cannot Create Volunteer Account!")

def login_vol(request):
    if request.user.is_authenticated:
        return redirect(login_view)
    elif 'hospLog' in request.session:
        return redirect(login_hosp)
    elif 'volLog' in request.session:
        context = {
            "volunteer": Volunteer.objects.get(pk=request.session['volLog'])
        }
        return render(request, "pages/volunteer.html", context)
    else:
        vid = request.POST.get('vID')
        pwd = request.POST.get('pwd')
        v = Volunteer.objects.get(pk=vid)
        if v:
            if v.password == pwd:
                request.session['volLog'] = vid
                context = {
                "volunteer": v
                }
                return render(request, "pages/volunteer.html", context)
            else:
                return HttpResponse("Invalid Password!")
        else: 
            return HttpResponse("Invalid Credentials!")
    
    return redirect(login)

def logout_vol(request):
    if 'volLog' in request.session:
        del request.session['volLog']
        return redirect(login_view)
    else:
        return redirect(login_view)


now = datetime.datetime.now()

newday = now.replace(hour=23, minute=59, second=59, microsecond=0)

if now == newday:
    for s in Slot.objects.all():
        s.book1 = s.book2 = s.book3 = 0 
    for a in Appointment.objects.all():
        a.delete()

print(now)