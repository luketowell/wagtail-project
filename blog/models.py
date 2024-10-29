from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField

# Create your models here.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    api_fields = [
        APIField('intro')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ["blog.BlogPage"]

class BlogPage(Page):
    date = models.DateField("Post Date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    api_fields = [
        APIField('date'),
        APIField('intro'),
        APIField('body')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    parent_page_types = ["blog.BlogIndexPage"]