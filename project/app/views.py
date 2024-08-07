from django.shortcuts import render,redirect
from .models import RegData
from .models import Enquiry
from .models import AdminReg

# Create your views here.
def home(request):
    return render(request,'app/display.html')

def login(request):
    return render(request,'app/login.html')

def register(request):
    return render(request,'app/registration.html')

def UserRegister(request):
    if request.method == "POST":
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        cpass= request.POST['cpass']
 # validate user alreday exsist 
        User = RegData.objects.filter(email=email)
        if User:
            message = "user alreday exist"
            return render(request,'app/registration.html',{'msg':message})
        else:
           if password == cpass:
            newuser = RegData.objects.create(name=name,lname=lname,password=password,email=email,contact=contact)
            message = "user register successfully"
            return render(request,'app/login.html',{'msg':message})
           else:
            message="password doesn't match"
            return render(request,'app/registration.html',{'msg':message})
    else:
     return render(request,'app/registration.html')

def UserLogin(request):
    if request.method == "POST":
      email=request.POST['email'] 
      password=request.POST['password']  
      #checking the emailid with database
      User = RegData.objects.get(email=email)  
      if User:
         id = User.id
         context= {
             'id':id,
         }  
         if User.password == password:
           name = User.name,
           lname = User.lname,
           email = User.email,
           contact= User.contact,
           password = User.password,
           data = {
             'name':User.name,
             'lname': User.lname,
             'email':User.email,
             'contact':User.contact,
             'password':User.password,  
          }
           return render(request,'app/dashboard.html',{'data':data ,'con':context})    
         else:
            message="password does not match"
            return render(request,'app/login.html',{'msg':message})
    else:
        message = "user does not exsist"
        return render(request,'app/registration.html',{'msg':message})

def userquery(request):
    if request.method == "POST":
       name = request.POST['name']
    #    print(name)
       lname = request.POST['lname']
    #    print(lname)
       contact = request.POST['contact']
    #    print(contact)
       email = request.POST['email']
    #    print(email)
       password = request.POST['password']
       id = request.POST['id']
       data = {
             'id':id,
             'name':name,
             'lname': lname,
             'email':email,
             'contact':contact, 
             'password':password,
          }
       return render(request,'app/enquiry.html',{'data':data})  

def insertquery(request):
    if request.method == 'POST':
       name=request.POST['name']
       lname=request.POST['lname']
       email=request.POST['email']
       contact=request.POST['contact']
       enquiry=request.POST['enquiry']
       password= request.POST['password']
       newuser = Enquiry.objects.create(name=name,lname=lname,email=email,contact=contact,enquiry=enquiry,password=password,)
       print(newuser)
       Data = {
             'name':name,
             'lname':lname,
             'email':email,
             'contact':contact,
            #  'enquiry':enquiry,
             'password':password,
          }
       return render(request,'app/dashboard.html',{'Data':Data})

def showquery(request):
    print(request.POST)
    if request.method == 'POST':
       name = request.POST['name']
       lname = request.POST['lname']
       email = request.POST['email']
       contact = request.POST['contact']
       password = request.POST['password']
       data1 = Enquiry.objects.filter(email = email)
       print(data1)
       return render(request,'app/showquery.html',{'user':data1})

def editPage(request,pk):
#fetching the data of perticular ID
 get_data=Enquiry.objects.get(id=pk)
 return render(request,'app/edit.html',{'key2':get_data})

def updateData(request,pk):
#  print(request.POST)
 udata=Enquiry.objects.get(id=pk)
 udata.name=request.POST['name']
 udata.lname=request.POST['lname']
 udata.email=request.POST['email']
 udata.contact=request.POST['contact']
 udata.password=request.POST['password']
 udata.enquiry=request.POST['enquiry']
 email=udata.email
 udata.save()
#  return redirect('showquery')
 user=Enquiry.objects.filter(email=email)
 print(user)
 return render(request,'app/showquery.html',{'user':user})

def deleteData(request,pk):
 ddata=Enquiry.objects.get(id=pk)
 email=ddata.email
#Query for delete
 ddata.delete()
 user=Enquiry.objects.filter(email=email)
 return render (request,'app/showquery.html',{'user':user})

def logout(request):
   return render(request,'app/display.html')


#======================= admin views function==================================# 

def adreg(request):
   return render(request, 'app/adreg.html')

def adlog(request):
   return render(request, 'app/adlog.html')

#============================= admin reg login match====================

def AdminRegister(request):
    if request.method == "POST":
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        cpass= request.POST['cpass']
 # validate user alreday exsist 
        User = AdminReg.objects.filter(email=email)
        if User:
            message = "user alreday exist"
            return render(request,'app/adreg.html',{'msg':message})
        else:
           if password == cpass:
            newuser = AdminReg.objects.create(name=name,lname=lname,password=password,email=email,contact=contact)
            message = "user register successfully"
            return render(request,'app/adlog.html',{'msg':message})
           else:
            message="password doesn't match"
            return render(request,'app/adreg.html',{'msg':message})
    else:
     return render(request,'app/adreg.html')

def AdminLogin(request):
    if request.method == "POST":
      email=request.POST['email'] 
      password=request.POST['password']  
      #checking the emailid with database
      User = AdminReg.objects.get(email=email)
      # if not User:
      #    
      if User:
        if User.password == password:
          name = User.name,
          lname = User.lname,
          email = User.email,
          contact= User.contact,
          password = User.password,
          data = {
             'name':User.name,
             'lname': User.lname,
             'email':User.email,
             'contact':User.contact,
             'password':User.password,  
          }
          return render(request,'app/Admindashboard.html',{'data':data})    
        else:
            message="password does not match"
            return render(request,'app/adlog.html',{'msg':message})
      else:
        message = "user does not exsist"
        return render(request,'app/adreg.html',{'msg':message})



def adminlogout(request):
   return render(request,'app/display.html')

def AdminQuery(request):
      data0 = Enquiry.objects.all()
      print( print("SQL Query :", data0.query))
      return render(request,'app/AdminQuery.html',{'data0':data0})    
         


   
   


