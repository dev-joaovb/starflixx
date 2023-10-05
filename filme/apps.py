from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

class EpisodeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'episodios'
