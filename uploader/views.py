from django.shortcuts import render,HttpResponse,HttpResponseRedirect,Http404,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User 
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .models import EbookModel,EbookModel2,EbookModel3,EbookModel4
from .models import User,teacher,student,FeedBack
from .forms import UploadPdf,Feed,uploadpdf2,uploadpdf3,uploadpdf4
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

UserModel=get_user_model()

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            auth_login(request,user)
            
            if user.is_teacher:
                return redirect('/')
            if user.is_student:
                return redirect('/')
            if user.is_superuser:
                return redirect('/')

        else:
            messages.info(request,'invalid user')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        department=request.POST['department']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,"username taken")
                return redirect('register')

            elif User.objects.filter(email=email):
                messages.info(request,"email taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.is_active = False
                user.is_student=True
                user.save()
                stu=student.objects.create(user=user)
                stu.department=department
                stu.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('actmail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                })
                email=EmailMessage(
                    mail_subject,
                    message,
                    'noreply@semicolan.com',
                    [email],
                )
                email.send(fail_silently=False)
                return HttpResponse('please confirm your mail')
        else:
            messages.info(request,"password unmatch")
            return redirect('register')

    else:
        return render(request,'register.html')

def staffregister(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        department=request.POST['department']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,"username taken")
                return redirect('staffregister')

            elif User.objects.filter(email=email):
                messages.info(request,"email taken")
                return redirect('staffregister')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.is_active = False
                user.is_teacher=True
                user.is_staff=True
                user.save()
                tch=teacher.objects.create(user=user)
                tch.department=department
                tch.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('staff_actmail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                })
                mail='ajaymkumar172@gmail.com'
                email=EmailMessage(
                    mail_subject,
                    message,
                    'noreply@semicolan.com',
                    [mail],
                )
                email.send(fail_silently=False)
                return HttpResponse('please wait until HoD confirm your mail')
        else:
            messages.info(request,"password unmatch")
            return redirect('staffregister')

    else:
        return render(request,'staffregister.html')



def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def pdfview(request):
    return render(request,'home.html')


def pdfdisplay(request):
    pdf = EbookModel.objects.all()
    if request.method=='POST':
        forms=UploadPdf(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()


    else:
        forms=UploadPdf()

    context ={
    'frm':forms,
    'pdf':pdf
    }
    return render(request,'pdfdisplay.html',context)

def pdfdisplay2(request):
    pdf = EbookModel2.objects.all()
    if request.method=='POST':
        forms=uploadpdf2(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()


    else:
        forms=uploadpdf2()

    context ={
    'frm2':forms,
    'pdf2':pdf
    }
    return render(request,'pdfdisplay2.html',context)


def pdfdisplay3(request):
    pdf = EbookModel3.objects.all()
    if request.method=='POST':
        forms=uploadpdf3(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()


    else:
        forms=uploadpdf3()

    context ={
    'frm3':forms,
    'pdf3':pdf
    }
    return render(request,'pdfdisplay3.html',context)


def pdfdisplay4(request):
    pdf = EbookModel4.objects.all()
    if request.method=='POST':
        forms=uploadpdf4(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()


    else:
        forms=uploadpdf4()

    context ={
    'frm4':forms,
    'pdf4':pdf
    }
    return render(request,'pdfdisplay4.html',context)



def feedback(request):
    
    
    if request.method=='POST':
        fbs=FeedBack.objects.create()
        fbs.name=request.POST['name']
        fbs.feedback=request.POST['feedback']
        fbs.username=request.POST['username']
        fbs.save()
     
        messages.success(request,'your feedback has taken')
        return redirect('feedback')



    else:
        fb=FeedBack.objects.all()
        context={
        'fb':fb
        }


    return render(request,'feedback.html',context)
def logout(request):
    auth.logout(request)
    return redirect('login')



 
    