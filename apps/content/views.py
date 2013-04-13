# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from . import models

def single_entry(request, slug):
    
    entry = get_object_or_404(models.Entry, slug=slug)
    
    return render_to_response(
        'content/template.single_entry.html',
        {'entry': entry},
        context_instance=RequestContext(request)
        )


def list_view(request, tag_slug=None):
    
    if tag_slug is not None:
        #single tag
        tag = get_object_or_404(models.Tag, slug=tag_slug)
        entries = tag.entry_set.filter(is_published=True)
        page_title = tag.tag
    else:
        #home page
        entries = models.Entry.objects.filter(is_published=True, include_on_front_page=True)
        page_title = ''
    
    column = 1
    entries_by_column = []
    columns = [1,2,3,4]
    for entry in entries:
        entries_by_column.append({'entry'   : entry, 
                                  'column'  : column})
        
        if column < len(columns): 
            column += 1 
        else: 
            column = 1;
    
    return render_to_response(
        'content/template.list.html',
        {'entries_by_column': entries_by_column,
         'columns'  :   columns,
         'entries' : entries,
         'page_title' : page_title
         },
        context_instance=RequestContext(request)
        )
