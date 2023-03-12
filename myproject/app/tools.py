from django.core.mail import send_mail
from django.template import loader
from .models import Profile, Foo
from django.contrib.auth.models import User


def sendMail(parameter):
    pickedProfile = Profile.objects.get(id=parameter)
    from_email = "Migrate Wisely Mail Department <migratewisely@outlook.com>"
    to_list = ['ozan@tictocsoft.com']
    subject = "New Register"
    message = "New Message Sent"
    html_message = loader.render_to_string(
        "email/newRegistration.html",
        {
            "pickedProfile": pickedProfile,
        }
    )
    send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)

    return True



def sendChangeEmail(pkey, theEkey):
    encrypted_id = Foo.objects.get_by_ekey(theEkey)
    profile = Profile.objects.get(id=pkey)
    profileEmail = profile.email
    from_email = "Migrate Wisely Mail Department <migratewisely@outlook.com>"
    to_list = [profileEmail]
    subject = "E-Mail Change Request"
    message = "Your Changing Code Is Provided"
    html_message = loader.render_to_string("email/changeEmail.html",{"profile": profile,"encrypted_id":encrypted_id,})
    send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)
    return True


def sendChangePassword(pkey, theEkey):
    encrypted_id = Foo.objects.get_by_ekey(theEkey)
    profile = Profile.objects.get(id=pkey)
    profileEmail = profile.email
    from_email = "Migrate Wisely Mail Department <migratewisely@outlook.com>"
    to_list = [profileEmail]
    subject = "Password Change Request"
    message = "Your Changing Code Is Provided"
    html_message = loader.render_to_string("email/changePassword.html",{"profile": profile,"encrypted_id":encrypted_id,})
    send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)
    return True
