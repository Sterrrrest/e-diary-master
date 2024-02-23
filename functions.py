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
    subject = get_object_or_404(Subject, title=subject, year_of_study=schoolkid.year_of_study)
    lesson = Lesson.objects.filter(subject=subject).order_by("-date").first()
    random_commendation = random.choice(COMMENDATIONS)
    if not lesson:
        print('Такого урока нет')
    else:
        Commendation.objects.create(text=random_commendation, created=lesson.date, schoolkid=schoolkid, subject=subject, teacher=lesson.teacher)
