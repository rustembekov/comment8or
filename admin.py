from django.contrib import admin

class Comment8orAdminSite(admin.AdminSite):
    index_title = 'Sabyrzhan Rustembekov'
    title_header = 'c8admin'
    site_header = 'c8admin'
    logout_template = 'comment8or/logged_out.html'


