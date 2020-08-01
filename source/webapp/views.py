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
                email=form.cleaned_data['email']
            )
            return redirect('index')
        else:
            return render(request, 'book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def book_update_view(request, pk):
    book = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        form = BookForms(initial={
            'email': book.email,
            'text': book.text,
            'author': book.author
        })
        return render(request, 'book_update.html', context={
            'form': form,
            'book': book
        })
    elif request.method == 'POST':
        form = BookForms(data=request.POST)
        if form.is_valid():
            book.email = form.cleaned_data['email']
            book.text = form.cleaned_data['text']
            book.author = form.cleaned_data['author']
            book.save()
            return redirect('index')
        else:
            return render(request, 'book_update.html', context={
                'book': book,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def book_delete_view(request, pk):
    book = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')



