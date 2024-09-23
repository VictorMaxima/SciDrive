from django.contrib.auth.backends import BaseBackend
class MyBackend(BaseBackend):
    def authenticate( request, email=None, password=None):
        try:
            user = Individual.objects.get(email=email)
            if user.check_password(password):
                return user
        except Individual.DoesNotExist:
            print(Individual.objects)
            return None
        print(Individual.objects)
        print("yes")
        return user
    def get_user(self, client_id):
        try:
            return Individual.objects.get(pk=client_id)
        except Individual.DoesNotExist:
            return None