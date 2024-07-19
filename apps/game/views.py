from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.accounts.models import CustomUser
from .models import Game
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def main(request):
    return render(request, 'main.html')

def attack(request):
    # Generate 5 random cards
    cards = random.sample(range(1, 11), 5)
    # 현재 사용자를 제외한 모든 사용자 목록을 가져옴
    users = User.objects.exclude(id=request.user.id)

    if request.method == 'POST':
        # 사용자가 선택한 카드 번호를 가져옴
        selected_card_number = int(request.POST.get('selected_card'))
        # 선택한 수비자 ID를 가져옴
        defender_id = int(request.POST.get('defender'))
        # 해당 ID의 사용자가 존재하는지 확인하고 가져옴
        defender = get_object_or_404(User, id=defender_id)

        # 무작위로 승리 조건 선택 (높은 숫자가 이기거나 낮은 숫자가 이기는 조건)
        win_condition = random.choice(['HIGH', 'LOW'])

        # 새로운 게임을 생성
        game = Game.objects.create(
            attacker=request.user,  # 현재 로그인된 사용자
            defender=defender,      # 선택한 수비자
            attacker_card=selected_card_number,  # 선택한 카드 번호
            win_condition=win_condition,         # 승리 조건
            status='PENDING'                     # 게임 상태를 'PENDING'으로 설정
        )
        # 생성된 게임의 상세 페이지로 리디렉션
        return redirect('game:game_detail', pk=game.id)

    # GET 요청일 경우, 랜덤으로 생성된 카드와 사용자를 템플릿에 전달
    return render(request, 'attack.html', {'cards': cards, 'users': users})

@login_required # 로그인 여부 확인
def game_history(request):
    # 사용자가 공격자인 게임
    attacks = Game.objects.filter(attacker=request.user).order_by('-id')
    
    # 사용자가 수비자인 게임
    defenses = Game.objects.filter(defender=request.user).order_by('-id')

    # print("Attacks:", attacks.count())
    # print("Defenses:", defenses.count())
    
    context = {
        'attacks': attacks,
        'defenses': defenses,
    }
    return render(request, 'list.html', context)

@login_required
def cancel_game(request, pk):
    game = get_object_or_404(Game, id=pk, attacker=request.user, status='PENDING')
    game.status = 'CANCELLED'
    game.save()
    return redirect('game:game_history')


def game_detail(request, pk):
    game=Game.objects.get(id=pk)
    ctx={
        'game':game, 
        'result_text':'',
        'user_win':None,
    }

    if game.status=='ONGOING':
        ctx['buttons']=['전적목록']
    elif game.status=='PENDING':
        ctx['result_text']='진행중...'
        ctx['buttons']=['전적목록']
    elif game.status=="FINISHED":
        win_condition=game.win_condition
        
        if win_condition=='LOW':
            ctx['result_text']='숫자가 작은 사람이 이깁니다.'
        elif win_condition=='HIGH':
            ctx['result_text']='숫자가 큰 사람이 이깁니다.'

        if win_condition=='LOW':
            ctx['user_win']=game.attacker_card < game.defender_card
        else:
            ctx['user_win']=game.attacker_card > game.defender_card
    
        ctx['buttons']=['전적목록']

    return render(request, 'detail.html', ctx)

import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Game

@login_required
def counter_attack(request, pk):
    game = get_object_or_404(Game, id=pk, defender=request.user, status='PENDING')
    if request.method == 'POST':
        # 반격 로직 구현
        game.defender_card = int(request.POST['card'])
        game.status = 'FINISHED'

        # 승패 결정 및 점수 계산 로직
        if game.win_condition == 'HIGH':
            if game.attacker_card > game.defender_card:
                game.result = 'ATTACKER_WIN'
                game.attacker_score = game.attacker_card
                game.defender_score = -game.defender_card
            elif game.attacker_card == game.defender_card:
                game.result = 'DRAW'
                game.attacker_score = game.defender_score = 0
            else:
                game.result = 'DEFENDER_WIN'
                game.attacker_score = -game.attacker_card
                game.defender_score = +game.defender_card
        else:
            if game.attacker_card < game.defender_card:
                game.result = 'ATTACKER_WIN'
                game.attacker_score = game.attacker_card
                game.defender_score = -game.defender_card
            elif game.attacker_card == game.defender_card:
                game.result = 'DRAW'
                game.attacker_score = game.defender_score = 0
            else:
                game.result = 'DEFENDER_WIN'
                game.attacker_score = -game.attacker_card
                game.defender_score = +game.defender_card
        
        game.attacker.score += game.attacker_score
        game.defender.score += game.defender_score
        game.attacker.save()
        game.defender.save()
        game.save()
        return redirect('game:game_history')
    
    # 1부터 10까지의 숫자 중 랜덤하게 5개 선택
    random_numbers = random.sample(range(1, 11), 5)
    
    context = {
        'game': game,
        'random_numbers': random_numbers,
    }
    return render(request, 'counter.html', context)


def ranking(request):
    top_users = CustomUser.objects.all().order_by('-score')[:3]  # 상위 3명만 가져옴
    ctx = {
        'top_users': top_users,
    }
    return render(request, 'ranking.html', ctx)