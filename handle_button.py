import page
import flet as ft

def handle_button_click(e: ft.Event[ft.Button]):
    message.value = (
        f"Textboxes values are:  '{tb1.value}', '{tb2.value}'."
    )