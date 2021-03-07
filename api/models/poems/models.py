from django.db import models
from django.utils.timezone import now

class Poems(models.Model):
    content=models.CharField(max_length=1000,blank=True,null=True)
    image_url=models.URLField(unique=True)
    LANGUAGE=(('tamil','Tamil, the ancient language'),('english','English, the language of the world'))
    language=models.CharField(max_length=10,choices=LANGUAGE,blank=True,null=True)
    wroteAt=models.DateTimeField(blank=True,null=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:10]
