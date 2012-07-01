from .models import BlockArea

class BlockAreaHelper:
    """A way to have lazy lookups
       since this is for a context processor
       and will be sent to every single view"""
    def __getattr__(self, name):
        try:
            obj = BlockArea.objects.get(key=name)
            return obj
        except:
            return super(BlockAreaHelper, self).__getattr__(name)
        
block_areas = BlockAreaHelper()

def block_areas_cp(request):
    """
       usage
       
       {% block_areas.main %}
           
    """
    return {'block_areas' : block_areas}