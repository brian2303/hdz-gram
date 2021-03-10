from django.contrib.auth.models import User
from django.db import models

"""
    CONFIGURAR DJANGO PARA QUE SIRVA ARCHIVOS MEDIA

    Django por defecto no esta preparado para servir
    archivos estaticos pero para configurarlo para que
    pueda servir imagenes o videos debemos realizar los
    siguientes pasos

    1. Cuando creemos el campo que va tener una imagen debemos
        con el atributo upload_to='path/where/upload/file/'

    2. Debemos en el archivo principal de urls.py indicarle
        cual configurar las rutas para que aparte de buscar
        las rutas con la configuracion de django tambien
        pueda servir imagenes en una ruta determinada.

        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    3. Luego en el archivo settings.py debemos configurar las variables
        MEDIA_ROOT y MEDIA_URL la primera contiene la ruta absoluta
        del directorio que guardara los archivos media como .jpg .png etc.
        y la segunda es como se llamara el directorio que va contener
        estas imagenes y archivos media

        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        MEDIA_URL = "/media/"
"""


class Profile(models.Model):
    """
    Profile model.
    Proxy model that extendes the base data with other
    information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        error_messages={
            "max_length": "Logitud máxima 20",
        },
    )

    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns username"""
        return self.user.username
