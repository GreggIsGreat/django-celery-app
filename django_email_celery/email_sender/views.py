from django.http import HttpResponse
from django.shortcuts import render
from .tasks import go_to_sleep, add
from .tasks import go_to_sleep, send_email_task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee_database
from .serializers import employee_databaseSerializer


# Create your views here.


def index(request):
    return render(request, 'email_sender/index.html')


def prgbar(request):
    task = go_to_sleep.delay(1)
    return render(request, 'email_sender/prgbar.html',{'task_id' : task.task_id})


def emailtin(request):
    add.delay(2, 2)
    send_email_task.delay()
    return render(request, 'email_sender/emailtin.html')


# class employeedata(APIView):
#
#     def get(self, request):
#         employ = employee_database.objects.all()
#         serializer = employee_databaseSerializer(employ, many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass


# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic import View
#
# from .tasks import go_to_sleep, add
# from .tasks import go_to_sleep, send_email_task
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import employee_database
# from .serializers import employee_databaseSerializer
# from django.views.generic import TemplateView
#
# # Create your views here.
#
#
# # def index(request):
# #     return render(request, 'email_sender/index.html')
#
#
# class index(View):
#     template_name = "email_sender/index.html"
#
#
# class prgbar(View):
#     task = go_to_sleep.delay(1)
#     two = {'task_id': task.task_id}
#     template_name = "email_sender/prgbar.html"
#
#
# class emailtin(TemplateView):
#     add.delay(2, 2)
#     send_email_task.delay()
#     template_name = 'email_sender/emailtin.html'
#
#
# # class employeedata(APIView):
# #
# #     def get(self, request):
# #         employ = employee_database.objects.all()
# #         serializer = employee_databaseSerializer(employ, many=True)
# #         return Response(serializer.data)
# #
# #     def post(self):
# #         pass
