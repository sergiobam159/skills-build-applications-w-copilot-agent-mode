from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=captain, type='Cycling', duration=45)
        Activity.objects.create(user=batman, type='Swimming', duration=60)
        Activity.objects.create(user=superman, type='Yoga', duration=20)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=captain, points=90)
        Leaderboard.objects.create(user=batman, points=95)
        Leaderboard.objects.create(user=superman, points=85)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', user=ironman)
        Workout.objects.create(name='Cardio', description='Entrenamiento de cardio', user=captain)
        Workout.objects.create(name='Strength', description='Entrenamiento de fuerza', user=batman)
        Workout.objects.create(name='Flexibility', description='Entrenamiento de flexibilidad', user=superman)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
