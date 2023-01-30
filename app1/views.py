from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import RegisterForm,ImageUploadForm,LoginForm,UpdateForm,ChangePasswordForm
from . models import Register,Image
from django.contrib.auth import logout as logouts

# Create your views here.
def index(request):
    name="adarsh"
    return render(request,'index.html',{'data':name})

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'user already exists')
                return redirect('/register')
            
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/register')
            else:
                tab=Register(Name=name,Age=age,Place=place,Email=email,Photo=photo,Password=password)
                tab.save()
                messages.success(request,'successfull')
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})


def uploadimage(request):
    if request.method=='POST':
        form=ImageUploadForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Upload Successfully')
            return redirect('/')
    else:
        form=ImageUploadForm
    return render(request,'uploadimage.html',{'form':form})                                                                         

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register.objects.get(Email=email)
                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/login')
                else:
                    messages.success(request,'successfull')
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'email or passsword incorrect')
                return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated Successfully')
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form})

def changepassword(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if  form.is_valid():
            old=form.cleaned_data['OldPassword']
            new=form.cleaned_data['NewPassword']
            confirm=form.cleaned_data['ConfirmPassword']
            if old != user.Password:
                messages.warning(request,'Not oldpassword')
                return redirect('/changepassword/%s' %user.id)
            elif old==new:
                messages.warning(request,'same password')
                return redirect('/changepassword/%s' % user.id)
            elif new != confirm:
                messages.warning(request,'new and confirm passwords doesnot match')
                return redirect('/changepassword/%s' % user.id)
            else:
                user.Password=new
                user.save()
                messages.success(request,'changed succesfully')
                return redirect('/home/%s' % user.id)

    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user})

def logout(request):
    logouts(request)
    messages.success(request,'logout successfully')
    return redirect('/')

def showimage(request):
    image=Image.objects.all()
    return render(request,'gallery.html',{'image':image})

def detail(request,id):
    image=Image.objects.get(id=id)
    return render(request,'detail.html',{'image':image})
