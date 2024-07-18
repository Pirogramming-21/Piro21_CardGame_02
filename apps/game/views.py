from django.shortcuts import render
from .models import Game
import random

# Create your views here.
def main(req):
    return render(req, 'main.html')

def game_detail(request, pk):
    game=Game.objects.get(id=pk)
    ctx={
        'game':game, 
        'result_text':'',
        'player1_win':None,
    }

    if game.status=='ONGOING':
        ctx['result_text']='진행중...'
        ctx['buttons']=['게임취소', '전적목록']
    elif game.status=='PENDING':
        ctx['buttons']=['대응하기', '전적목록']
    elif game.status=="FINISHED":
        win_condition=game.win_condition
        
        if win_condition=='LOW':
            ctx['result_text']='숫자가 작은 사람이 이깁니다.'
        elif win_condition=='HIGH':
            ctx['result_text']='숫자가 큰 사람이 이깁니다.'

        if win_condition=='LOW':
            ctx['player1_win']=game.attacker_card < game.defender_card
        else:
            ctx['player1_win']=game.attacker_card > game.defender_card
    
        ctx['buttons']=['전적목록']

    return render(request, 'detail.html', ctx)