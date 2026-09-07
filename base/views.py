from django.shortcuts import render


# create rooms

room = [   
    {'id': 'id1', 'name': 'lets learn python'},
    {'id': 'id2', 'name': 'lets learn java'},
    {'id': 'id3', 'name': 'lets learn c++'},
]



def home(request):
    return render(request, 'home.html', {'rooms': room})

def rooms(request):
    return render(request, 'rooms.html')