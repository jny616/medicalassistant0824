#admin.py

class records_Admin(admin.ModelAdmin):
    list_display = ('id','uid','name','description','mdt')
admin.site.register(records,records_Admin)