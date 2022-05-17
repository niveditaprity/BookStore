from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from books.models import Book,Review
import json

from django.contrib.auth.mixins import LoginRequiredMixin

loadData= open('/Users/NiveditaKumari/Documents/Nivedita/Django/bookstore/books/books.json').read()
bookData=json.loads(loadData)
# Create your views here.

class BookListView(ListView):
    model=Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


# def index(request):
#     bookData=Book.objects.all()
#     context={'books':bookData}
#     return render(request,'books/index.html',context)

class BookDetailView(DetailView):
    model=Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews']= context['book'].review_set.all()
        context['authors']= context['book'].author.all()
        return context


# def show(request,id):
#     try:
#         singleBook=Book.objects.get(pk=id)
#         reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")

#     context={'book':singleBook,'reviews':reviews}
#     return render(request,'books/show.html',context)


def review(request,id):
    body=request.POST['review']
    newreview = Review(body=body,book_id=id)
    newreview.save()
    return redirect('/booksapp/books')

def author(request,author):
    books =Book.objects.filter(author__name=author)
    context={'books':books}
    return render(request,'books/book_list.html',context)
