from django import template
from ..models import BlockArea

register = template.Library()

def render_block_area(context, block_area_name):
	
	block_area = BlockArea.objects.get(key=block_area_name)
	return block_area.render(context)

register.simple_tag(render_block_area, takes_context=True)
  