from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.
class Run(models.Model):
     distance = models.DecimalField(max_digits=5, decimal_places=2)
     start_Time = models.DateTimeField(auto_now=False, auto_now_add=False)
     end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

     def __str__(self):
          return f'''[{self.distance},{self.start_Time},{self.end_time},{self.user.username}]'''