
def elephantblog_entry_url_app(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'elephantblog_entry_detail',
        'elephantblog.urls',
        kwargs={
            'year': self.published_on.strftime('%Y'),
            'month': self.published_on.strftime('%m'),
            'day': self.published_on.strftime('%d'),
            'slug': self.slug,
        })


def elephantblog_categorytranslation_url_app(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'elephantblog_category_detail',
        'elephantblog.urls',
        kwargs={
            'slug': self.slug,
        })
