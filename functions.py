import random

from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Subject
from datacenter.models import Lesson
import os

from environs import Env
env = Env()
env.read_env()


def fix_marks(schoolkid):
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid)
    schoolkid_marks.filter(points__lt=4).update(points="5")


def delete_chastisement(schoolkid):
    chast_schoolkid=Chastisement.objects.filter(schoolkid=schoolkid)
    chast_schoolkid.delete()

def create_commendation(schoolkid, subject):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)[0]
    texts = ["Brilliant", "Super", "Genius"]
    subject = Subject.objects.filter(title=subject, year_of_study='6')[0]
    teacher = Lesson.objects.filter(subject=subject)[0].teacher
    lesson_date = Lesson.objects.filter(subject=subject).order_by('-date')[0].date
    random_text = random.choice(texts)

    Commendation.objects.create(text=random_text, created=lesson_date, schoolkid=schoolkid, subject=subject, teacher=teacher)
