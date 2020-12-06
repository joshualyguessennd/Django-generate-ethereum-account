from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
	list_display = ['id','email','username', 'wallet', 'date_join', 'last_login', 'is_admin','is_staff']
	search_fields = ['id','email','username',]
	readonly_fields = ['id']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)


