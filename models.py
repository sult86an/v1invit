from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

def get_first_name(self):
    return self.first_name


User.add_to_class("__str__", get_first_name)


#ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Initi(models.Model):
    mub_name = models.CharField(max_length=250)
    leader = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('initiatives:reports', kwargs={'pk': self.pk})

    def __str__(self):
        return self.mub_name


class Goals(models.Model):
    goal = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)

    def __str__(self):
        return self.goal + ' - ' + self.mub.mub_name


class Supports(models.Model):
    support = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)

    def __str__(self):
        return self.support


class Reports(models.Model):
    week_ar = models.CharField(max_length=250)
    week_no = models.CharField(max_length=250)
    mub_r = models.ForeignKey(Initi, on_delete=models.CASCADE)
    ready = models.BooleanField(default=0)
    ratio = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('initiatives:detail',  kwargs={'pk': self.pk}),

    def __str__(self):
        return self.week_ar + ' ' + self.mub_r.mub_name


class Comment(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    grade = models.IntegerField(default=0)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.report.week_ar + ' -  ' + self.report.mub_r.mub_name


class Stages(models.Model):
    stage = models.CharField(max_length=250)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)
    ratio = models.IntegerField(default=0)
    end_date = models.DateField()

    def __str__(self):
        return self.stage


class MainStage(models.Model):

    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stages, on_delete=models.CASCADE)
    ratio = models.IntegerField(default=0)
    end_date = models.CharField(max_length=250, default=' ')
    progress_num = models.IntegerField(default=0)
    info = models.TextField()
    final_rate = models.FloatField(default=0)
    created_date = models.DateTimeField(null=False, default=datetime.now())

    def __str__(self):
        return self.stage.stage


class Risks(models.Model):
    risk = models.CharField(max_length=500)
    mub_risk = models.ForeignKey(Initi, on_delete=models.CASCADE)
    owner_risk = models.CharField(max_length=250)
    probability = models.CharField(max_length=250)
    influence = models.CharField(max_length=250)
    plan = models.TextField()

    def __str__(self):
        return self.risk


class Challenges(models.Model):
    challenge = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)
    owner = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    info = models.TextField()

    def __str__(self):
        return self.challenge + ' - ' + self.mub.mub_name
