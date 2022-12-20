from django.shortcuts import render
from .models import Department, Doctor
from .forms import BookingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def departments(request):
    dep_name = {
        "depn": Department.objects.all()
    }
    return render(request, 'department.html', dep_name)


def doctors(request):
    dict_doc = {
        'doc': Doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    formdemo=BookingForm()
    dict_form={
        'bookkey':formdemo
    }
    return render(request, 'booking.html',dict_form)

def about(request):
    return render(request, 'about.html')

def cancellation(request):
    return render(request, 'cancellation.html')


def cardiology(request):
    return render(request, 'cardiology.html')



def contactus(request):
    return render(request, 'contactus.html')



def dentalsurgery(request):
    return render(request, 'dentalsurgery.html')


def emergencymedicine(request):
    return render(request, 'emergency medicine.html')


def ent(request):
    return render(request, 'ENT.html')

def generalmedicine(request):
    return render(request, 'generalmedicine.html')


def privacypolicy(request):
    return render(request, 'privacy policy.html')


def refundpolicy(request):
    return render(request, 'refundpolicy.html')



def termsandconditions(request):
    return render(request, 'terms&conditions.html')

def searching(request):
    if request.method =="POST":
        q = request.POST['q']
        doct=Doctor.objects.filter(doc_name__contains=q)
        dpr=Department.objects.filter(dpt_name__contains=q)

        return render(request,'search.html',{'q':q,'doct':doct,'dpr':dpr})
    else:
        return render(request,'search.html',{})
        
    
    

    


