from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()
    return render(request, "std/home.html", {'std':std})

def std_add(request):
    if request.method=='POST':
        print("Added")
        stds_event=request.POST.get("std_event")
        stds_date=request.POST.get("std_date")
        stds_time=request.POST.get("std_time")
        stds_description=request.POST.get("std_description")
        stds_contact=request.POST.get("std_contact")

        s=Student()
        s.event=stds_event
        s.date=stds_date
        s.time=stds_time
        s.description=stds_description
        s.contact=stds_contact

        s.save()

        return redirect("/std/home")
        
    return render(request, "std/add_std.html", {})
def delete_std(request, event):
    s=Student.objects.get(pk=event)
    s.delete()

    return redirect("/std/home")

def update_std(request, event):
    std=Student.objects.get(pk=event)
    return render(request, "std/update_std.html", {'std':std})

def do_update_std(request, event):
    stds_event=request.POST.get("std_event")
    stds_date=request.POST.get("std_date")
    stds_time=request.POST.get("std_time")
    stds_description=request.POST.get("std_description")
    stds_contact=request.POST.get("std_contact")
    std=Student.objects.get(pk=event)
    std.event=stds_event
    std.date=stds_date
    std.time=stds_time
    std.description=stds_description
    std.contact=stds_contact
    std.save()
    return redirect("/std/home")