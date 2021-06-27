from django.db import models

# Create your models here.
class info(models.Model):
	name=models.CharField(max_length=100)
	pno=models.IntegerField()

	def __str__(self):
		return str(self.id) + "  " + self.name + "  " + str(self.pno)

	class meta :
		db_table='details' 