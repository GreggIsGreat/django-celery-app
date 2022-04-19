from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder
# from django_email_celery.Rest_API.models import checkfilestatus
from celery import shared_task, Celery
from django.core.mail import send_mail
import requests

app = Celery()

# from django.core.mail import send_mail


# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(10):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 10, f'On iteration{i}')
    return 'Good'


@shared_task()
def add(x, y):
    return x + y


@shared_task()
def send_email_task():
    send_mail('Celery Task Works',
              'This is proof the task is still running',
              'rttteddy@gmail.com', ['rttteddy@gmail.com'])

    return None

# @shared_task()
# def send_email_task():
#     sleep(10)
#     send_mail('Celery Task Works',
#               'This is proof the task is still running',
#               'sh107ed@gmail.com',['rigiwid562@sueshaw.com'])


# @app.task(name="Fail_safe_me")
# def fail_safe_me():
#     file_status = checkfilestatus
#     if file_status == checkfilestatus('success'):
#         pt = 'https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n' \
#              'Subject: New Ticket\n' \
#              'Requestor: thabang@gmail.com\n' \
#              'Owner: thabang@alise@gmail.com'
#
#         login = {
#             "user": "guest",
#             "pass": "guest"
#         }
#         with requests.Session() as session:
#             post = session.post(pt, data=login)
#             print(post.text)
#     return 'Give me what I want'
