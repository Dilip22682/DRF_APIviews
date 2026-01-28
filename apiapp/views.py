from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from .models import student
from .serializer import studentSerializer
from rest_framework.decorators import api_view
from rest_framework .views import APIView
from rest_framework import status


# Create your views here.
# @api_view(['GET'])
def home(request):
    return JsonResponse({'msg':'hello world'})

class studentDetails(APIView):
    def get(self,request,pk=None,formate=None):
        id=pk
        if id is not None:
            stu=student.objects.get(id=id)
            serializer=studentSerializer(stu)
            return Response(serializer.data)
        stu=student.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,formate=None):
        # obj=request.body
        serializer=studentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,formate=None):
        id=pk
        if id is not None:
            stu=student.objects.get(id=id)
            print("request:",request.data)
            serializer=studentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updatad '},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None,formate=None):
        id=pk
        if id is not None:
            stu=student.objects.get(id=id)
            serializer=studentSerializer(stu,data=request.data,partial=True)
            # print("obj:",obj)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated (patch) !!'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk=None,formate=None):
        id=pk
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data is deleted '})
        