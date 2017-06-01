from django.shortcuts import render

def post_list(request):
    return render(request, 'review/post_list.html', {})
