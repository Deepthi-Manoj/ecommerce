from django import template
register = template.Library()
@register.simple_tag
def progress_percentage(value,total):
    percent=(value/total )* 100
    return percent