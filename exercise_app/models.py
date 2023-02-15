import uuid
from django.db import models
# Create your models here.

class UserModel(models.Model):
    id = models.UUIDField(help_text="Unique key", primary_key=True, default=uuid.uuid4, editable=False)

