from django.shortcuts import render,HttpResponse, redirect
import requests
from locations.models import *
from accounts.models import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from locations.models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth import logout


def user_login(request):
    return render(request,'login.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        email = email.lower()
        email_exits = None
        try:
            email_exist = CustomUser.objects.get(email=email)
            if email_exist is not None:
                messages.error(request, 'Account already exist!')
                return redirect('register')
        except:
            password = request.POST.get('password')
            phone_number = request.POST.get('phone_number')
            type_user = request.POST.get('type_user')
            address = request.POST.get('address')
            areas = request.POST.get('area')
            state_id = request.POST.get('state')
            print("----------------------------",state_id)
            district_id = request.POST.get('districts')
            print(district_id)
            state = state_master.objects.get(state_id=state_id)
            district = district_master.objects.get(district_id=district_id)
            user = CustomUser.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone_number = phone_number, 
                role = type_user,
                address = address,
                state = state,
                district = district,
                is_staff = False,
                is_superuser = False
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'Account created successfully!', extra_tags='success')

            return redirect('login')
    else:
        states =state_master.objects.all()
        return render(request,'register.html',{'states':states})
    
def user_login(request):
    if request.method == 'POST':
        context = {'Login_status': ''}

        # get the username and password from the POST request
        email1 = request.POST.get('email')
        email1 = email1.lower()
        password1 = request.POST.get('password')
        print(email1)
        print(password1)
        user = None
        try:
            user = CustomUser.objects.get(email__iexact=email1)
        except:
            print("user not exist")

        if user is not None:
            print("fetching")
            authenticate_user = authenticate(request, email=email1, password=password1)

            if authenticate_user is not None:
                login(request, authenticate_user)
                if authenticate_user.role == "FARMER":
                     context = {
                         'user': "FARMER",
                     }
                     return render(request,'logout.html',context)
                else:
                    context = {
                         'user': "Owner",
                     }
                    return render(request,'logout.html',context)
                
            else:
                print("something went wrong")
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def get_districts(request):
    state_name = request.GET.get('complainant_state') 
    state_object = state_master.objects.get(state_id=int(state_name))
    districts_objects = district_master.objects.filter(state_name=state_object.state_name)
    districts = list(districts_objects.values('district_id', 'district_name'))
    print(districts)
    return JsonResponse({'districts': districts})


def landing_page(request):
    return render(request, 'index.html')


def grid_shop(request):
    return render(request, 'grid_shop.html')



def logout_view(request):
    logout(request)
    return redirect('landing_page')


def single_product(request):
    return render(request, 'single_product.html')