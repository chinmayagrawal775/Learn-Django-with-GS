from  django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("---------------------------------------")
    print("logged in")
    print("sender", sender)
    print("request", request)
    print("user", user)
    print("user pass", user.password)
    print(f"kwargs:{kwargs}")

# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("---------------------------------------")
    print("logged out")
    print("sender", sender)
    print("request", request)
    print("user", user)
    print("user pass", user.password)
    print(f"kwargs:{kwargs}")

# user_logged_out.connect(log_out, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("---------------------------------------")
    print("login failed")
    print("sender", sender)
    print("credentials", credentials)
    print("request", request)
    print(f"kwargs:{kwargs}")

# user_loggin_failed.connect(login_failed, sender=User)