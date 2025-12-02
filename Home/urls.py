from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="About"),
    path("services", views.services, name="Services"),
    path("contact", views.contact, name="Contact"),
    path("news", views.news, name="News"),
    path("airdrops", views.airdrops, name="Airdrops"),
    path("coindata", views.coindata, name="CoinData"),
    path("nodes", views.nodes, name="Nodes"),
    path("node1", views.node1, name="Node1"),
    path("node2", views.node2, name="Node2"),
    path("node3", views.node3, name="Node3"),
    path("node4", views.node4, name="Node4"),
    path("login", views.login, name="Login"),
    path("register", views.register, name="Register"),
]
