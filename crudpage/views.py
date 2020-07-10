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

def detail(request, id):
    myposting = Posting.objects.get(id=id)

    return render(request, 'detail.html', {
        'myposting' : myposting
    })

def delete(request, id):
    if request.method == "POST":
        myposting = Posting.objects.get(id=id)
        myposting.delete()
        return redirect('/')
    else:
        return redirect('/')

def edit(request, id):
    if request.method == "POST":
        myposting = Posting.objects.get(id=id)
        
        newtitle = request.POST['title']
        newcontents = request.POST['contents']

        myposting.title = newtitle
        myposting.contents = newcontents
        myposting.save()

        return redirect('../')
    else:
        myposting = Posting.objects.get(id=id)
        return render(request, 'edit.html', {
            'myposting' : myposting
        })