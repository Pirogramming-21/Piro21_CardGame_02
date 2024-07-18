from django.shortcuts import render

def main(req):
    return render(req, 'main.html')

def attack(req):
    return render(req, 'attack.html')

def counter(req):
    return render(req, 'counter.html') 

def game_list(req):
    return render(req, 'list.html')

def game_detail(req, pk):
    return render(req, 'detail.html', {'pk': pk})

def ranking(req):
    return render(req, 'ranking.html')