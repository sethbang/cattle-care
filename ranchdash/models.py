from django.db import models
from django.db.models import IntegerField, Model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
import datetime
from geoposition.fields import GeopositionField


# Create your models here.

class Pasture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, help_text="Enter the animals name", blank=True)
    # location = GeopositionField()
    loc = models.FloatField(default=1.0)
    max_cows = models.PositiveSmallIntegerField(help_text="Maximum number of cows possible in pasture.", default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

# class Beast(models.Model):
#     SEASONS = (
#         ('W', 'Winter'),
#         ('SP', 'Spring'),
#         ('SU', 'Summer'),
#         ('F', 'Fall'),
#     )
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=30, help_text="Enter the animals name", blank=True)
#     birth_year = models.PositiveSmallIntegerField(validators=[
#         MaxValueValidator(datetime.date.today().year),
#         MinValueValidator(1990)
#     ])
#     birth_season = models.CharField(max_length=002, choices=SEASONS)