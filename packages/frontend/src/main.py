
import flet as ft

from flet_core.control_event import ControlEvent

# importig DIY functions
from router import views_handler
from utils.ui.interface import ResponsiveMenuLayout, create_page, ToggleDarkMode



class UploadImage:
    pass


def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Qu'est-ce qu'on mange ce soir ?"
    menu_button = ft.IconButton("menu")
    page.theme = ft.Theme(color_scheme_seed='green')
    page.appbar = ft.AppBar(
            title=ft.Text(f"{page.title}", size=35),
            leading=menu_button,
            leading_width=40,
            center_title=True,
            toolbar_height=50,
        )
    
    
    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])
        page.update()
    page.on_route_change = route_change
    page.go("/login")
    
    # pages = [
    #     (
    #             dict(
    #                 icon=ft.icons.LANDSCAPE_OUTLINED,
    #                 selected_icon=ft.icons.LANDSCAPE,
    #                 label="Menu in landscape",
    #             ),
    #             create_page(
    #                 "Menu in landscape 2",
    #                 "Menu in landscape is by default shown, side by side with the main content, but can be "
    #                 "hidden with the menu button.",
    #             ),
    #         ),
    #         (
    #             dict(
    #                 icon=ft.icons.PORTRAIT_OUTLINED,
    #                 selected_icon=ft.icons.PORTRAIT,
    #                 label="Menu in portrait",
    #             ),
    #             create_page(
    #                 "Menu in portrait",
    #                 "Menu in portrait is mainly expected to be used on a smaller mobile device."
    #                 "\n\n"
    #                 "The menu is by default hidden, and when shown with the menu button it is placed on top of the main "
    #                 "content."
    #                 "\n\n"
    #                 "In addition to the menu button, menu can be dismissed by a tap/click on the main content area.",
    #             ),
    #         ),
    #         (
    #             dict(
    #                 icon=ft.icons.INSERT_EMOTICON_OUTLINED,
    #                 selected_icon=ft.icons.INSERT_EMOTICON,
    #                 label="Minimize to icons",
    #             ),
    #             create_page(
    #                 "Minimize to icons",
    #                 "ResponsiveMenuLayout has a parameter minimize_to_icons. "
    #                 "Set it to True and the menu is shown as icons only, when normally it would be hidden.\n"
    #                 "\n\n"
    #                 "Try this with the 'Minimize to icons' toggle in the top bar."
    #                 "\n\n"
    #                 "There are also landscape_minimize_to_icons and portrait_minimize_to_icons properties that you can "
    #                 "use to set this property differently in each orientation.",
    #             ),
    #         ),
    #         (
    #             dict(
    #                 icon=ft.icons.COMPARE_ARROWS_OUTLINED,
    #                 selected_icon=ft.icons.COMPARE_ARROWS,
    #                 label="Menu width",
    #             ),
    #             create_page(
    #                 "Menu width",
    #                 "ResponsiveMenuLayout has a parameter manu_extended. "
    #                 "Set it to False to place menu labels under the icons instead of beside them."
    #                 "\n\n"
    #                 "Try this with the 'Menu width' toggle in the top bar.",
    #             ),
    #         )
    # ]
    
    # menu_layout = ResponsiveMenuLayout(page, pages)
    
    # menu_button.on_click = lambda e: menu_layout.toggle_navigation()
    # page.appbar.actions = []
    # ToggleDarkMode(page, page.appbar.actions)
    # page.add(
    #     menu_layout
    #     )
    
if __name__ == "__main__" :
    ft.app(target=main)
    