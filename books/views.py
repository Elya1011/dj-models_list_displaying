from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.order_by('-pub_date')
    context = {'books': books}
    return render(request, template, context)

def show_book(request, pub_date):
    template = 'books/books_by_date.html'
    books = Book.objects.order_by('-pub_date')
    context = {}
    date_list = []
    for book in books:
        date_list.append(str(book.pub_date))
    paginator = Paginator(date_list, 1)
    page_number = 1
    for index, date in enumerate(date_list):
        if date == pub_date:
            page_number = index + 1
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['pub_date'] = pub_date
    context['books'] = []
    if page_obj.has_previous():
        context['prev_page'] = date_list[page_obj.previous_page_number() - 1]
    if page_obj.has_next():
        context['next_page'] = date_list[page_obj.next_page_number() - 1]
    for book in books:
        if str(book.pub_date) == pub_date:
            context['books'].append(book)
    return render(request, template, context)