"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from mysite import views as mv

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('switch-theme/', mv.change_theme, name="change-theme"),
    path('', mv.homepage, name="homepage"),
    path('view_book/', mv.view_book, name="view_book"),
    path('intro/<slug:post_slug>/', mv.intro, name='intro'),
    path('filter/', mv.filter, name="filter"),
    path('search_books/', mv.search_books, name='search_books'),
    path('episode/<int:episode_id>/', mv.showepisode, name='showepisode'),
    
    path('admin_login/', mv.admin_login, name='admin_login'),
    path('view_users/', mv.view_users, name='view_users'),
    path('add_book/', mv.add_book, name='add_book'),

    path('user_login/', mv.user_login, name='user_login'),
    path('user_registration/', mv.user_registration, name='user_registration'),
    path('profile/', mv.profile, name='profile'),
    path('edit_profile/', mv.edit_profile, name='edit_profile'),
    path('edit_account/', mv.edit_account, name='edit_account'),
    path("logout/", mv.Logout, name="logout"),

    path("delete_book/<int:myid>/", mv.delete_book, name="delete_book"),
    path("delete_user/<int:myid>/", mv.delete_student, name="delete_student"),

    
]
