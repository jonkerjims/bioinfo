from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'laboratory_tmp/index.html')


def team(request):
    return render(request,'laboratory_tmp/team.html')