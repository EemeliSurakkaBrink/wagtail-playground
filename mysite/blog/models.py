# Blog app models that define the page types for a simple blog functionality.
# BlogIndexPage serves as the main blog listing page, while BlogPage represents individual blog posts.
# Each blog post includes a date, intro text, and rich text body with search capabilities.

from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + ["intro"]


class BlogPage(Page):
    
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    intro = RichTextField(blank=True)
    
    # add the get_context method:
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + ["date", "intro", "body"]