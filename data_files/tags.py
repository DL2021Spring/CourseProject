from django import template
import markdown2

register = template.Library()


@register.simple_tag(takes_context=True)
def some_tags(context):
  pass


@register.filter
def markdownify(text):
  
  return markdown2.markdown(text, extras=["fenced-code-blocks"], safe_mode=None)
