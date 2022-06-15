from django.db import models

class DjangoClasses(models.Model):
	Title = models.CharField(max_length=50)
	Course_Number = models.IntegerField(blank=True, null=False)
	Instructor = models.CharField(max_length=50, blank=True, null=False)
	Duration = models.FloatField(blank=True, null=False)

	objects = models.Manager() # the objects all come from the models we made

	def __str__(self):
		return self.Title # This will name the objects by their title.