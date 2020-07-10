from django.shortcuts import render, redirect
from .models import Posting

def index(request):
    posting = Posting.objects.all()
    return render(request, 'index.html', {
        'posting' : posting
    })

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        # date는 model에서 auto_now옵션을 넣어줬기 때문에 자동으로 현재 시간이 들어간다.

        new_posting = Posting.objects.create(
            title = title,
            contents = contents
        )
        return redirect('/')
    
    else:
        # http 통신 중 get을 호출하면 그냥 페이지가 나온다
        return render(request, 'create.html')

    