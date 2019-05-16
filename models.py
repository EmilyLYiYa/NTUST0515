from django.db import models

# Create your models here.
# class Restaurant(models.Model):
	# name = models.CharField(max_length=20)
	# phone_number = models.CharField(max_length=15)
	# address =  models.CharField(max_length=50, blank=True) 

# class Food(models.Model):
	# name = models.CharField(max_length=20)
	# price = models.DecimalField(max_digits=3, decimal_places=0)
	# comment = models.CharField(max_length=50, blank=True)
	# is_spicy = models.BooleanField(default=False)
	# restaurant = models.ForeignKey(Restaurant)

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0) 