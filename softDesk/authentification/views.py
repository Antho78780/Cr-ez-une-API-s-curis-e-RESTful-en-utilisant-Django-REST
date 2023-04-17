from django.shortcuts import HttpResponse
from authentification.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

@csrf_exempt
def signup(request):
    if request.method == "POST":
       print(request.POST)
       username = request.POST["username"]
       first_name = request.POST["first_name"]
       last_name = request.POST["last_name"]
       email = request.POST["email"]
       password = make_password(request.POST["password"])
       
       user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

       return HttpResponse(f"Utilisateur créer: {user}")

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        return HttpResponse("my reponse")