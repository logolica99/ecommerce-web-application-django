from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories",views.Categories,name="categories"),
    path("watchlist", views.Watchlist, name="watchlist"),
    path("create_listing",views.create_listing,name="create_listing"),
    path("<int:list_id>",views.listing_page,name="listing_page")
]
