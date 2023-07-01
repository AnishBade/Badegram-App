from django.apps import AppConfig

# Register your models here.
class PostConfig(AppConfig):
    default_auto_field ='django.db.models.BigAutoField'
    name = 'core.post'
    label = "core_post"