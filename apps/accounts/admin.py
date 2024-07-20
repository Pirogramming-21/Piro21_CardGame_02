from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # 사용자 목록에 표시할 필드
    list_display = ('username', 'email', 'score', 'is_staff', 'is_superuser')

    # 사용자 편집 페이지에서 표시할 필드
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('score',)}),
    )

    # 사용자 추가 페이지에서 표시할 필드
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('score',)}),
    )

# CustomUser 모델을 커스터마이징한 UserAdmin과 함께 등록
admin.site.register(CustomUser, CustomUserAdmin)