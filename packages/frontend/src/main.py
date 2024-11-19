import time
import flet as ft


def main(page: ft.Page):
    page.title = "Qu'est-ce qu'on mange ce soir?"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(
        ft.Row(
            [
                new_task,
                ft.ElevatedButton("Add", on_click=add_clicked)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

ft.app(main)