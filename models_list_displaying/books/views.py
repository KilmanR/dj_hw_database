from django.shortcuts import render, get_object_or_404  # noqa: F401
from django.db.models import Min, Max  # noqa: F401
from .models import Book
from datetime import datetime


def books_view(request):
    template = "books/books_list.html"
    books = Book.objects.all().order_by("pub_date")
    context = {"books": books}
    return render(request, template, context)


def books_by_date_view(request, pub_date):
    template = "books/books_list.html"
    pub_date_obj = datetime.strptime(pub_date, "%Y-%m-%d").date()
    books = Book.objects.filter(pub_date=pub_date_obj).order_by("pub_date")
    
    previous_date = (
        Book.objects.filter(pub_date__lt=pub_date_obj)
        .order_by("-pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )

    next_date = (
        Book.objects.filter(pub_date__gt=pub_date_obj)
        .order_by("pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )

    context = {
        "books": books,
        "pub_date": pub_date_obj,
        "previous_date": previous_date,
        "next_date": next_date,
    }
    return render(request, template, context)
