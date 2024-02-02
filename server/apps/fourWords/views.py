from django.shortcuts import render

def fourWords_main(request):
    return render(request, 'games/fourWords_main.html')

def fourWords_game_start(request):
    pass

def next_fourWords_ajax(request):
    pass
