from django.db import models
from django.core.files.storage import FileSystemStorage
from Project1 import settings
class reg(models.Model):
	Value=models.CharField(max_length=75)
	Choose_file=models.FileField(upload_to="files_Entry")
	def __str__(self):
		return self.Value

class log(models.Model):
	fk=models.ForeignKey(reg,related_name='fk',on_delete=models.CASCADE)
	created_update=models.TextField()
	old_value=models.TextField(null=True)
	new_value=models.TextField(null=True)
	file_updated=models.BooleanField(null=True)
	time=models.DateTimeField(auto_now=True)
	

