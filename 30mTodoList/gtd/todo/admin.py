from django.contrib import admin
from todo.models import List, Item

class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'title')
    #search_fields = ('title')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'priority', 'completed', 'todo_list')
    # list_filter = ('publication_date',)
    # date_hierarchy = 'publication_date'
    # ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    # filter_horizontal = ('authors',)
    # raw_id_fields = ('publisher',)

# admin.site.register(List)
admin.site.register(List, ListAdmin)
# admin.site.register(Item)
admin.site.register(Item, ItemAdmin)