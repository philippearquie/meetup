import os.path
import csv
from datetime import datetime
from Meetup.models import Company,Employee
class InvalidExtensionError(Exception):
    def __init__(self,ext):
        self.ext = ext 
class CSVParser(object):
    def __init__(self,my_file):
        self.file = my_file
        self.reader = None
    def validate(self):
        ext = os.path.splitext(self.file.name)
        if ext[1] != '.csv':
            raise InvalidExtensionError(ext[1])
    def parse(self):
        self.reader = csv.reader(self.file)
        for row in self.reader:
            if row[0]== 'Name':
                continue
            employee = Employee()
            employee.Name = row[0]
            employee.User_ID = row[1]
            employee.Title = row[2]
            employee.Member_ID = row[3]
            try:
                company = Company.objects.get(name__iexact=row[4])
            except Company.DoesNotExist:
                company = Company(name=row[4])
                company.save()
            employee.Company = company
            if row[5]:
                employee.Joined_Group_on = datetime.strptime(row[5],"%d/%m/%Y")
            if row[6]:
                employee.Last_visited_group_on = datetime.strptime(row[6],"%d/%m/%Y")
            if row[7]:
                employee.Last_Attended = datetime.strptime(row[7],"%d/%m/%Y")
            employee.Total_RSVPs = row[8]
            employee.RSVPed_Yes = row[9]
            employee.RSVPed_Maybe = row[10]
            employee.RSVPed_No = row[11]
            employee.Meetups_attended = row[12]
            employee.No_shows = row[13]
            employee.Intro = row[14]
            employee.Photo = row[15]
            employee.Assistant_Organizer = row[16]
            employee.Mailing_List = row[17]
            employee.Url_of_Member_Profile = row[18]
            employee.save()
        
        