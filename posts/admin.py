from django.contrib import admin
from .models import Post
from .models import Vote

admin.site.register(Post)
admin.site.register(Vote)
