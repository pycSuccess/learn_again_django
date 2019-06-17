from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models import Sum,Min,Max,Avg
# Create your views here.


from blog.models import Book
from blog.models import Emp
from blog.models import Publish


def index(request):
    num = 100
    return render(request, 'index.html', {'num':num})


def login(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        url = reverse('index')
        return redirect(url)
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
