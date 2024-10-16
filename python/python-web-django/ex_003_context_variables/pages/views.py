from django.shortcuts import render

# Create your views here.


def home_view(request):
    my_context = {
        'my_list': ['Item 1', 'Item 2', 'Item 3'],
        'my_dict': {'key_1': 'Value 1',
                    'key_2': 'Value 2'},
        'section': {'home_page': 'Context variables'},
    }
    return render(request, 'home.html', my_context)
