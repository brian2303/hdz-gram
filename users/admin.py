from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Agregando el modelo Profile que creamos basados en User de django al admin.
from users.models import Profile
from django.contrib.auth.models import User

# Registrar un Model de manera simple
# admin.site.register(Profile)


# Registrar un model con caracteristicas extras como filtros etc.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # formato en el que vamos a mostrar los datos en el admin
    list_display = ("pk", "user", "phone_number", "website", "picture")

    # Con esto cada vez que hacemos click en un registro de la columna user nos lleva al detalle completo
    list_display_links = ("user",)

    # podemos editar solo haciendo click en el valor del campo
    list_editable = ("phone_number", "website")

    # aparece una barra de busqueda y me permite buscar por el campo email en este ejemplo
    search_fields = ("user__email", "user__username")

    # me agrega un filtro especial con estos campos.
    list_filter = ("created", "modified", "user__is_active")

    fieldsets = (
        (
            "Profile",
            {"fields": (("user", "phone_number"),)},
        ),
    )


# permite agregar los datos del profile de una vez en el registro de User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = "Profiles"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_display = ("username", "last_name", "email", "is_active", "is_staff")


admin.site.unregister(User)
admin.site.register(User, UserAdmin)