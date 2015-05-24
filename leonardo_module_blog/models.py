
from django.utils.translation import ugettext_lazy as _
from elephantblog.models import Entry
from leonardo.module import media, web

Entry.register_extensions('feincms.module.extensions.datepublisher',
                          'feincms.module.extensions.translations',
                          )

REGIONS = ('preview', 'main',)

Entry.register_regions(
    ('preview', _('Preview content area')),
    ('main', _('Main content area')),
)

Entry.create_content_type(
    web.widget.HtmlTextWidget, regions=REGIONS, optgroup=_('Text'))
Entry.create_content_type(
    web.widget.MarkupTextWidget, regions=REGIONS, optgroup=_('Text'))

for widget in media.default.widgets:
    Entry.create_content_type(widget, regions=REGIONS, optgroup=_('Media'))

try:
    from leonardo_oembed.widget import OembedWidget
    Entry.create_content_type(OembedWidget,
                              regions=REGIONS, optgroup=_('External content'))
except:
    pass
