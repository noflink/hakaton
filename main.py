import flet as ft


def main(page: ft.Page):

    def start_screen():
        page.appbar = ft.AppBar(title=ft.Text("Start screen"), center_title=True)
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        log_in_button = ft.Button(content="Log in")
        sign_in_button = ft.Button(content="Sign up")
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        log_in_button,
                        sign_in_button,
                    ]
                )
            ),
        )
    def soldier_or_host():
        page.appbar = ft.AppBar(title=ft.Text("soldier or host"), center_title=True)
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        soldier = ft.Checkbox(label="חייל")
        host = ft.Checkbox(label="מארח")
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        soldier,
                        host,
                    ]
                )
            ),
        )

    def soldier_sign_up():
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Sign up screen"), center_title=True)
        name = ft.TextField(label="Name", hint_text="Jane Doe")
        last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        password = ft.TextField(key="password_textfield",label="Enter password",password=True,can_reveal_password=True)
        email = ft.TextField(label="email", hint_text="Jane Doe")

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        name,
                        last_name,
                        password,
                        email,
                    ]
                )
            ),
        )

    def host_sign_up():
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Sign up screen"), center_title=True)
        name = ft.TextField(label="Name", hint_text="Jane Doe")
        last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        password = ft.TextField(key="password_textfield",label="Enter password",password=True,can_reveal_password=True)
        email = ft.TextField(label="email", hint_text="Jane Doe")
        city = ft.TextField(label="City", hint_text="Jane Doe")

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        name,
                        last_name,
                        password,
                        email,
                        city,
                    ]
                )
            ),
        )

    def host_page():
        page.appbar = ft.AppBar(title=ft.Text("Host home screen"), center_title=True)


        host_name = ft.TextField(label="Name", hint_text="Jane Doe")
        host_last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        spots = ft.TextField(label="How many spots", hint_text="Jane Doe")
        add = ft.Button(content="+")
        content = ft.TextField(
            key="styled_textfield",
            text_size=15,
            bgcolor=ft.Colors.BLACK_26,
            filled=True,
            focused_color=ft.Colors.GREEN,
            focused_bgcolor=ft.Colors.CYAN_200,
            border={
                ft.ControlState.DEFAULT: ft.OutlineInputBorder(
                    border_radius=100,
                    side=ft.BorderSide(color=ft.Colors.GREEN_800),
                ),
                ft.ControlState.FOCUSED: ft.OutlineInputBorder(
                    border_radius=100,
                    side=ft.BorderSide(width=2, color=ft.Colors.GREEN_ACCENT_400),
                ),
            },
            max_length=100,
            capitalization=ft.TextCapitalization.CHARACTERS,
        )

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        host_name,
                        host_last_name,
                        spots,
                        content,
                    ]
                )
            ),
        )
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        add,
                    ]
                )
            ),
        )

    def build_tiles(items: list[str]) -> list[ft.Control]:
        return [
            ft.ListTile(
                title=ft.Text(item),
                data=item,
                on_click=handle_tile_click,
            )
            for item in items
        ]

    async def handle_tile_click(e: ft.Event[ft.ListTile]):
        await anchor.close_view()

    async def handle_change(e: ft.Event[ft.SearchBar]):
        query = e.control.value.strip().lower()
        matching = (
            [city for city in cities if query in city.lower()] if query else cities
        )
        anchor.controls = build_tiles(matching)

    def handle_submit(e: ft.Event[ft.SearchBar]):
        print(f"Submit: {e.data}")

    async def handle_tap(e: ft.Event[ft.SearchBar]):
        await anchor.open_view()

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.Colors.AMBER,
        bar_hint_text="Select where you want to stay...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=build_tiles(cities),
    )
    page.add(ft.SafeArea(content=anchor))
    gv = ft.GridView(expand=True, max_extent=400, child_aspect_ratio=1)
    page.add(gv)

    for i in range(12):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Host name: {posts[i]["host_name"]}"),
                alignment=ft.Alignment.CENTER,
                bgcolor=ft.Colors.AMBER_100,
                border=ft.Border.all(1, ft.Colors.AMBER_400),
                border_radius=ft.BorderRadius.all(10),
            )
        )
    page.update()


#soldier_sign_up()
    #host_sign_up()
    #host_page()
    #sign_up()
    #start_screen()
if __name__ == "__main__":
    ft.run(main)