from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime

# Create your models here.
class Stage(models.Model):
    name = models.CharField(max_length = 200)
    order = models.IntegerField(help_text = 'The order this is displayed on the screen')
    description = models.TextField(blank = True, null = True)
    value = models.IntegerField(help_text = 'On a scale of 0 to 100 of the stage of the pipeline')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Company(models.Model):
    name = models.CharField(max_length = 200)
    website = models.URLField(max_length = 200, blank = True, null = True)
    address1 = models.CharField(max_length = 200, blank = True, null = True)
    address2 = models.CharField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    state = models.CharField(max_length = 200, blank = True, null = True)
    zipcode = models.CharField(max_length = 200, blank = True, null = True)
    country = models.CharField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 200, blank = True, null = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'

class Contact(models.Model):
    company = models.ForeignKey(Company, blank = True, null = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address1 = models.CharField(max_length = 200, blank = True, null = True)
    address2 = models.CharField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    state = models.CharField(max_length = 200, blank = True, null = True)
    zipcode = models.CharField(max_length = 200, blank = True, null = True)
    country = models.CharField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 200, blank = True, null = True)
    email  = models.EmailField(max_length = 200, blank = True, null = True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.get_full_name()

class Campaign(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.name

class Opportunity(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField()
    stage = models.ForeignKey(Stage)
    contact = models.ForeignKey(Contact)
    value = models.FloatField(help_text='How much this opportunity is worth to the organization')
    source = models.ForeignKey(Campaign, help_text='How did this contact find out about us?', blank = True, null = True)
    user = models.ForeignKey(User, help_text='The user that is assigned to this opportunity')
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
            return self.name

    class Meta:
        verbose_name_plural = 'opportunities'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Opportunity, self).save(*args, **kwargs)
        

class Reminder(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateField(help_text="due date")
    note = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.opportunity + u": " + self.note

class Report(models.Model):
    name = models.CharField(max_length = 200)
    link = models.URLField()

    def __unicode__(self):
        return self.name

class CallLog(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.opportunity + " on " + self.date.strftime("%Y-%m-%d") + " by " + self.user.get_full_name() 

    class Meta:
        ordering = ['-date','user']

class OpportunityStage(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    stage = models.ForeignKey(Stage)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.opportunity + " moved to " + self.stage

