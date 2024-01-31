from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "games/main.html")

def image(request):
    return render(request, "games/detail.html")