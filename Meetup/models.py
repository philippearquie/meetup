from django.db import models
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 30,unique=True)
    def __unicode__(self):
        return self.name
class Employee(models.Model):
    Name = models.CharField(max_length = 30)
    User_ID = models.CharField(max_length = 15)
    Title = models.CharField(max_length = 15)
    Member_ID = models.IntegerField()
    Company = models.ForeignKey(Company)
    Joined_Group_on = models.DateField()
    Last_visited_group_on = models.DateField()
    Last_Attended = models.DateField(null=True)
    Total_RSVPs = models.IntegerField()
    RSVPed_Yes = models.IntegerField()
    RSVPed_Maybe = models.IntegerField()
    RSVPed_No = models.IntegerField()
    Meetups_attended = models.IntegerField()
    No_shows = models.IntegerField()
    Intro = models.CharField(max_length = 10)
    Photo = models.CharField(max_length = 10)
    Assistant_Organizer = models.CharField(max_length = 10)
    Mailing_List = models.CharField(max_length = 10)
    Url_of_Member_Profile = models.CharField(max_length = 300)
    def __unicode__(self):
        return self.name
