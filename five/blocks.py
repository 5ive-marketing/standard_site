from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock
)


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
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
        icon = "fa-image"
        template = "blocks/carousel_block.html"


class Carousel(StreamBlock):
    """
    Carousel contains carousel blocks, so that you can have multiple carousels on a page.
    """
    carousel_block = CarouselBlock()

    class Meta:
        icon = "fa-images"
        template = "blocks/carousel.html"


class ColumnBlock(StreamBlock):
    """
    Define the blocks that all columns will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html"
    )
    carousel_block = Carousel()
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        template="blocks/embed_block.html")

    class Meta:
        icon = "fa-images"
        # template = "blocks/column.html"


class RowBlock(StreamBlock):
    """
    Define the blocks that all rows will utilize
    """
    column = ColumnBlock()

    class Meta:
        icon = "fa-images"
        template = "blocks/row.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the blocks that all web pages will utilize
    """
    rows = RowBlock()

    class Meta:
        icon = 'fa-stream'
