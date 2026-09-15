import flet as ft


def sign_in_up(page: ft.Page):
    page.appbar = ft.AppBar(title=ft.Text("Home page"), center_title=True)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(content="Sign in"),
                    ft.Button(content="Sign up"),


                ]
            )
        ),
    )
