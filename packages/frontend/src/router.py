import flet as ft
from pages.auth.login import LogIn
from pages.auth.signup import SignUp


def views_handler(page: ft.Page) -> None:
    return {
        "/login": ft.View(route="/login", controls=[LogIn(page)]),
        "/signup": ft.View(route="/signup", controls=[SignUp(page)])
    }