from django import forms
from .models import *


class TaskFrom(forms.ModelForm):
	"""docstring for TaskFrom"""
	class Meta:
		model = Task
		fields = '__all__'
