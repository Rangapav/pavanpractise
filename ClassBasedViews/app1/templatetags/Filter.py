from django import template
register=template.Library()
@register.filter(name = 'pavan')
def pavan(value):
    y=value[:5].upper()
    return y
#     register.filter("myname",pavan)


@register.filter(name ='kalyan')
def proAppend(value,arg):
    x = str(arg)+value
    return x
