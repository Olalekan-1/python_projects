from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
""" def hello():
    return print("Hello, It si good to learn the Djano")
    # print("you will be fine learning this Man!")
 """
def say_hello(request):
    # l = "Welcome to the World of Django"
    return render(request, "index.html  ")