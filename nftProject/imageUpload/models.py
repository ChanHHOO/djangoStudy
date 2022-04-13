from django.db import models

def forder_name_path(instance, filename):
    
    return '{}/{}'.format(instance.title, filename)

class FileUpload(models.Model):
    
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to=forder_name_path, blank=True)
    content = models.TextField()

    def __str__(self):
        return "먀임야ㅓ미아ㅓㅁㅇ미ㅏ어미ㅏ어민"