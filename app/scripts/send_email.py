from django.core.mail import send_mail

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'e.gomez@uvax.es'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

send_mail(
    'Título del correo',
    'Hola, este correo es enviado desde un post en Django. 🐍',
    'e.gomez@uvax.es',
    ['eduardegomez@gmail.com'],
    fail_silently=False
)

