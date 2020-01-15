from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, IntegerBlock
)

from wagtail.snippets.blocks import SnippetChooserBlock

from django.db import models


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    position = ChoiceBlock(
        choices=[
            ('', '- Change Alignment -'),
            ('left', 'Left'),
            ('right', 'Right'),
            ('center', 'Center'),
        ],
        required=False,
        blank=True
    )
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class BannerBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)

    class Meta:
        icon = 'image'
        template = "blocks/banner_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    size = ChoiceBlock(choices=[
        ('', 'Select a blockquote size'),
        ('short', 'Short'),
        ('long', 'Long'),
    ], blank=True, required=False)

    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


class CarouselBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to create a sequence of sub-blocks of different types, which can be mixed and reordered at will.
    """
    image = ImageChooserBlock()
    quotation = StructBlock(
        [
            ('text', TextBlock()),
            ('author', CharBlock())
        ]
    )

    video = EmbedBlock()

    class Meta:
        icon = "fa-images"
        template = "blocks/carousel_block.html"


class Carousel(StreamBlock):
    """
    Carousel contains carousel blocks, so that you can have multiple carousels on a page.
    """
    carousel_block = CarouselBlock()

    class Meta:
        icon = "fa-images"
        template = "blocks/carousel.html"


class ColumnBlock(StructBlock):
    """
    Define the blocks that all columns will utilize
    """
    background = ImageChooserBlock(
        required=False,
        help_text="This will set the background image of the row.",
        group="Container"
    )
    width = IntegerBlock(
        max_value=12,
        min_value=1,
        default=12,
        blank=True,
        required=False,
        help_text="Select the width of the column, max of 12.",
        group="Container"
    )

    padding = ChoiceBlock(
        choices=[
            ('', 'Select a padding size'),
            ('none', 'None'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        blank=True,
        required=False,
        help_text="Select how much top and bottom padding you would like on the row.",
        group="Container"
    )

    content = StreamBlock(
        [
            ('heading', HeadingBlock()),
            ('paragraph', RichTextBlock(
                icon="fa-paragraph",
                template="blocks/paragraph_block.html"
            )),
            ('carousel', Carousel()),
            ('image', ImageBlock()),
            ('banner', BannerBlock()),
            ('quote', BlockQuote()),
            ('heading', HeadingBlock()),
        ],
        help_text="Add content to column."
    )

    class Meta:
        icon = "fa-columns"
        template = "blocks/column.html"
        closed = True


class RowBlock(StructBlock):
    """
    Define the blocks that all rows will utilize
    """

    background = ImageChooserBlock(
        required=False,
        help_text="This will set the background image of the row.",
        group="Container"
    )

    padding = ChoiceBlock(
        choices=[
            ('', 'Select a padding size'),
            ('none', 'None'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        blank=True,
        required=False,
        help_text="Select how much top and bottom padding you would like on the row.",
        group="Container"
    )

    content = StreamBlock(
        [
            ('column', ColumnBlock()),
        ],
        help_text="Add column to row."
    )

    class Meta:
        icon = "fa-align-justify"
        template = "blocks/row.html"
        closed = True


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the blocks that all web pages will utilize
    """
    title = models.CharField(max_length=255,
                             null=True,
                             blank=True,)
    rows = RowBlock()
