from django.contrib import admin
from .models import Post, Mark
# Register your models here.

admin.site.register(Mark)

class PostAdmin(admin.ModelAdmin):
    model = Post
    readonly_fields = ('get_count_of_likes', 'get_count_of_dislikes')
    fields = ('author', 'title','content', 'get_count_of_likes', 'get_count_of_dislikes' )
    list_display = ('author', 'title','content', 'get_count_of_likes', 'get_count_of_dislikes' )


admin.site.register(Post,PostAdmin )