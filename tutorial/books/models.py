from django.db import models

# Create your models here.

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=20, null=True)
    state_provence = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
