from django.db import models


class Heart(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    chest_pain = models.IntegerField()
    resting_blood_pressure = models.IntegerField()
    serum_cholestoral = models.IntegerField()
    fasting_blood_sugar = models.IntegerField()
    resting_electrocardiographic = models.IntegerField()
    maximum_heart_rate_achieved = models.IntegerField()
    exercise_induced_angina = models.IntegerField()
    depression_induced_by_exercise_relative_to_rest = models.DecimalField(
        max_digits=10, decimal_places=3)
    slope_of_the_peak_exercise = models.IntegerField()
    number_of_major_vessels_colored_by_flourosopy = models.IntegerField()
    thal = models.IntegerField()
    presence_of_heart_disease = models.IntegerField()
