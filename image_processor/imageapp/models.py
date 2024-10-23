from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_image = models.ImageField(upload_to='processed_images/', blank=True, null=True)
