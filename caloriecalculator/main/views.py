from django.shortcuts import render

# Create your views here.

def home(request):
   
    return render(request,"index.html")

def calculations(request):
    if request.method=='POST':
        goal=request.POST.get('Goal')
        age=request.POST.get('age')
        heights=request.POST.get('height')
        weight=request.POST.get('weight')
        sex=request.POST.get("sex")
        Activity=request.POST.get("activity")
        calorie=0
        
        
    if sex=='male' and goal!='-20':
        calorie+=(10*int(weight)+6.5*int(heights)-5*int(age)+5)*float(Activity)
        surplus_calorie=(calorie*(int(goal)/100))
        required_calorie=calorie+surplus_calorie                      

    else:
        calorie+=(int(weight)*10+6.5*int(heights)-5*int(age)-161)*float(Activity)
        required_calorie=calorie                         
                          

    return render(request,'result.html',{'req_calorie':round(required_calorie)})