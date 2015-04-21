
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *


default_app_config = 'leonardo_module_blog.BlogConfig'


class Default(object):

    optgroup = _('Blog')

    @property
    def apps(self):
        return [
            'elephantblog',
            'leonardo_module_blog',

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
    name = 'leonardo_module_blog'
    verbose_name = _("Blog")

default = Default()
