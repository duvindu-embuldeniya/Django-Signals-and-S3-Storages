from django.db.models.signals import post_save, post_delete
from . models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

def create_profile(sender, instance, created, *args, **kwargs):
    created_user = instance
    if created:
        Profile.objects.create(
            user = created_user
        )

        subject = "Welcome"
        message = "We are glad you are here!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [created_user.email],
            fail_silently=False,
        )



def delete_user(sender, instance, *args, **kwargs):
    deleted_profile = instance
    user = instance.user

    user.delete()

post_save.connect(create_profile, sender = User)
post_delete.connect(delete_user, sender = Profile)