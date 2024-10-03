from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CarsPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cars_posts'
    verbose_name = _("Cars Posts")

    def ready(self):
        import apps.cars_posts.signals