import random

from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Subject
from datacenter.models import Lesson
from django.shortcuts import get_object_or_404


COMMENDATIONS = ["Brilliant", "Super", "Genius"]


def fix_marks(schoolkid):
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid)
    schoolkid_marks.filter(points__lt=4).update(points="5")


def delete_chastisement(schoolkid):
    chastisement_schoolkid = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement_schoolkid.delete()

def create_commendation(schoolkid, subject):
    schoolkid = get_object_or_404(Schoolkid, full_name__contains=schoolkid)
    subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
    teacher = Lesson.objects.filter(subject=subject)[0].teacher
    lesson_date = Lesson.objects.filter(subject=subject).order_by('-date').first().date
    random_commendation = random.choice(COMMENDATIONS)

    Commendation.objects.create(text=random_commendation, created=lesson_date, schoolkid=schoolkid, subject=subject, teacher=teacher)
