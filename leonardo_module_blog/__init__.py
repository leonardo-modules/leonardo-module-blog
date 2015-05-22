
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *


default_app_config = 'leonardo_module_blog.BlogConfig'


class Default(object):

    optgroup = ('Blog')

    @property
    def apps(self):
        return [
            'leonardo_module_blog',
            'elephantblog',

        ]

    @property
    def widgets(self):
        return [
            BlogCategoriesWidget,
            RecentBlogPostsWidget,
        ]

    @property
    def plugins(self):
        return [
            ('elephantblog.urls', 'Blog entries'),
        ]

    config = {
        'BLOG_PAGINATE_BY': (10, _('Blog Entries Pagination')),
        'DISQUS_COMMENTS': (False, _('Enable Disqus comments')),
        'DISQUS_SHORTNAME': ('michaelkuty', _('Disqus shortname identificator.')),

    }

    navigation_extensions = [
        'elephantblog.navigation_extensions.treeinfo',
    ]

    absolute_url_overrides = {
        'elephantblog.entry': 'leonardo_module_blog.overrides.elephantblog_entry_url_app',
        'elephantblog.categorytranslation':
        'leonardo_module_blog.overrides.elephantblog_categorytranslation_url_app',
    }


class BlogConfig(AppConfig, Default):
    name = 'leonardo_module_blog'
    verbose_name = ("Blog")

default = Default()
