import os
from dynaconf import settings

print (os.environ['ENV_FOR_DYNACONF'])
if settings.DEBUG is True:
    print(settings.NAME)
else:
    print(settings.KEY)
    print(settings.TOKEN)