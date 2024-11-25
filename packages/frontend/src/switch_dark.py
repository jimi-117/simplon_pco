import flet as ft
from time import sleep

class ToggleDarkMode():
    def __init__(
        self,
        page: ft.Page,
        contents: list,
        * args,
        ** kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        
        # progress bar
        self.splash = ft.ProgressBar(visible=False)
        
        def change_theme(e: ft.ControlEvent) ->None:
            self.splash.visible = True
            page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
            page.update()
            
            sleep(1)
            
        # Button to toggle theme mode
        toggle_dark_light = ft.IconButton(
            tooltip=f"Toggle {page.theme_mode} mode",
            on_click=change_theme,
            icon="light_mode",
            selected_icon="dark_mode",
            style=ft.ButtonStyle(
                color={
                    "": ft.colors.ORANGE_200,
                    "selected": ft.colors.GREY
                }
            )
        )
        
        contents.append(
            ft.Container(
                content=toggle_dark_light,
                margin=ft.margin.only(
                    right=10
                )
            )
        )