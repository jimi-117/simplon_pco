import flet as ft
from utils.ui.colors import (
    double_spanish_white,
    wheatfield,
    satin_linen,
    san_juan,
    roman_coffee,
    battleship_gray,
    brown_yellow,
    customPrimaryColor,
    customBgColor,
    customTextHeaderColor,
    customTextColor,
    customSideBarIconColor,
    customDashbordBgColor,
    customBorderColor    
)

class CustomTextField(ft.TextField):
    def __init__(
        self,
        label,
        icon = None,
        password = False,
        border = ft.InputBorder.NONE,
        can_reveal_password = False,
        error_text = None,
        input_filter = None,
        **kwargs
    ) -> None:
        super().__init__(
            color = customTextColor,
            label = label,
            icon = icon,
            password = password,
            border = border,
            can_reveal_password = can_reveal_password,
            content_padding = ft.padding.only(top=0, bottom = 0, right = 20),
            error_text = error_text,
            hint_style = ft.TextStyle(size=14, color=customTextColor),
            input_filter = input_filter,  
            focused_color = customTextColor,
            **kwargs
        )