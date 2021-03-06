from django.contrib import admin
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'updated',
        'timestamp',
        'new_content'
    ]
    readonly_fields = ['updated', 'timestamp', 'new_content']

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    class Meta:
        model = PostModel


admin.site.register(PostModel, PostModelAdmin)

# admin.site.register(PostModel)
