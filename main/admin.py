from django.contrib import admin
from .models import Comment, Category, Product, Slider, SupterSlider, Blog, Contacts

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Slider)
admin.site.register(SupterSlider)
admin.site.register(Blog)
admin.site.register(Contacts)
admin.site.register(Comment)
