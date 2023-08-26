from django.contrib import admin
from .models import passwords  , chats ,answers

# your_app_name/admin.py


admin.site.register(answers)
admin.site.register(passwords)
admin.site.register(chats)
