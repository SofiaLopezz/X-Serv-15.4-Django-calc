from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def suma (request, num1, num2):

	sum = int(num1) + int(num2)

	return HttpResponse ("El resultado de " + str(num1) + " + " + str(num2) + " es " + str(sum))

def resta (request, num1, num2):

	rest =  int(num1) - int(num2)

	return HttpResponse ("El resultado es " + str(num1) + " - " + str(num2) + " es " + str(rest))

def multiplicacion (request, num1, num2):

	mult =  int(num1) * int(num2)

	return HttpResponse ("El resultado es " + str(num1) + " * " + str(num2) + " es " + str(mult))

def division (request, num1, num2):
	
	try:
		div =  int(num1) / int(num2)
		return HttpResponse ("El resultado es " + str(num1) + " / " + str(num2) + " es " + str(div))
	except:
		return HttpResponse ("No es posible dividir entre 0, introduzca otro valor")