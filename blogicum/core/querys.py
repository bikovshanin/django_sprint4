from django.db.models import Count
from django.utils import timezone as tz

from blog.models import Post


def full_query_set():
    return Post.objects.select_related(
        'location',
        'author',
        'category'
    ).annotate(comment_count=Count('comments')).order_by('-pub_date')


def post_query_set():
    return full_query_set().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=tz.now(),
    )
