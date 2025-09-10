from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Spiderman', email='spiderman@marvel.com', team=team)
        self.assertEqual(user.name, 'Spiderman')
        self.assertEqual(user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Ironman', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Thor', email='thor@marvel.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Batman', email='batman@dc.com', team=team)
        workout = Workout.objects.create(name='Pushups', description='Upper body workout', user=user)
        self.assertEqual(workout.name, 'Pushups')
