from django.db import models



class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.name
    
    
class TestModel(models.Model):
	title = models.CharField(max_length=120)
    # Создаст дату при каждом сохранении объекта
	date1 = models.DateField(auto_now=True)
    # Создаст дату при создании объекта
	date2 = models.DateField(auto_now_add=True)
    # Создаст дату и время при изменении объекта
	date3 = models.DateTimeField(auto_now=True)
    # Создаст дату и время при создании объекта
	date4 = models.DateTimeField(auto_now_add=True)
 
    # def __str__(self):
    #     return self.title
    
    
    
