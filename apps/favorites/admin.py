from django.contrib import admin

from apps.favorites.models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post')

admin.site.register(Favorite, FavoriteAdmin)
