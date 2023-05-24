from django.db import models


class History(models.Model):
	question = models.CharField(max_length=200)
	answer = models.TextField(max_length=5000)

	class Meta:
		verbose_name_plural = 'Histories'

	def __str__(self):
		return self.question


