from django.contrib import admin
from webapp.models import Guestbook


class GuestPostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'email', 'text', 'created_at', 'status')
    list_display_links = ('pk', 'author')
    list_filter = ('author',)
    search_fields = ('author',)


admin.site.register(Guestbook, GuestPostAdmin)