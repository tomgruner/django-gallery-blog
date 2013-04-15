from django.contrib import admin
from django.conf import settings

from sorl.thumbnail.admin import AdminImageMixin

from . import models

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)} 
    list_display = ('tag', 'slug', 'show_in_tag_list')

class ImageInlineModelAdmin(AdminImageMixin, admin.TabularInline):
    model = models.Image
    extra = 0
    sortable_field_name = "order"

class EntryAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [ImageInlineModelAdmin]
    list_display = ('slug', 'title', 'tag_list', 'date', 'is_published', 'include_on_front_page')
    date_hierarchy = 'date'
    search_fields = ('title', 'seo_keywords', 'seo_description')
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '%sgrappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%sbase/js/tinymce_setup.js' % settings.STATIC_URL,
        ]
    

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag, TagAdmin)
