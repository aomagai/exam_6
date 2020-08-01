from webapp.models import Guestbook
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForms, BROWSER_DATETIME_FORMAT
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Guestbook.objects.all()
    else:
        data = Guestbook.objects.filter(status='active')
    return render(request, 'index.html', context={
        'books': data
    })

def book_view(request, pk):
    book = get_object_or_404(Guestbook, pk=pk)
    context = {'book': book}
    return render(request, 'book_view.html', context)


def book_create_view(request):
    if request.method == "GET":
        form = BookForms()
        return render(request, 'book_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = BookForms(data=request.POST)
        if form.is_valid():
            book = Guestbook.objects.create(
                text=form.cleaned_data['text'],
                author=form.cleaned_data['author'],
                status=form.cleaned_data['status'],
            )
            return redirect('book_view', pk=book.pk)
        else:
            return render(request, 'book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def article_update_view(request, pk):
    book = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        form = BookForms(initial={
            'title': book.title,
            'text': book.text,
            'author': book.author,
            'status': book.status,
            'publish_at': make_naive(book.publish_at)\
                .strftime(BROWSER_DATETIME_FORMAT)
        })
        return render(request, 'book_update.html', context={
            'form': form,
            'article': book
        })
    elif request.method == 'POST':
        form = BookForms(data=request.POST)
        if form.is_valid():
            # Article.objects.filter(pk=pk).update(**form.cleaned_data)
            book.title = form.cleaned_data['title']
            book.text = form.cleaned_data['text']
            book.author = form.cleaned_data['author']
            book.status = form.cleaned_data['status']
            book.publish_at = form.cleaned_data['publish_at']
            book.save()
            return redirect('book_view', pk=book.pk)
        else:
            return render(request, 'book_update.html', context={
                'book': book,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])