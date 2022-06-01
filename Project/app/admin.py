from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Tag)
admin.site.register(models.LikeQuestion)
admin.site.register(models.Answer)
admin.site.register(models.Question)
admin.site.register(models.LikeAnswer)
