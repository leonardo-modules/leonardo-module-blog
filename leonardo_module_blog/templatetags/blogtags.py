
from django import template
from elephantblog.models import Entry

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_prev(context, same_category=False):
    """ This tag can be used on an entry detail page to tease
        other previous entry
    """
    prev_entry = Entry.objects.filter(
        published_on__lte=context['object'].published_on
    ).order_by('-published_on').exclude(pk=context['object'].pk).first()

    return prev_entry


@register.assignment_tag(takes_context=True)
def get_next(context, same_category=False):
    """ This tag can be used on an entry detail page to tease
        other previous entry
    """
    next_entry = Entry.objects.filter(
        published_on__gte=context['object'].published_on
    ).order_by('-published_on').exclude(pk=context['object'].pk).first()

    return next_entry
