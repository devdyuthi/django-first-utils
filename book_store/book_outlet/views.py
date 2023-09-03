from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg


# Create your views here.


def index(request):
    books = Book.objects.all()
    num_books = books.count()
    average_rating = books.aaggregate(Avg())

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": num_books,
            "average_rating": average_rating,
        },
    )


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "best_selling": book.best_selling,
        },
    )
