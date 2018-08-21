from django.contrib import admin
from .models import Media, Picture, Video, Document, Tag, Post, Link, Sponsor, Member, OutreachEvent

# Register your models here.


admin.site.register(Media)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Document)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Link)
admin.site.register(Sponsor)
admin.site.register(Member)
admin.site.register(OutreachEvent)
