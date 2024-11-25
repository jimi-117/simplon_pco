import os
import flet as ft
import requests
import json
from flet_core.control_event import ControlEvent
from responsive_menu_layout import ResponsiveMenuLayout
from switch_dark import ToggleDarkMode

class UserLogin:
    pass

class UserLogout:
    pass

class UserRegister:
    pass

class UploadImage:
    pass

def create_page(title: str, body: str):
        return ft.Row(
            controls=[
                ft.Column(
                    horizontal_alignment="stretch",
                    controls=[
                        ft.Card(content=ft.Container(ft.Text(title, weight="bold"), padding=8)),
                        ft.Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )

def main(page: ft.Page, title="Qu'est-ce qu'on mange ce soir ?") -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    menu_button = ft.IconButton("menu")
    page.theme = ft.Theme(color_scheme_seed='green')
    page.appbar = ft.AppBar(
            title=ft.Text(f"{title}", size=20),
            leading=menu_button,
            leading_width=40,
            center_title=True,
            toolbar_height=70,
        )
    
    pages = [
        (
                dict(
                    icon=ft.icons.LANDSCAPE_OUTLINED,
                    selected_icon=ft.icons.LANDSCAPE,
                    label="Menu in landscape",
                ),
                create_page(
                    "Menu in landscape",
                    "Menu in landscape is by default shown, side by side with the main content, but can be "
                    "hidden with the menu button.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.PORTRAIT_OUTLINED,
                    selected_icon=ft.icons.PORTRAIT,
                    label="Menu in portrait",
                ),
                create_page(
                    "Menu in portrait",
                    "Menu in portrait is mainly expected to be used on a smaller mobile device."
                    "\n\n"
                    "The menu is by default hidden, and when shown with the menu button it is placed on top of the main "
                    "content."
                    "\n\n"
                    "In addition to the menu button, menu can be dismissed by a tap/click on the main content area.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.INSERT_EMOTICON_OUTLINED,
                    selected_icon=ft.icons.INSERT_EMOTICON,
                    label="Minimize to icons",
                ),
                create_page(
                    "Minimize to icons",
                    "ResponsiveMenuLayout has a parameter minimize_to_icons. "
                    "Set it to True and the menu is shown as icons only, when normally it would be hidden.\n"
                    "\n\n"
                    "Try this with the 'Minimize to icons' toggle in the top bar."
                    "\n\n"
                    "There are also landscape_minimize_to_icons and portrait_minimize_to_icons properties that you can "
                    "use to set this property differently in each orientation.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.COMPARE_ARROWS_OUTLINED,
                    selected_icon=ft.icons.COMPARE_ARROWS,
                    label="Menu width",
                ),
                create_page(
                    "Menu width",
                    "ResponsiveMenuLayout has a parameter manu_extended. "
                    "Set it to False to place menu labels under the icons instead of beside them."
                    "\n\n"
                    "Try this with the 'Menu width' toggle in the top bar.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.ROUTE_OUTLINED,
                    selected_icon=ft.icons.ROUTE,
                    label="Route support",
                    route="custom-route",
                ),
                create_page(
                    "Route support",
                    "ResponsiveMenuLayout has a parameter support_routes, which is True by default. "
                    "\n\n"
                    "Routes are useful only in the web, where the currently selected page is shown in the url, "
                    "and you can open the app directly on a specific page with the right url."
                    "\n\n"
                    "You can specify a route explicitly with a 'route' item in the menu dict (see this page in code). "
                    "If you do not specify the route, a slugified version of the page label is used "
                    "('Menu width' becomes 'menu-width').",
                ),
            ),
            (
                dict(
                    icon=ft.icons.PLUS_ONE_OUTLINED,
                    selected_icon=ft.icons.PLUS_ONE,
                    label="Fine control",
                ),
                create_page(
                    "Adjust navigation rail",
                    "NavigationRail is accessible via the navigation_rail attribute of the ResponsiveMenuLayout. "
                    "In this demo it is used to add the leading button control."
                    "\n\n"
                    "These NavigationRail attributes are used by the ResponsiveMenuLayout, and changing them directly "
                    "will probably break it:\n"
                    "- destinations\n"
                    "- extended\n"
                    "- label_type\n"
                    "- on_change\n",
                ),
            ),
    ]
    
    menu_layout = ResponsiveMenuLayout(page, pages)
    
    menu_button.on_click = lambda e: menu_layout.toggle_navigation()
    page.appbar.actions = []
    ToggleDarkMode(page, page.appbar.actions)
    
    page.add(menu_layout)
    
if __name__ == "__main__" :
    ft.app(target=main)
    