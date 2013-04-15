from django.db import models
from django.template.loader import get_template
from django.template import Context
from ..content import models as content_models

class Menu(models.Model):
    STYLES = (('black', 'Black'),
              ('orange', 'Orange'),)
    
    title = models.CharField(max_length=40)
    style = models.CharField(max_length=40, choices=STYLES)
    show_title = models.BooleanField(default=True, help_text="Show the title above the menu?")
    
    def item_count(self):
        return self.menuitem_set.count()
    
    def render(self, context):
        c = Context({'menu' : self})
        return get_template('layout/menu.html').render(c)
    
    def __unicode__(self):
        return unicode(self.title)
    
class MenuItem(models.Model):
   
    LINK_TYPE_CHOICES = (
        ('custom', 'Custom link'),
        ('tag', 'Link to tag'),
        ('entry', 'Link to entry'),
    )
   
    TARGET_CHOICES = (
        ('_blank', 'Open in a new window'),
        ('_self', 'Open in the same window'),
    )
    
    order   = models.IntegerField()
    text    = models.CharField(max_length=1000)
    target  = models.CharField(max_length=50, choices=TARGET_CHOICES, default='_self')
    link_type = models.CharField(choices=LINK_TYPE_CHOICES, max_length=50, default='custom')
    custom_link =models.URLField(blank=True)
    link_to_entry = models.ForeignKey(content_models.Entry, blank=True, null=True)
    link_to_tag = models.ForeignKey(content_models.Tag, blank=True, null=True)

    menu = models.ForeignKey(Menu)
    
    def links_to(self):
        if self.link_type == 'none':
            return ''
        if self.link_type == 'custom':
            return self.custom_link
        if self.link_type == 'entry':
            return self.link_to_entry.get_absolute_url()
        
        
    
        
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ['order']


class BlockArea(models.Model):
    key = models.CharField(max_length=100)

    def render(self, context):
        html = ''
        for block in self.block_set.all():
            html += '<div class="block">' + block.render(context) + '</div>'
        
        return html
    
class Block(models.Model):
    
    TYPES = (('html', 'HTML Block'),
             ('tag_list', 'Tag List'),
             ('menu', 'Menu Block'))
    
    block_area = models.ForeignKey(BlockArea)
    
    block_type = models.CharField(choices=TYPES, max_length=30)
    
    html = models.TextField(blank=True, null=True)
    
    menu = models.ForeignKey(Menu,blank=True, null=True)
    
    order = models.IntegerField()
    
    def render(self, context):
        if self.block_type == 'html':
            return self.html
        elif self.block_type == 'tag_list':
            context.tag_list = ""
            return content_models.Tag.render_list(context=context)
        elif self.block_type == 'menu':
            return self.menu.render(context=context)
       
    def __unicode__(self):
        if self.block_type == 'html':
            return 'HTML'
        elif self.block_type == 'tag_list':
            return 'Tag List'
        elif self.block_type == 'menu':
            return 'Menu - ' + self.menu.title 
    
    class Meta:
        ordering = ['order',]
