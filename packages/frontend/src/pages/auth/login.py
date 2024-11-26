import flet as ft

class LogIn(ft.Container):
    def __init__(self, page:ft.Page) -> None:
        super().__init__()
        
        self.content = ft.Column(
            controls=[
                ft.Text("Login here!", color="white"),
                ft.ElevatedButton(
                    text= "Sign up", 
                    on_click= lambda e: page.go("/signup")),
                
            ]
        )