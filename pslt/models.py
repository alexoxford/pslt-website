from django.db import models

# Create your models here.


class Media(models.Model):
    uri = models.URLField()
    alt_text = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Media'


class Picture(Media):
    pass


class Video(Media):
    pass


class Document(models.Model):
    uri = models.URLField()
    year = models.IntegerField()
    TYPE_CHOICES = (('Proposal', 'Proposal'),
                    ('PDR', 'PDR'),
                    ('CDR', 'CDR'),
                    ('FRR', 'FRR'),
                    ('PLAR', 'PLAR'),
                    ('Other', 'Other'))
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    SUBTYPE_CHOICES = (('Report', 'Report'),
                       ('Slides', 'Slides'),
                       ('Flysheet', 'Flysheet'),
                       ('Single', 'Single'))
    subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES)
    page_count = models.IntegerField()
    name = models.CharField(max_length=500)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.year) + ' ' + self.short_name


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Post(models.Model):
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=10000)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Link(models.Model):
    uri = models.URLField()
    text = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    img_uri = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    img_uri = models.CharField(max_length=500, blank=True)
    role = models.CharField(max_length=500)
    bio = models.CharField(max_length=5000)
    priority = models.IntegerField()

    def __str__(self):
        return self.name


class OutreachEvent(models.Model):
    name = models.CharField(max_length=100)
    img_uri = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
