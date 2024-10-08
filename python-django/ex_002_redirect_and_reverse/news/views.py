from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect
)
from django.urls import reverse


topics = {
    'games': 'Games page',
    'mobile': 'Mobile page',
    'tech': 'Technology page'
}


def news_page_view(request, topic):
    try:
        result = topics[topic]
        return HttpResponse(result)
    except:
        raise Http404('404 page not found :(')
    return HttpResponseRedirect


def news_page_num_view(request, page_num):
    topics_list = list(topics.keys())
    
    try:
        topic_name = topics_list[page_num]
        return HttpResponseRedirect(reverse('topic-page', args=[topic_name]))
    except:
        valid_page_nums = ''
        for (num, item) in enumerate(topics_list):
            valid_page_nums += f'{num}: {item}\n'
        raise Http404(f'404 page not found :()' + '\n\n' + 'Valid page numbers:\n' + valid_page_nums)
