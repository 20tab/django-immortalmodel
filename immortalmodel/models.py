from django.db import models
from django.utils.translation import ugettext_lazy as _


class ImmortalQuerySet(models.query.QuerySet):
    """
    Represents a lazy database lookup for a set of objects.
    It updates "deleted" attribute instead deleting items.
    """
    def delete(self):
        self.update(deleted=True)


class ImmortalManager(models.Manager):
    def get_queryset(self):
        """
        Returns a new QuerySet object.  Subclasses can override this method
        to easily customize the behavior of the Manager.
        It filters by "deleted" attribute.
        """
        return ImmortalQuerySet(self.model, using=self._db).filter(deleted=False)

    get_query_set = get_queryset


class ImmortalModel(models.Model):
    """
    Implementation of undeletable model
    """
    deleted = models.BooleanField(_('deleted'), default=False)

    objects = ImmortalManager()
    baseobjects = models.Manager()

    def delete(self, using=None, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True