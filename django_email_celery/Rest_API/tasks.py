# from celery import shared_task, Celery
# # from .models import checkfilestatus
# from . import rt_rest
# import requests
#
#
# app = Celery()
#
#
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
