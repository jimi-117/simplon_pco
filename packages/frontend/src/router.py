import flet as ft
from pages.auth.login import LogIn
from pages.auth.signup import SignUp
from utils.ui.colors import (
    customBgColor
)


def views_handler(page: ft.Page) -> None:

    return {
        "/login": 
            ft.View(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                route = "/login", 
                bgcolor = customBgColor,
                padding = ft.padding.all(0),
                controls = [LogIn(page)]
                ),
        "/signup": 
            ft.View(route="/signup", controls=[SignUp(page)])
    }