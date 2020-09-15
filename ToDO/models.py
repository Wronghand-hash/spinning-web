from django.db import models

# Create your models here.
class Era(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True  )

    def __str__(self):
        return self.title



class Task(models.Model):
    era = models.ForeignKey(Era ,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, help_text="description . . . ")
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
