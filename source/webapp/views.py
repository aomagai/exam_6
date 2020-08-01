from webapp.models import Guestbook
from django.shortcuts import render, redirect, get_object_or_404

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