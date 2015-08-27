from django.db import models

# Create your models here.

class Question(models.Model):
    pub_date = models.DateTimeField('Publication Date')
    question_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.choice_text
