
from django.utils.translation import ugettext_lazy as _
from elephantblog.models import Entry
from leonardo.module import media, web

Entry.register_extensions('feincms.module.extensions.datepublisher',
                          'feincms.module.extensions.translations',
                          )
Entry.register_regions(
    ('main', _('Main content area')),
)

Entry.create_content_type(
    web.widget.HtmlTextWidget, regions=('main',), optgroup=_('Text'))
Entry.create_content_type(
    web.widget.MarkupTextWidget, regions=('main',), optgroup=_('Text'))

for widget in media.default.widgets:
    Entry.create_content_type(widget, regions=('main',), optgroup=_('Media'))
