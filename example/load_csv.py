from app1.models import Heart
import csv

with open('heart_3.csv') as f:
    reader = csv.reader(f)
    for idx, row in enumerate(reader):
        print(idx, row)
        _, created = Heart.objects.get_or_create(
            age=row[0],     sex=row[1],     chest_pain=row[2],
            resting_blood_pressure=row[3],     serum_cholestoral=row[4],
            fasting_blood_sugar=row[5],
            resting_electrocardiographic=row[6],
            maximum_heart_rate_achieved=row[7],
            exercise_induced_angina=row[8],
            depression_induced_by_exercise_relative_to_rest=row[9],
            slope_of_the_peak_exercise=row[10],
            number_of_major_vessels_colored_by_flourosopy=row[11],
            thal=row[12],     presence_of_heart_disease=row[13],
        )
