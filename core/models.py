from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_user = models.IntegerField()
    bio = models.TextField(blank=True) #não precisa ter uma bio, então se não tiver, funciona do mesmo jeito.
    profileimg = models.ImageField(upload_to='profile_images', default='login_blank.png') #autoexplicativo 
    location = models.CharField(max_length=100, blank=True) #se você quiser, pode escrever, mas se não, continua rodando.


    def _str_(self):
        return self.user.username