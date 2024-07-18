from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game


def main(request):
    return render(request, 'main.html')

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
def cancel_game(request, game_id):
    game = get_object_or_404(Game, id=game_id, attacker=request.user, status='PENDING')
    game.status = 'CANCELLED'
    game.save()
    return redirect('game_history')

@login_required
def counter_attack(request, game_id):
    game = get_object_or_404(Game, id=game_id, defender=request.user, status='PENDING')
    if request.method == 'POST':
        # 반격 로직 구현
        game.defender_card = int(request.POST['card'])
        game.status = 'FINISHED'
        # 승패 결정 로직 (예시)
        if game.win_condition == 'HIGH':
            game.result = 'ATTACKER_WIN' if game.attacker_card > game.defender_card else 'DEFENDER_WIN'
        else:
            game.result = 'ATTACKER_WIN' if game.attacker_card < game.defender_card else 'DEFENDER_WIN'
        game.save()
        return redirect('game_history')
    return render(request, 'counter_attack.html', {'game': game})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'detail.html', {'game': game})