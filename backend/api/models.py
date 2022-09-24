import uuid
from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to='brand/images', null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    