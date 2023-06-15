from django.shortcuts import render

# Create your views here.


def home_view(request):
    my_context = {
        'my_list': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'home.html', my_context)
