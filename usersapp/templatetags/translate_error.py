from django import template

register = template.Library()

ERROR_TRANSLATIONS = {
    "The two password fields didn’t match.": "Las contraseñas no coinciden.",
    "This password is too short. It must contain at least 8 characters.": "La contraseña debe contener al menos 8 caracteres.",
    "This password is too common.": "Contraseña muy común.",
    "This password is entirely numeric.": "La contraseña no puede ser enteramente numérica.",
    "The password is too similar to the username.": "La contraseña es demasiado similar al nombre de usuario.",
    "The password is too similar to the first name.": "La contraseña es demasiado similar al nombre.",
    "The password is too similar to the last name.": "La contraseña es demasiado similar al apellido.",
    "The password is too similar to the email address.": "La contraseña es demasiado similar al email.",
}

@register.filter
def translate_error(msg):
    return ERROR_TRANSLATIONS.get(str(msg), msg)
