from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import RawHTMLBlock
from wagtail.snippets.models import register_snippet

from wagtail.snippets.edit_handlers import SnippetChooserPanel


# Import from other custom modules
from five import blocks


@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    text = StreamField([
        ('html', RawHTMLBlock(),),
    ], verbose_name="Add Snippet", null=True)

    panels = [
        StreamFieldPanel('text'),
    ]

    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name = 'Footer'


@register_snippet
class RawHtml(models.Model):
    title = models.CharField(max_length=255,
                             null=True,
                             blank=True,)

    text = StreamField([
        ('html', RawHTMLBlock()),
    ], verbose_name="Add Snippet")

    panels = [
        FieldPanel('title'),
        StreamFieldPanel('text'),
    ]

    def __str__(self):
        return self.title


class HomePage(Page):
    """
    Custom Homepage
    """
    is_creatable = False

    body = StreamField(
        blocks.BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    seo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('seo_image'),
    ]


def get_context(self, request, *args, **kwargs):
    context = super(HomePage, self).get_context(request, *args, **kwargs)
    context['posts'] = self.posts
    context['homepage_page'] = self

    context['menuitems'] = self.get_children().filter(
        live=True, show_in_menus=True)

    return context


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    seo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    body = StreamField(
        blocks.BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('seo_image'),
    ]


class ContactPage(Page):
    """
    Custom Contact page
    """
    is_creatable = False

    body = StreamField(
        blocks.BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    rawhtml = models.ForeignKey(
        'base.RawHtml',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Add Snippet"
    )

    seo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        SnippetChooserPanel('rawhtml'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('seo_image'),
    ]
