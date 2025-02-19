from django.http import HttpResponse
from django.shortcuts import render, redirect
from db.models import Register
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
import logging


# Set up a logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request,"home.html")

def chat(request):
    return render(request,"chatbot.html")

def quiz(request):
    return render(request,"quiz.html")

def login(request):
	return render(request,"login.html")

# def loginafter(request):
# 	email = (request.POST["email"])
# 	password = (request.POST["password"])
    
# 	showdata = Register.objects.get(email = email, password = password )
# 	display={
# 	'showdata':showdata
# 	}
# 	return render(request,"home.html",display)

def loginafter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            register = Register.objects.get(email=email)
        except Register.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        # Check the password
        if check_password(password, register.password):
            request.session['user_id'] = register.id  # Store user ID in session
            request.session['user_name'] = register.name  # Store user name
            messages.success(request, "Login successful!")  # Success message
            return redirect('/dashboard/')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')



def signup(request):
	return render(request,"signup.html")

# def signupafter(request):
# 	name = (request.POST["name"])
# 	email =  (request.POST["email"])
# 	password = int (request.POST["password"])
# 	res = Register( name = name, email = email, password = password)
# 	res.save()
# 	return HttpResponseRedirect("/login/")

# def signupafter(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if email already exists
#         if Register.objects.filter(email=email).exists():
#             return render(request, 'signup.html', {'error': 'Email already exists'})

#         # Save the user
#         hashed_password = make_password(password)  # Hash the password
#         register = Register(name=name, email=email, password=hashed_password)
#         register.save()

#         return render(request, 'signup.html', {'success': 'User signed up successfully'})

#     return render(request, 'signup.html')

def signupafter(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if Register.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        # Save the user
        hashed_password = make_password(password)  # Hash the password
        register = Register(name=name, email=email, password=hashed_password)
        register.save()

        # Send a welcome email to the user
        subject = 'Welcome to Our Platform'
        message = f"""Hi {name},

        Thank you for signing up on our platform! We're thrilled to have you on board.  
        Please verify your email by clicking the link below:

        [Verification Link]

        If you didn't sign up, please ignore this email."""
        from_email = settings.EMAIL_HOST_USER  # Get your email from settings
        recipient_list = [email]  # Recipient's email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return render(request, 'signup.html', {'success': 'User signed up successfully. A confirmation email has been sent.'})
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return render(request, 'signup.html', {'error': f'User signed up, but email could not be sent. Error: {str(e)}'})

    return render(request, 'signup.html')

def dashboard(request):
    if 'user_id' in request.session:
        return render(request, 'dashboard.html', {'user_name': request.session.get('user_name')})
    else:
        return redirect('/login/')  # Redirect to login if not logged in


def logout(request):
    request.session.flush()  # Clear session
    return redirect('/login/')  # Redirect to login after logout

