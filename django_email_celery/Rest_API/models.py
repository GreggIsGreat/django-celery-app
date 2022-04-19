# from django.db import models
#
#
# # Create your models here.
#
#
# class checkfilestatus(models.Model):
#     status = (
#         ("Success", "Success"),
#         ("Fail", "Fail"),
#     )
#     file_status = models.CharField(choices=status, default='None', max_length=200)
#
#     def __str__(self):
#         return self.file_status
