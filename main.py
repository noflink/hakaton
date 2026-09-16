import flet as ft


def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = (
            f"Textboxes values are:  '{tb1.value}', '{tb2.value}'. "

        )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Log In", size=40, weight=ft.FontWeight.W_600),
                    tb1 := ft.TextField(label="Email"),
                    tb2 := ft.TextField(label="Password"),

                    ft.Button(content="Submit", on_click=handle_button_click),
                    message := ft.Text(),
                ],
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main)