from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class USER(AbstractUser):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128, db_column='pw')
    team = models.CharField(max_length=80)

    first_name = None
    last_name = None
    email = None
    is_staff = None
    is_active = None
    date_joined = None