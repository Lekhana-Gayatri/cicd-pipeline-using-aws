from django.db import models
from django.contrib.auth.models import User
class fundRaised(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=29,choices=[('medical','medical'),('emergency','emergency'),('Education','Education'),('startUps','startUps'),('charity','charity')],default='charity')
    fund_for=models.CharField(max_length=29,choices=[('someoneElse','someoneElse'),('yourself','yourself'),('charity','charity')],default='yourself')
    goal=models.IntegerField(default=0)
    photo=models.ImageField(upload_to='stories/')
    title=models.TextField(max_length=50,unique=True)
    story=models.TextField(max_length=1000)
    present_fund=models.IntegerField(default=0)
    NoDonations=models.IntegerField(default=0)
    withdrawAmount=models.IntegerField(default=0)
    phone=models.TextField()
    def __str__(self):
        return self.title
class Donations(models.Model):
    funds=models.ForeignKey(fundRaised,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    comment=models.TextField(max_length=1000)
    paymentMethod=models.CharField(max_length=30)
    def __str__(self):
        return self.funds.title+"--"+str(self.pk)
class successStories(models.Model):
    funds=models.ForeignKey(fundRaised,on_delete=models.CASCADE)
    iv=models.FileField(upload_to='stories/')
    def __str__(self):
        return self.title