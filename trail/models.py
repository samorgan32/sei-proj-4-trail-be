from django.db import models

# Create your models here.
class Walkthrough(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', related_name = 'walkthrough', on_delete = models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    cover_slide = models.ImageField(upload_to='images/', default='images/default.jpeg')

    def __str__(self):
        return self.title

class Slide(models.Model):
    walkthrough = models.ForeignKey(Walkthrough, on_delete=models.CASCADE, related_name='slides')
    position = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpeg')
    description = models.TextField()


    
    
    class Meta:
        ordering = ['position']
        verbose_name_plural = 'slides'


    def __str__(self):
        return f'walkthrough: {self.walkthrough} slide #: {self.position}'

