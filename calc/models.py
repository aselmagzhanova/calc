from unidecode import unidecode
import django
from django.conf import settings
from django.db import models

# Create your models here.

def get_user_model_fk_ref():
    if django.VERSION[:2] >= (1, 5):
        return settings.AUTH_USER_MODEL
    else:
        return 'auth.User'

class Graph(models.Model):
    class Meta():
        db_table = 'graphics'

    function_text = models.TextField()
    user = models.ForeignKey(get_user_model_fk_ref())