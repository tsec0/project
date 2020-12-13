from django.contrib import admin

from pets.models import Pet, Like, Comment, Sell


class SoldInline(admin.TabularInline):
    model = Sell


class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = (
        LikeInline,
        SoldInline,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Sell)