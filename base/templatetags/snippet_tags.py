from django import template

from wagtail.core.models import Page

from base.models import FooterText, RawHtml

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('tags/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.all()

    return {
        'footer_text': footer_text,
    }


# Advert snippets
@register.inclusion_tag('tags/rawhtml.html', takes_context=True)
def rawhtml(context):
    return {
        'raw_html': RawHtml.objects.all(),
        'request': context['request'],
    }
