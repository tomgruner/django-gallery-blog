from django.contrib import admin


from . import models


class MenuItemStackedModelAdmin(admin.StackedInline):
    model = models.MenuItem
    sortable_field_name = "order"
    raw_id_fields = ('link_to_entry',)
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display=('title', 'item_count')
    inlines = [MenuItemStackedModelAdmin,]
    
    

class BlockStackedInlineModelAdmin(admin.StackedInline):
    model = models.Block
    sortable_field_name = "order"
    extra = 0


class BlockAreaAdmin(admin.ModelAdmin):
    list_display=('key',)
    inlines = [BlockStackedInlineModelAdmin,]
        

admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.BlockArea, BlockAreaAdmin)