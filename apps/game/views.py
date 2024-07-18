<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game
import random

# Create your views here.
def main(req):
    return render(req, 'main.html')

# @login_required
def attack(request):
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
        return redirect('game:detail', game_id=game.id)

    # GET 요청일 경우, 랜덤으로 생성된 카드와 사용자를 템플릿에 전달
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game
import random

# Create your views here.
def main(req):
    return render(req, 'main.html')

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
        return redirect('game:detail', game_id=game.id)

    # GET 요청일 경우, 랜덤으로 생성된 카드와 사용자를 템플릿에 전달
>>>>>>> 139da3ccd826d829b22e4166afb3e16dbb74cf98
    return render(request, 'attack.html', {'cards': cards, 'users': users})