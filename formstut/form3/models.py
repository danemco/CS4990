from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
GENRES = (
       ('c', 'Classical'), 
       ('r', 'Rock'), 
       ('y', 'Country'),
       ('t', 'Techno'),
   )


class Song(models.Model):
   title = models.CharField(max_length=200)
   musician = models.CharField(max_length=200)
   genre = models.CharField(max_length=2, choices=GENRES)

   def __unicode__(self):
      return self.title

   def get_absolute_url(self):
      return reverse('form3:songupdate', kwargs={'pk': self.pk})
