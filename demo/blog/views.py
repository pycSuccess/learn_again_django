from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models import Sum,Min,Max,Avg,Count
import datetime
import json
from django.contrib import auth
from django.core.paginator import Paginator
import time
# Create your views here.


from blog.models import Book
from blog.models import Emp
from blog.models import Publish
from blog.models import Author
from blog.models import AuthorDetail
from blog.models import UserInfo
from blog.blog_from import UserInfo as UiForm


def index(request):
    if request.COOKIES.get('is_login'):
        username = request.COOKIES.get('username')
        return render(request, 'index.html', {'username':username})
    url = reverse('login')
    return redirect(url)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'mqy' and password == '123456':
            url = reverse('index')
            rsp = redirect(url)
            rsp.set_cookie('is_login',True)
            rsp.set_cookie('username', username)
            return rsp
    return render(request, 'login.html')


def add(request):

    # 使用类名+objects进行相关操作
    # book = Book.objects.create(title="放风筝的人", price="14.11", pub_date="2017-12-12", publish="苹果出版社", state=True)
    # print(book.title)
    # book = Book(title='放风的人', price='11.22', pub_date='2019-11-11', publish='苹果出版社', state=False)
    # book.save()
    return HttpResponse('添加成功')


def select(request):
    # books_list = Book.objects.all()    # 返回的是queryset 里面存的是多条记录对象
    # print(type(books_list))
    # print(books_list)
    # print(books_list[0].title)
    # filter_books = Book.objects.filter(title = '放风筝的人')  # 返回的也是queryset
    # print(type(filter_books))
    # print(filter_books[0].title)
    # obj_book = Book.objects.get(title='放风的人') # 只有get返回的是表的一条记录也就是一个对象
    # print(type(obj_book))
    # print(obj_book.title)
    # books_list = Book.objects.exclude(title='放风的人') # 返回的也是queryset 该类型支持切片需要取出单个对象进行操作
    # print(type(books_list))
    # print(books_list[0].title)
    # books_list = Book.objects.order_by('price')   # 使用order_by的时候一定是queryset类型 同时要将排序字段作为参数
    # print(books_list)
    # count = Book.objects.all().filter(title='放风的人').count()  # 只有是queryset才存在多个操作api
    # print(count)
    # 在进行查询的时候由于不知道数据量有多大应该先判断exists 也就是结果进行取first
    # if Book.objects.all().exists:
    #     count = Book.objects.all().count()
    #     print(count)
    # books_list = Book.objects.all().values('title','price')   # 就是对对象进行相应字段的拆分作为字典放在queryset中
    # print(books_list)
    # books_list = Book.objects.all().values_list('title', 'price') # 与values逻辑一致但是返回的数据结构是元祖而不是字典
    # print(books_list)
    # distinct() 该方法就是进行对queryset进行去重操作
    return HttpResponse('应该已经有了结果了')


# 使用include模板方法 包含的html不用是完整的 局部代码即可
def test_include(request):
    return render(request, 'test_include.html')


# 使用extends来进行继承base页面 当前页面只写入局部代码即可
# 一定要在第一行进行extends文件 并且使用block 和 endblock
def test_extends(request):
    return render(request, 'extends_base.html')


def many_to(request):
    # AuthorDetail.objects.get_or_create(gf='唐安娜', tel=1314)
    # ad_obj = AuthorDetail.objects.create(gf='唐安娜', tel=1314)
    # print(type(ad_obj))
    # au_obj = Author.objects.create(name='hong', age=25, ad=ad_obj)
    # print(au_obj)
    # book = Book.objects.get_or_create(title='西游记',price=100, pub_date='1990-02-22', publish_id=2)
    # print(book)
    # book = Book.objects.create(title='python', price=221, pub_date='2019-09-22', publish_id=1)
    # aus = Author.objects.all()[:2]
    # book.authors.add(aus[0],aus[1])
    # 通过get_or_create方法返回的是一个tuple第一个是对象第二个是是否成功
    # book = Book.objects.get_or_create(title='java', price=33, pub_date='2001-03-22', publish_id=2)
    # print(book, type(book[0]))
    # ret =Book.objects.all().aggregate(Min('price'))
    # print(ret.get('price__min'))
    # print(type(ret))
    res = Book.objects.all().aggregate(price=Avg('price'))
    print(res.get('price'))
    # 多对多中存在的方法 add在第三张表添加关系 remove移除指定关系 clear清空关系 set清空关系并设置关系（[列表内是关系对象])
    return HttpResponse('ok')


def test_annotate(request):
    # ret = Emp.objects.all().values('dep').annotate(price=Max('salary'))
    # print(ret)
    ret = Publish.objects.values("id").annotate(avg=Avg("book__price")).values("name","avg")
    print(ret)
    return HttpResponse('no no no')


# F就是能够直接获取对应参数的值并且计算作为参数值  Q就是增强筛选括起来之后可以使用 & | ~ 与或非
def test_f_q(request):
    return  HttpResponse('f  q')


def test_son_select(request):
    # book = Book.objects.filter(id=3).first()
    # print(book.price)
    # print(book.authors.all())
    # print(book.publish)

    # 主要是针对一对多情况的 正向查（从表存在该字段）和反向查（没有该字段使用从表名_set.all()获取全部数据）
    # 查询西游记这本书的出版社的名字
    # book = Book.objects.filter(title='西游记').first()
    # name = book.publish.name
    # print(name)
    # print(Book.objects.filter(title='python').first().publish.name)
    # name =Publish.objects.filter(book__title='西游记').values('name')
    # print(name)
    # 查询与西瓜出版社关联的所有书籍的名字
    publish = Publish.objects.filter(name='榴莲出版社').first()
    name = publish.book_set.all().values_list('title')
    print(name)
    return HttpResponse('over')


def test_manytomany(request):
    # 查询西游记这本书籍的所有作者的姓名和年龄
    # result = Book.objects.filter(title='西游记').first().authors.all().values('name','age')
    # print(result)
    # book = Book.objects.filter(title='西游记').first()
    # print(book)
    # result = book.authors.all().values('name', 'age')
    # print(result)
    # print(type(Book.objects.filter(title='西游记').first().authors))
    # result = Author.objects.filter(book__title='西游记').values('name', 'age')
    # print(result)

    # 查询作者xiao出版过的所有书籍名称
    result = Author.objects.filter(name='hong').first().book_set.all().values('title')
    print(result)
    return HttpResponse('many to many')


def test_onetoone(request):
    '''

    由于是一对一的关系所以不存在_set拼接且用all获取 直接获取的是对象进行.属性即可
    :param request:
    :return:
    '''

    # 查询hong的女朋友的名字
    # gf_name = Author.objects.filter(name='hong').first().ad.gf
    # print(gf_name)
    # 查询手机号为112的作者名字
    author_name = AuthorDetail.objects.filter(tel='13145').first().author.name
    au_name = AuthorDetail.objects.filter(tel='13145').values('author__name')
    print(author_name)
    print(au_name)
    return HttpResponse('test one to one')


def test_jointable(request):
    # 查询榴莲出版社出版过的所有书籍的名字以及作者的姓名
    # result = Publish.objects.filter(name__contains='榴莲出版社').values_list('book__title', 'book__authors__name')
    # print(result)
    # 查询每一本书籍的名称以及作者个数 分组后再进行filter使用的是having
    result = Book.objects.values('id').annotate(count=Count('authors__id')).filter(count__gt=1).values('title','count')
    print(result)
    return HttpResponse('test join table')


def test_ajax(request):
    return render(request, 'test_ajax.html')


def get_date(request):
    return HttpResponse('群山淡景')


def test_session_index(request):
    print(request.session.get('is_login'))
    if request.session.get('is_login'):
        username = request.session['username']
        login_time = request.session['login_time']
        print(login_time)
        obj = {'u':username, 'l':login_time}
        return render(request, 'index.html', {'obj':obj})
    url = reverse('session_login')
    return redirect(url)


def test_session_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        if username == 'mqy' and password == '123456':
            request.session['username'] = username
            request.session['login_time'] = str(datetime.datetime.now())
            request.session['is_login'] = True
            url = reverse('session_index')
            print(url)
            return redirect(url)
    return render(request, 'login.html')


def show_ajax(request):
    return render(request, 'test_js_add.html')


def test_add(request):
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        print(a,b)
        c = int(a)+int(b)
    elif request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = int(a) + int(b)
    return HttpResponse(str(c))


def new_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_is = UserInfo.objects.filter(user=user)
        if user_is:
            user = user_is[0]
            print(user.pwd)
            if pwd == user.pwd:
                return HttpResponse(json.dumps(user.user))
        else:
            return HttpResponse(json.dumps('账号或密码错误'))
    return render(request, 'new_login.html')


def test_form(request):
    userInfo = UiForm(request.POST)
    if request.method == 'POST':
        if userInfo.is_valid():
            data = userInfo.cleaned_data
            print(data)
        return HttpResponse('ok')
    return render(request, 'test_form.html', {'userinfo':userInfo})


# django.contrib.auth 主要提供 auth.authenticate（username,password） 获取查询对象
# 通过auth.login(request,user) 将关系绑定成session形式 全局变量request.user
# 通过auth.is_authenticated 属性来判断是否检测成功
# 通过auth.logout(request) 对该请求记录进行清除类似:session.flush()
def test_auth(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        ret = auth.authenticate(username=user,password=pwd)
        if ret:
            auth.login(request,ret)  # 绑定到session且request.ret直接获取
            url = reverse('test_auth_index')
            return redirect(url)
    return render(request, 'login.html')


def test_auth_index(request):
    if request.user.is_authenticated:
        print(type(request.user))
        username = request.user.username  # 获取的时候就是直接对象点即可可以当做user对象获取相应属性
        return render(request, 'index.html', {'username':username})
    url = reverse('test_auth')
    return redirect(url)


def test_auth_logout(request):
    auth.logout(request)  # 解除这种绑定关系
    url = reverse('test_auth')
    return redirect(url)


# 通过bulk_create接收对象列表可快速创建
def test_bulk_create(request):
    user_list = []
    for i in range(100):
            user = 'mqy{}'.format(i)
            user_list.append(UserInfo(user=user, pwd='123456'))
    UserInfo.objects.bulk_create(user_list)
    return HttpResponse('ok')


def test_paginator(request):
    users = UserInfo.objects.all()
    paginator = Paginator(users,10)
    data_obj = paginator.page(2)  # 返回的是第2页所有数据对象
    print(paginator.count)  # 返回所有的数据数
    print(paginator.num_pages)  # 返回多少页数
    print(paginator.page_range)  # 返回一个range(1,21)
    return render(request, 'show_paginator.html', {'users': data_obj})
