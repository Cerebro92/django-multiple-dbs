import string
import random

from django.core.management.base import BaseCommand, CommandError
from college.models import College
from student.models import Student


class Command(BaseCommand):
    help = 'Populate college & students tables'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str)

        parser.add_argument(
            '--num_records',
            help='Num of records to sync in tables',
            default=100,
            type=int
        )

    def handle(self, *args, **options):
        _map = {
            'college': self.populate_colleges,
            'student': self.populate_students
        }

        model_name = options['model_name']
        num_records = options['num_records']

        if model_name not in [College._meta.app_label, Student._meta.app_label]:
            raise CommandError("Invalid model name. please select between college and student")

        func = _map[model_name]
        func(num_records=num_records)

        self.stdout.write(self.style.SUCCESS('Successfully added %s records' % num_records))

    @classmethod
    def populate_colleges(cls, num_records):
        for _ in range(num_records):
            name = ''.join(random.choices(string.ascii_uppercase, k=20))
            established_year = random.randint(1920, 2000)
            College.objects.create(name=name, established_year=established_year)

    @classmethod
    def populate_students(cls, num_records):
        for _ in range(num_records):
            name = ''.join(random.choices(string.ascii_uppercase, k=7))
            age = random.randint(20, 28)
            gender = random.choice(['M', 'F'])
            Student.objects.create(name=name, age=age, gender=gender)
