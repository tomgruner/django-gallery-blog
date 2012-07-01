from . import models

def tags(request):
    
    return {'tag_list': models.Tag.objects.filter(show_in_tag_list = True)}