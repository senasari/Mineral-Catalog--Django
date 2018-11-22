from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=100, default="")
    image_filename = models.TextField(default="")
    image_caption = models.TextField(default="")
    category = models.TextField(default="")
    formula = models.TextField(default="")
    strunz_classification = models.TextField(default="")
    color = models.TextField(default="")
    crystal_system = models.TextField(default="")
    unit_cell = models.TextField(default="")
    crystal_symmetry = models.TextField(default="")
    cleavage = models.TextField(default="")
    mohs_scale_hardness = models.TextField(default="")
    luster = models.TextField(default="")
    streak = models.TextField(default="")
    diaphaneity = models.TextField(default="")
    optical_properties = models.TextField(default="")
    group = models.TextField(default="")
    refractive_index = models.TextField(default="")
    crystal_habit = models.TextField(default="")
    specific_gravity = models.TextField(default="")

    def __str__(self):
        return self.name
