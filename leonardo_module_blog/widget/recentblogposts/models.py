# -#- coding: utf-8 -#-

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from elephantblog.models import Entry
from leonardo.module.web.models import ListWidget
from elephantblog.utils import entry_list_lookup_related

try:
    # Load paginator with additional goodies form towel if possible
    from towel.paginator import Paginator, EmptyPage, PageNotAnInteger
except ImportError:
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class RecentBlogPostsWidget(ListWidget):
    post_count = models.PositiveIntegerField(
        verbose_name=_("post count"), default=3)
    show_button = models.BooleanField(
        default=True, verbose_name=_("show link button"))

    featured_only = models.BooleanField(
        _('featured only'), blank=True, default=False,
        help_text=_('Only show articles marked as featured'))

    only_active_language = models.BooleanField(
        _('show only post with active language'), blank=True, default=False,
        help_text=_('Only show articles written in active language'))

    def get_last_posts(self):
        return Entry.objects.all().order_by('-published_on')[:self.post_count]

    def get_all_posts(self):
        return Entry.objects.filter(published_on__in=[50, 60]).order_by('-published_on')

    def render_content(self, options):
        request = options.get('request')
        context = {'widget': self, 'request': request}

        if self.featured_only:
            entries = Entry.objects.featured()
        else:
            entries = Entry.objects.active()

        if self.only_active_language:
            entries = entries.filter(
                language=get_language())

        entries = entries.transform(entry_list_lookup_related)

        if self.post_count:
            paginator = Paginator(entries, self.post_count)
            page = request.GET.get('page', 1)
            try:
                self.entries = paginator.page(page)
            except PageNotAnInteger:
                self.entries = paginator.page(1)
            except EmptyPage:
                self.entries = paginator.page(paginator.num_pages)

        else:
            self.entries = entries

        context['entries'] = self.entries

        return render_to_string(self.get_template, context)

    class Meta:
        abstract = True
        verbose_name = _("recent blog posts")
        verbose_name_plural = _("recent blog posts")
