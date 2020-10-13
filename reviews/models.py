from django.db import models

# Create your models here.


class Position(models.Model):
    # let's not do a company model for now, dunno if this is good or not
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
  
    def __str__(self):
        return "%s, %s (%s)" % (self.company_name, self.job_title, self.location)

class Review(models.Model):
    
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    comment = models.TextField()

    user_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    
    total_time = models.IntegerField(null=True)
    total_number_interviews = models.IntegerField(null=True)
    has_live_coding = models.BooleanField(default=False)
    has_pair_programming = models.BooleanField(default=False)
    has_take_home = models.BooleanField(default=False)
    can_meet_team = models.BooleanField(default=False)
    got_an_offer = models.BooleanField(default=False)
    would_recommend = models.BooleanField(default=False)

    rating = models.IntegerField(choices=RATING_CHOICES)

    def __unicode__(self):
        return self.title
