'''
Admin
'''
from django.contrib import admin
from project.models import User,Driver,Updates,Report,Trip,Schedule


admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Updates)
admin.site.register(Report)
admin.site.register(Trip)
admin.site.register(Schedule)
