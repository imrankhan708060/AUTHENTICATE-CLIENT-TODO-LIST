from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class Task(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    #fetching a data through primary key
    def get_absolute_url(self):
        return reverse("todos:edt",kwargs={"pk":self.pk})
    #deleting a data through primary key
    def delete_data(self):
        return reverse("todos:delte",kwargs={"pk":self.pk})




