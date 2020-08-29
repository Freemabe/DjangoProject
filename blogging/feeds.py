from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
from django.template.defaultfilters import truncatewords

class LatestEntriesFeed(Feed):
    title = "Most recent blogs"
    link = "/sitenews/"
    description = "Updates the blog."

    def items(self):
        return Post.objects.order_by('published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.text, 30)

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])