<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    attacker = models.ForeignKey(User, related_name='attacks', on_delete=models.CASCADE)
    defender = models.ForeignKey(User, related_name='defenses', on_delete=models.CASCADE)
    attacker_card = models.IntegerField(null=True)
    defender_card = models.IntegerField(null=True)

    STATUS_CHOICES = [
        ('PENDING', '반격 대기'),
        ('ONGOING', '게임 진행 중'),
        ('FINISHED', '게임 종료'),
        ('CANCELLED', '취소')
    ]

    WIN_CONDITION_CHOICES = [
        ('HIGH', 'Higher number wins'),
        ('LOW', 'Lower number wins'),
    ]

    win_condition = models.CharField(max_length=4, choices=WIN_CONDITION_CHOICES, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    result = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
=======
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    attacker = models.ForeignKey(User, related_name='attacks', on_delete=models.CASCADE)
    defender = models.ForeignKey(User, related_name='defenses', on_delete=models.CASCADE)
    attacker_card = models.IntegerField(null=True)
    defender_card = models.IntegerField(null=True)

    STATUS_CHOICES = [
        ('PENDING', '반격 대기'),
        ('ONGOING', '게임 진행 중'),
        ('FINISHED', '게임 종료'),
        ('CANCELLED', '취소')
    ]

    WIN_CONDITION_CHOICES = [
        ('HIGH', 'Higher number wins'),
        ('LOW', 'Lower number wins'),
    ]

    win_condition = models.CharField(max_length=4, choices=WIN_CONDITION_CHOICES, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    result = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
>>>>>>> 139da3ccd826d829b22e4166afb3e16dbb74cf98
        return f"Game {self.id}: {self.attacker.username} vs {self.defender.username}"