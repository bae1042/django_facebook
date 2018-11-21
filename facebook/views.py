from django.shortcuts import render, redirect
from facebook.models import Article, Comment

def newsfeed(request) :
    articles = Article.objects.all()

    #코멘트 db 넣기
    if request.method =='POST':
        num = int(request.POST['num'])
        one_feed = Article.objects.get(pk=num)

        Comment.objects.create(
            article = one_feed,
            author = request.POST['author'],
            text = request.POST['text'],
            password = request.POST['password']
        )

    return render(request, 'newsfeed.html', {'articles': articles, 'test':'test'})


# Create your views here.
def play(request):
    return render(request, 'play.html')

count = 0
def play2 (request):
    bae = '배동훈'
    global count
    count = count + 1

    age = 19
    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은 맑았다', '오늘은 춥다', '오늘은 배부르다', 'ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ']

    return render(request, 'play2.html', {'name': bae,
                                          'cnt': count,
                                          'age': status,
                                          'diary': diary})

def bae(request):
    return render(request, 'bae.html')

visitor = 0
def event(request):
    global visitor
    visitor = visitor + 1

    if visitor == 7 :
        print('당첨')
    else :
        print('꽝')

    if visitor == 7 :
        lotto = '당첨'
    else :
        lotto = '꽝'


    return render(request, 'event.html', {'visitor' : visitor, 'lotto' : lotto })


def new_feed(request) :
    # 데이터를 받아서 글 생성

    if request.method == 'POST':
        Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content']+'추신: 감사합니다.',
            password=request.POST['password']
            )

    return render(request,'new_feed.html')



def edit_feed(requet, pk) :
    article = Article.objects.get(pk=pk)

    if requet.method == "POST":
        article.author = requet.POST['author']
        article.title = requet.POST['title']
        article.text = requet.POST['content']
        article.save()
        # 저장 후 해당 글 페이지로 이동
        return redirect('/')

    return render(requet, 'edit_feed.html',
                  {'feed': article})g

def remove_feed(requet, pk) :
    article = Article.objects.get(pk=pk)

    # 글삭제 로직
    if requet.method =="POST":
        if article.password == requet.POST['password']:
            article.delete()
            return redirect('/')
        else:
            pass

    return render(requet, 'remove_feed.html',
                  {'feed':article})