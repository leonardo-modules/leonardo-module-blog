
import six
from django.utils.translation import ugettext_lazy as _
from elephantblog.models import Entry
from importlib import import_module
from leonardo.module import media, web

from .widget.blogcategories.models import BlogCategoriesWidget
from .widget.recentblogposts.models import RecentBlogPostsWidget

Entry.register_extensions('leonardo.extensions.datepublisher',
                          'leonardo.extensions.translations',
                          )

REGIONS = ('preview', 'main',)

Entry.register_regions(
    ('preview', _('Preview content area')),
    ('main', _('Main content area')),
)


def get_class_from_string(widget):
    mod = '.'.join(widget.split('.')[0:-1])
    cls_name = widget.split('.')[-1]
    return getattr(import_module(mod), cls_name)

Entry.create_content_type(
    web.models.HtmlTextWidget, regions=REGIONS, optgroup=_('Text'))
Entry.create_content_type(
    web.models.MarkupTextWidget, regions=REGIONS, optgroup=_('Text'))

for widget in media.default.widgets:
    if isinstance(widget, six.string_types):
        widget = get_class_from_string(widget)
    Entry.create_content_type(widget, regions=REGIONS, optgroup=_('Media'))

try:
    from leonardo_oembed.models import OembedWidget
    Entry.create_content_type(OembedWidget,
                              regions=REGIONS, optgroup=_('External content'))
except:
    pass
