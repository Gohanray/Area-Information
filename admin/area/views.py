from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'areainfo.html')

def calculate(request):
    name=str(request.GET["nm"])
    area=int(request.GET["area"])
    units=str(request.GET["units"])
    risk=str(request.GET["risk"])

    sing_cir_area=3.14159
    if units=='sq_feet':
        area=area*(0.0929)
    if units=='sq_km':
        area=area*(1000*1000)

    c_capacity = area//sing_cir_area
        
    reducer=0.1
    if risk=='medium':
        reducer=0.2
    if risk=='high':
        reducer=0.5

    res=int(c_capacity-c_capacity*reducer) 
    print("unit",res)   
    return render(request, 'result.html',{'result':res},content_type='text/html')    
