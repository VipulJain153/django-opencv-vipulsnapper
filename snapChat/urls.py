from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "VipulSnapper Admin"
admin.site.site_title = "VipulSnapper Admin Portal"
admin.site.index_title = "Welcome to VipulSnapper"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainApp.urls")),
]
