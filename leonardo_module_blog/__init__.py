
from django.apps import AppConfig

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

    navigation_extensions = [
        'elephantblog.navigation_extensions.treeinfo',
        'elephantblog.navigation_extensions.common',
        'elephantblog.navigation_extensions.recursetree',
    ]


class BlogConfig(AppConfig, Default):
    name = 'leonardo_module_blog'
    verbose_name = ("Blog")

default = Default()
