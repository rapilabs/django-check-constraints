from django.apps import AppConfig, apps
from django.db.models import options
from django.db import connections
from django.db import DEFAULT_DB_ALIAS


class DjangoCheckConstraintsConfig(AppConfig):
    name = 'django_check_constraints'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('check_constraints',)

    def ready(self):
        connection = connections['default']
        for model in apps.get_models():
            if hasattr(model._meta, 'check_constraints'):
                print('Found constraint on model {}: {}'.format(model._meta.object_name, model._meta.check_constraints))
                compiler = model.objects.all().query.get_compiler(DEFAULT_DB_ALIAS)
                print('sql: {}'.format(model._meta.check_constraints.as_sql(compiler, connection)))

