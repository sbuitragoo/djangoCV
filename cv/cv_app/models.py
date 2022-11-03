from django.db import models

class Person(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()

    def __str__(self):
        return self.id

class Career(models.Model):
    # id = models.Index(name='Career')
    title_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=5)

    def __str__(self):
        return self.title_name

class University(models.Model):
    # id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Studies(models.Model):
    # id = models.UUIDField(primary_key=True)
    title_name = models.ForeignKey(Career, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title_name.title_name

class PersonStudies(models.Model):
    # id = models.UUIDField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    study_name = models.ForeignKey(Studies, on_delete=models.CASCADE)

    def __str__(self):
        return self.person_id.id

class Company(models.Model):
    # id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    # id = models.UUIDField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    currently_working = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.person.id

class Languages(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language

class PersonLanguages(models.Model):
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)

    def __str__(self):
        return self.person.id

class SocialMedia(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class PersonMedia(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    value = models.CharField(default="sbuitragoo", max_length=30)

    def __str__(self):
        return self.person.id