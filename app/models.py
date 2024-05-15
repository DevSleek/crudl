from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to='media/photos', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'heic']),])
    video = models.FileField(upload_to='media/videos')
    voice = models.FileField(upload_to='media/audios')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


