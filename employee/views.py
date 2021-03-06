from django.shortcuts import render
from employee.models import *
from employee.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CompanyDetailsApiView(APIView):

    def get(self,request,pk):
        all_company = Company.objects.all()
        print(all_company)
        if all_company:
            company_serializers = CompanySerializers(all_company, many=True)
            return Response(company_serializers.data)
        else:
            return Response(company_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,pk):
        company_serializers = CompanySerializers(data=request.data)
        if company_serializers.is_valid():
            company_serializers.save()
            return Response(company_serializers.data, status=status.HTTP_201_CREATED)
        else:

            return Response(company_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        company_id = Company.objects.get(pk=pk)
        company_serializers = CompanySerializers(company_id,data=request.data)
        if company_serializers.is_valid():
            company_serializers.save()
            return Response(company_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(company_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        company_id = Company.objects.get(pk=pk)
        company_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DepartmentDetailsApiView(APIView):

    def get(self,request,pk):
        all_department = Department.objects.all()

        if all_department:
            department_serializers = DepartmentSerializers(all_department, many=True)
            return Response(department_serializers.data)
        else:
            return Response(department_serializers.errors, status=status.HTTP_400_BAD_REQUEST),


    def post(self,request,pk):
        department_serializers = DepartmentSerializers(data=request.data)
        if department_serializers.is_valid():
            department_serializers.save()
            return Response(department_serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(department_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk):
        department_id = Department.objects.get(pk=pk)
        department_serializers = DepartmentSerializers(department_id,data=request.data)
        if department_serializers.is_valid():
            return Response(department_serializers.data, status=status.HTTP_200_OK)            
        else:
            return Response(department_serializers.errors, status=status.HTTP_400_BAD_REQUEST )

    
    def delete(self,request,pk):
        department_id = Department.objects.get(pk=pk)
        department_id.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
