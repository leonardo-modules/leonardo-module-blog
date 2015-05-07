from haystack import indexes, fields

from elephantblog.models import Entry


class EntryIndex(indexes.SearchIndex, indexes.Indexable):

    url = fields.CharField(model_attr="get_absolute_url")
    text = fields.CharField(document=True, use_template=True)

    title = fields.CharField(model_attr="title")
    slug = fields.CharField(model_attr="slug")
    author = fields.CharField(model_attr="author")
    content = fields.CharField(model_attr="content")

    published_on = fields.DateTimeField(model_attr='published_on', null=True)
    last_changed = fields.DateTimeField(model_attr='last_changed', null=True)

    def should_update(self, instance, **kwargs):
        return instance.is_active()

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(is_active=True)

    def get_updated_field(self):
        return "last_changed"
