
from django.apps import AppConfig

from .widget import *


default_app_config = 'leonardo.module.blog.BlogConfig'


class Default(object):

    optgroup = ('Blog')

    @property
    def apps(self):
        return [
            'leonardo.module.blog',
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
            ('elephantblog.urls', 'Blog'),
        ]


class BlogConfig(AppConfig, Default):
    name = 'leonardo.module.blog'
    verbose_name = ("Blog")

default = Default()
