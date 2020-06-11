from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from breadcrumbs.models import Node

# Register your models here.

admin.site.register(
    Node,
    DraggableMPTTAdmin,
)