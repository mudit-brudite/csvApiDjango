from django.db import models

# Create your models here.

class Question(models.Model):
    question_title = models.TextField()
    question_description = models.TextField(null=True, blank =True)
    question_constrants= models.CharField(max_length=50,null=True , blank =True)
    question_testcases_input = models.TextField(null=True , blank =True)
    question_testcases_output = models.TextField(null=True , blank =True)
