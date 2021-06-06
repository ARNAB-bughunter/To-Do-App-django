from django.db import models

# Create your models here.

class Task(models.Model):
	title=models.CharField(max_length=150,null=False)
	is_complete=models.BooleanField(default=False)
	due_date=models.DateField(null=False)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

