from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime 

class goodmorningview(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data='hello good mornng')
    



class goodeveningview(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data='hello good evening')
    
class todayview(APIView):
    def get(self,request,*args,**kwargs):
        time_now=datetime.now()
        return Response(data=time_now)

class addview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        a=request.data.get('num1')
        b=request.data.get('num2')
        c=int(a)+int(b)
        return Response(data=c)

class substractview(APIView):
        def post(self,request,*args,**kwargs):
            print(request.data)
            a=request.data.get('num1')
            b=request.data.get('num2')
            if a>b:
               c=int(a)-int(b)
            else:
               c=int(b)-int(a)

            return Response(data=c)
    
class cubeview(APIView):
    def post(self,request,*args,**kwargs):
    
        a=int(request.data.get('num1'))
        c=a**2
        return Response(data=c)
