import flet as ft


def main(page: ft.Page):
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = (
            f"Textboxes values are:  '{tb1.value}', '{tb2.value}'."
        )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.SafeArea(

            content=ft.Column(

                controls=[
                    ft.Text(
                        value="Log In",
                        size=50,
                        weight=ft.FontWeight.W_900,
                        selectable=True,
                    ),
                    tb1 := ft.TextField(label="Email"),
                    tb2 := ft.TextField(
                        label="Password"
                    ),


                    ft.Button(content="Submit", on_click=handle_button_click),
                    message := ft.Text(),
                ],
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main)