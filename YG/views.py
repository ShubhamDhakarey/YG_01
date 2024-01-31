from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from .models import Category, Card
from django.contrib import messages

# Create your views here.
def index(request):
    category = Category.objects.all()
    card = Card.objects.all()
    # context = {
    #     'card': card,
    #     'category': category
    # }
    return render(request,'index.html',{'card': card, 'category': category})

# user login
def user_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1= StudentUser.objects.get(user=user)
                if user1.type=="student":
                    login(request,user)
                    error="No"
                else:
                    error="Yes"
            except:
                error="Yes"
        else:
            error="Yes"
    d={'error':error}
    return render(request,'user_login.html',d)

# user signup
def user_signup(request):
    error = ""
    if request.method=="POST":
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type="student")
            error="No"
        except:
            error="Yes"
    d={'error':error}
    return render(request,'user_signup.html',d)


#User home page
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method=="POST":
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']
        
        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen
        try:
            
            student.save()
            student.user.save()
            error="No"
        except:
            error="Yes"
        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error="No"
        except:
            pass
    d = {'student':student,"error":error}
    return render(request,'user_home.html',d)

#Logo maker views
def logo_maker(request):
    return render(request,'logo_maker.html')


# Views for business Cards
def business_card(request):
    return render(request,'business_card.html')


#Views for Social
def social(request):
    return render(request,'social.html')


#Views for More
def more(request):
    return render(request,'more.html')

#Views for Cards
def card_desc(request):
    return render(request,'card_desc.html')

#Views for Load more
def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    similar_cards = Card.objects.filter(category=card.category).exclude(pk=card_id)[:3]

    context = {
        'card': card,
        'similar_cards': similar_cards,
    }
    return render(request,'card_detail.html',context)


#Views for Softwares
from django.shortcuts import render
from .models import GraphicSoftware

def make_business_card(request):
    softwares = GraphicSoftware.objects.all()
    return render(request, 'make_business_card.html', {'softwares': softwares})



#Views for feedabck
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully") 
            return redirect(request,'index.html') 
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


