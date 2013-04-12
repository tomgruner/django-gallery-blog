from django.db import models
from django.template import Context
from django.template.loader import get_template
from sorl.thumbnail import ImageField


class Tag(models.Model):
    tag = models.CharField(
        max_length=100
        )
    
    slug = models.SlugField(
        max_length=100
        )

    show_in_tag_list = models.BooleanField(
        default = True
    )

    @staticmethod
    def render_list():
        
        c = Context({
            'tag_list' : Tag.objects.filter(show_in_tag_list = True)
            })
        
        t = get_template('content/tag.list.html')
        
        return t.render(c)

    def __unicode__(self):
        return unicode(self.tag)

class Image(models.Model):
    image       = ImageField(
        upload_to='images'
        )
    caption     = models.TextField(
        max_length=1000, 
        blank=True
        )
    entry       = models.ForeignKey(
        'Entry'
        )
    
    order = models.IntegerField()
    
    class Meta:
        ordering = ['order',]

# Create your models here.
class Entry(models.Model):
    title            = models.CharField(
        max_length=255
        )
    
    slug            = models.SlugField(
        max_length=255
        )
    
    preview_image    = ImageField(
        upload_to='images',
        blank=True,
        null=True
        )
    
    date = models.DateField(
        blank=True,
        null=True
    )
    
    is_published = models.BooleanField()
    
    include_on_front_page = models.BooleanField()
    
    tags = models.ManyToManyField(Tag, blank=True)
    
    main_content     = models.TextField(
        blank=True
        )
    
    seo_keywords     = models.CharField(
        max_length=255,
        help_text='A short list of words for Google that describe this entry, seperated by commas'
        )
    
    seo_description  = models.TextField(
        max_length=1000,
        help_text='A short description for Google'
        )
    
    def tag_list(self):
        return ", ".join(self.tags.values_list('tag', flat=True))

    def get_absolute_url(self):
        return '/' + self.slug
    
    def __unicode__(self):
        return unicode(self.title)
    
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'