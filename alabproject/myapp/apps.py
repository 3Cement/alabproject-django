# myapp/apps.py
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    Configuration class for the 'myapp' application.

    Attributes:
    - default_auto_field (str): The default field to use for automatically created fields.
    - name (str): The name of the application.
    - verbose_name (str): A human-readable name for the application displayed in the Django admin.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"
    verbose_name = "Aplikacja z wynikami testów laboratoryjnych"
