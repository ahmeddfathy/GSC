from django.db import models


class passwords(models.Model):
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.username
    
class chats(models.Model):
    chat = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.chat
    
class answers(models.Model):
    question = models.CharField(max_length=200)
    answer = models.OneToOneField(chats , on_delete=models.CASCADE)


