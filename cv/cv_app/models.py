from django.db import models

class Person(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def get_birth_date(self):
        return self.birth_date

class Career(models.Model):
    # id = models.Index(name='Career')
    title_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=5)

    def get_title(self):
        return self.title_name
    
    def get_duration(self):
        return self.duration
    

class University(models.Model):
    # id = models.Index(name='University')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Studies(models.Model):
    # id = models.Index(name='Studies')
    title_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

class PersonStudies(models.Model):
    # id = models.Index(name='PersonStudies')
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE)

class Company(models.Model):
    # id = models.Index(name='Company')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)

class WorkExperience(models.Model):
    # id = models.Index(name='WorkExperience')
    start_date = models.DateField()
    end_date = models.DateField()
    currently_working = models.BooleanField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)

class Languages(models.Model):
    # id = models.Index(name='Languages')
    language = models.CharField(max_length=30)

class PersonLanguages(models.Model):
    # id = models.Index(name='PersonLanguages')
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)

class SocialMedia(models.Model):
    # id = models.Index(name='SocialMedia')
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)

class PersonMedia(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)