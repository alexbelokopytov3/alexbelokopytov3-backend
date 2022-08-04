from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='add_class_and_type')
def add_class_and_type(value, arg0, arg1):
    return value.as_widget(attrs={'class': arg0, 'type': arg1})