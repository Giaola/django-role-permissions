import django
from distutils.version import StrictVersion


__version__ = '1.2.3'


try:
    dj_version = StrictVersion(django.get_version())
except:
    dj_version = StrictVersion('1.10')


if dj_version < StrictVersion('1.7'):
    from giaola_role_permissions.loader import load_roles_and_permissions
    load_roles_and_permissions()
else:
    default_app_config = 'giaola_role_permissions.apps.RolePermissions'
