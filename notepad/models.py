from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=100)
    #image = models.ImageField(blank= True, null= True)
    url = models.URLField(blank= True, null= True)
    timestand = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return f"/notes/{self.pk}/delete"

    def get_update_url(self):
        return f"/notes/{self.pk}/update"







