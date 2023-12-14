from django.shortcuts import render
import csv
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *



class CSVFile(APIView):
    
    def get(self,request):
                  
        return Response({"status": 200,
            "message": "this is msg"})

    def post(self,request):
        file=request.FILES['csvfile']
        
        file_path = 'csvApi/file.csv'
        with open(file_path, 'wb') as f:
            f.write(file.read())

        with open(file_path, 'r') as f:
            
            reader = csv.DictReader(f)

            
            for row in reader:
                Question.objects.create(
                    question_title = row.get("question_title"),
                    question_description = row.get("question_description"),
                    question_constrants = row.get("question_constrants"),
                    question_testcases_input = row.get("question_testcases_input"),
                    question_testcases_output = row.get("question_testcases_output")
                )
            
        return Response({"status": 200,"message": "this is a msg"})