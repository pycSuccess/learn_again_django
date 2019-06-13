from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.


from blog.models import Book


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
    book = Book(title='放风的人', price='11.22', pub_date='2019-11-11', publish='苹果出版社', state=False)
    book.save()
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
