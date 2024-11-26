import flet as ft

class SignUp(ft.Container):
    def __init__(self, page:ft.Page) -> None:
        super().__init__()
        
        self.content = ft.Column(
            controls = [
                ft.Text("Hello there, sign up here!"),
                ft.ElevatedButton(
                    text = "Login",
                    on_click = lambda e: page.go("/login")
                )
            ]
        )