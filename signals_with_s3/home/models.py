from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'profile/', blank=True, null=True)
    bio = models.TextField(default='Lorem...', blank=True, null=True)

    @property
    def imgUrl(self):
        try:
            return self.image.url
        except:
            return 'static/images/default.png/'