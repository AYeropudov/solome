from django.db import models
from posuda import urls


def show_urls(urllist, depth=0):
    return set([(entry.name, entry.name) for entry in urllist if entry.name is not None])


class SemanticKernel(models.Model):
    pattern = models.CharField(max_length=200, choices=show_urls(urllist=urls.urlpatterns), blank=True, default=None)
    base = models.BooleanField(default=False)
    append_base = models.BooleanField(default=True)

    title = models.TextField(blank=True, default=None)
    description = models.TextField(blank=True, default=None)
    keywords = models.TextField(blank=True, default=None)

    def __str__(self):
        base = "По умолчанию"
        if self.base:
            return "{} - {}".format(self.pattern, base)
        return "{}".format(self.pattern)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Семантическое ядро"

