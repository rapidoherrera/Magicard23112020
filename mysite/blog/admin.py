from django.contrib import admin
from .models import Post
from .models import Cliente

# Register your models here.
admin.site.register(Post)

admin.site.register(Cliente)