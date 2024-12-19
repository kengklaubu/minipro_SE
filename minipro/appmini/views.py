from django.shortcuts import render

# Create your views here.
def homepage(request):
    bikes = Bike.objects.all()
    return render(request, "homepage.html",{"bikes": bikes})


from .models import Bike
def bike_list(request):
    bikes = Bike.objects.all()  # ดึงข้อมูลจักรยานทั้งหมด
    return render(request, "bike_list.html", {"bikes": bikes})
