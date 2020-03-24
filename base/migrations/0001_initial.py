# Generated by Django 3.0.4 on 2020-03-24 21:31

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', wagtail.core.fields.StreamField([('html', wagtail.core.blocks.RawHTMLBlock())], null=True, verbose_name='Add Snippet')),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='RawHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('text', wagtail.core.fields.StreamField([('html', wagtail.core.blocks.RawHTMLBlock())], verbose_name='Add Snippet')),
            ],
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, group='Container', help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', '- Change Alignment -'), ('left', 'Left'), ('right', 'Right'), ('center', 'Center')], required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('rawhtml', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.RawHtml', verbose_name='Add Snippet')),
                ('seo_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, group='Container', help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', '- Change Alignment -'), ('left', 'Left'), ('right', 'Right'), ('center', 'Center')], required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body')),
                ('seo_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(group='Container', help_text='This will set the background image of the row.', required=False)), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, group='Container', help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], group='Container', help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', '- Change Alignment -'), ('left', 'Left'), ('right', 'Right'), ('center', 'Center')], required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body')),
                ('rawhtml', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.RawHtml', verbose_name='Add Snippet')),
                ('seo_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
