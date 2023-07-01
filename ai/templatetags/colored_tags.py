from django import template


register = template.Library()


@register.filter(name='ColoredTags')
def color_plot(tags):
    for tag in tags:
        print(tag)