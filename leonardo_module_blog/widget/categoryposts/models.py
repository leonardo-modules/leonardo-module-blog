# -#- coding: utf-8 -#-

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from elephantblog.models import Entry, Category
from leonardo.module.web.models import ListWidget


class CategoryPostsWidget(ListWidget):

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

    category = models.ForeignKey(Category, verbose_name=_('Category'))

    def get_items(self):
        entries = Entry.objects.active().order_by('-published_on')
        if self.featured_only:
          entries = entries.filter(is_featured=True)
        if self.only_active_language:
          lang = self.parent.language
          entries = entries.filter(language=lang)
        if self.category != None:
          entries = entries.filter(categories=self.category)
        if entries.count() > self.post_count:
          return entries[:self.post_count]
        else:
          return entries

    class Meta:
        abstract = True
        verbose_name = _("Category post")
        verbose_name_plural = _("Category posts")
