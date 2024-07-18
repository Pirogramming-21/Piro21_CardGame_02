from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game


@login_required
def game_history(request):
    # 사용자가 공격자인 게임
    attacks = Game.objects.filter(attacker=request.user).order_by('-id')
    
    # 사용자가 수비자인 게임
    defenses = Game.objects.filter(defender=request.user).order_by('-id')
    
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