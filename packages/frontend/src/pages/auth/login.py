import flet as ft
from utils.ui.colors import (
    wheatfield,
    customTextColor,
    customTextHeaderColor
)

class LogIn(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(
            expand=True,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        expand=2,
                        padding=ft.padding.all(20),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Welcome back !",
                                    color=customTextHeaderColor,
                                    weight=ft.FontWeight.BOLD,
                                    size=40
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        expand=3,
                        image=ft.DecorationImage(
                            src="images/vintage_kitchen.jpg",
                            fit=ft.ImageFit.COVER
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(
                                    name = ft.icons.LOCK_PERSON_ROUNDED,
                                    size = 200),
                                ft.Text(
                                    "Login Portal",
                                    color=wheatfield,
                                    weight=ft.FontWeight.NORMAL,
                                    size=40
                                ),
                            ]
                        )
                    )
                ]
            )
        )

