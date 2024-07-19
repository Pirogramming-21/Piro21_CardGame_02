from django.db import models
from django.conf import settings

class Game(models.Model):
    attacker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='attacks', on_delete=models.CASCADE)
    defender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='defenses', on_delete=models.CASCADE)
    attacker_card = models.IntegerField(null=True)
    defender_card = models.IntegerField(null=True)
    attacker_score = models.IntegerField(default=0) # 공격자 게임 점수 추가
    defender_score = models.IntegerField(default=0) # 수비자 게임 점수 추가

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

    RESULT_CHOICES = [
        ('ATTACKER_WIN', 'Attacker Win'),
        ('DEFENDER_WIN', 'Defender Win'),
        ('DRAW', 'Draw'),
    ]

    win_condition = models.CharField(max_length=4, choices=WIN_CONDITION_CHOICES, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    result = models.CharField(max_length=20, choices=RESULT_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Game {self.id}: {self.attacker.username} vs {self.defender.username}"