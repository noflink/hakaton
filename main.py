import flet as ft
import database as db
import consts
import Host
import Guest
from typing import *

cities = [
    "Jerusalem",
    "Tel Aviv",
    "Haifa",
    "Rishon LeZion",
    "Petah Tikva",
    "Ashdod",
    "Netanya",
    "Beersheba",
    "Bnei Brak",
    "Holon",
    "Ramat Gan",
    "Ashkelon",
    "Rehovot",
    "Bat Yam",
    "Herzliya",
    "Kfar Saba",
    "Hadera",
    "Modi'in-Maccabim-Re'ut",
    "Nazareth",
    "Lod",
    "Ramla",
    "Ra'anana",
    "Givatayim",
    "Kiryat Ata",
    "Nahariya",
    "Umm al-Fahm",
    "Eilat",
    "Acre",
    "Afula",
    "Karmiel",
    "Tiberias",
    "Kiryat Gat",
    "Kiryat Motzkin",
    "Kiryat Yam",
    "Kiryat Bialik",
    "Kiryat Ono",
    "Or Yehuda",
    "Yavne",
    "Nes Ziona",
    "Hod HaSharon",
    "Rosh HaAyin",
    "Ramat HaSharon",
    "Sakhnin",
    "Shefaram",
    "Tamra",
    "Arad",
    "Sderot",
    "Dimona",
    "Migdal HaEmek",
    "Yokneam Illit",
    "Nof HaGalil",
    "Safed",
    "Ma'alot-Tarshiha",
    "Tayibe",
    "Tira",
    "Qalansawe",
    "Kafr Qasim",
    "Rahat",
    "Kuseife",
    "Hura",
    "Ar'ara",
    "Baqa al-Gharbiyye",
    "Jisr az-Zarqa",
    "Kafr Kana",
    "Kafr Yasif",
    "Ein Mahil",
    "Abu Ghosh",
    "Daliyat al-Karmel",
    "Isfiya",
    "Zikhron Ya'akov",
    "Pardes Hanna-Karkur",
    "Binyamina",
    "Mevasseret Zion",
    "Shoham",
    "Gedera",
    "Ganei Tikva",
    "Even Yehuda",
    "Katzrin",
    "Metula",
    "Kiryat Shmona",
    "Ofakim",
    "Netivot",
    "Yeruham",
    "Mitzpe Ramon",
    "Bet Shemesh",
    "Beit She'an",
    "Nesher",
    "Tirat Carmel",
    "Gan Yavne",
    "Kadima-Zoran",
    "Harish",
    "Elad",
    "Modi'in Illit",
    "Beitar Illit",
]
user = None
db.start()


def main(page: ft.Page):
    def start_screen():
        page.appbar = ft.AppBar(title=ft.Text("Start screen"), center_title=True)
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        log_in_button = ft.Button(content="Log in", on_click=log_in)
        sign_in_button = ft.Button(content="Sign up", on_click=soldier_or_host)
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
        page.clean()
        page.appbar = ft.AppBar(title=ft.Text("soldier or host"), center_title=True)
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        soldier_button = ft.Button(content="Soldier", on_click=soldier_sign_up)
        host_button = ft.Button(content="Host", on_click=host_sign_up)
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        soldier_button,
                        host_button,
                    ]
                )
            ),
        )

    def soldier_sign_up():
        page.clean()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Sign up screen"), center_title=True)
        name = ft.TextField(label="Name", hint_text="Jane Doe")
        last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        password = ft.TextField(key="password_textfield", label="Enter password", password=True,
                                can_reveal_password=True)
        email = ft.TextField(label="email", hint_text="Jane Doe")
        create_button = ft.Button(content="create",
                                  on_click=lambda: handle_guest_sign_up(name.value, last_name.value, email.value,
                                                                        password.value))

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        name,
                        last_name,
                        password,
                        email,
                        create_button,
                    ]
                )
            ),
        )

    def host_sign_up():
        page.clean()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Sign up screen"), center_title=True)
        name = ft.TextField(label="Name", hint_text="Jane Doe")
        last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        i_d = ft.TextField(label="id")
        address = ft.TextField(label="address", hint_text="Jane Doe")
        phone_number = ft.TextField(label="phone number", hint_text="Jane Doe")
        password = ft.TextField(key="password_textfield", label="Enter password", password=True,
                                can_reveal_password=True)
        email = ft.TextField(label="email", hint_text="Jane Doe")
        city = ft.TextField(label="City", hint_text="Jane Doe")
        create_button = ft.Button(content="create",
                                  on_click=lambda: handle_host_sign_up(name.value, last_name.value, email.value,
                                                                       password.value, i_d.value, address.value,
                                                                       phone_number.value, city.value))

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        name,
                        last_name,
                        password,
                        email,
                        city,
                        i_d,
                        address,
                        phone_number,
                        create_button,
                    ]
                )
            ),
        )

    def host_page():
        page.clean()
        page.appbar = ft.AppBar(title=ft.Text("Host home screen"), center_title=True)

        host_name = ft.TextField(label="Name", hint_text="Jane Doe")
        host_last_name = ft.TextField(label="Last_Name", hint_text="Jane Doe")
        spots = ft.TextField(label="How many spots", hint_text="Jane Doe")
        add = ft.Button(content="+", on_click=lambda: add_post(spots.value, content.value))
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

    def add_post(spots, content):
        print("adding post")
        global user
        spots = int(spots)
        db.add_post(user.host_id, user.name, user.host_family, user.city, user.address, spots, content, "1.1.1")
        host_page()

    ########## RONI ##########

    def log_in():
        page.clean()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Log in screen"), center_title=True)
        password = ft.TextField(key="password_textfield", label="Enter password", password=True,
                                can_reveal_password=True)
        email = ft.TextField(label="email", hint_text="Jane Doe")
        create_button = ft.Button(content="create", on_click=lambda: check_login(email.value, password.value))

        page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        email,
                        password,
                        create_button,
                    ]
                )
            ),
        )

    def check_login(email, password):
        global user
        success, usertype = db.check_login(email, password)
        print(f"{success}: {usertype}")
        if success:
            if usertype == consts.HOSTS:
                host_dict = db.get_host(email)
                user = Host.Host(host_dict)
                host_page()
            elif usertype == consts.GUESTS:
                guest_dict = db.get_guest(email)
                user = Guest.Guest(guest_dict)
                posts = db.get_all_posts()
                guest_page(posts)

    def handle_host_sign_up(name, family, email, password, id, address, phone, city):
        global user
        db.add_host(name, family, email, password, id, address, phone, city)
        user = Host.Host(db.get_host(email))
        host_page()

    def handle_guest_sign_up(name, family, email, password):
        global user
        db.add_guest(name, family, email, password)
        user = Guest.Guest(db.get_guest(email))
        posts = db.get_all_posts()
        guest_page(posts)

    def guest_page(posts):
        page.clean()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        def build_tiles(items: list[str]) -> list[ft.Control]:
            return [
                ft.ListTile(
                    title=ft.Text(item),
                    data=item
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
            get_posts(e.data)

        def get_posts(city):
            if city == "":
                guest_page(db.get_all_posts())
                return
            guest_page(db.get_posts(city))

        async def handle_tap(e: ft.Event[ft.SearchBar]):
            await anchor.open_view()

        anchor = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.Colors.AMBER,
            bar_hint_text="Select where you want to stay...",
            view_hint_text="Choose a city from the suggestions...",
            on_change=handle_change,
            on_submit=handle_submit,
            on_tap=handle_tap,
            controls=build_tiles(cities),
        )
        page.add(ft.SafeArea(content=anchor))
        gv = ft.GridView(expand=True, max_extent=400, child_aspect_ratio=1)
        page.add(gv)

        for i in range(len(posts)):
            gv.controls.append(
                ft.Container(
                    ft.Text(f"Host name: {posts[i]["host_name"]},\n"
                            f"Content: {posts[i]["content"]}"),
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.AMBER_100,
                    border=ft.Border.all(1, ft.Colors.AMBER_400),
                    border_radius=ft.BorderRadius.all(10),
                )
            )
        page.update()

    # guest_page()
    # log_in()
    # soldier_or_host()
    # soldier_sign_up()
    # host_sign_up()
    # host_page()
    start_screen()


if __name__ == "__main__":
    ft.run(main)

# import database as db
#
#
# def main():
#     db.start()
#
#
# def start_connection():
#     # start gui
#     # welcome screen
#     # log in & sign up
#     # check log in / sign up
#     # main screen (guest/host)
#
#     #search function
#
#     #
#     pass
#
# def check_login_info(email, password, usertype):
#     success = db.check_login(email, password, usertype)
#     if success:
#         pass
#     return
#
# def check_sign_in_info(email, usertype):
#     success = db.check_sing_up_email(email, usertype)
#     if success:
#         add_user(usertype)
#     return
#
# def add_user(usertype):
#     pass
#
#
# # post = Post(333222, 3333111, "tehila", "zvulunov",
# #             "ramla", "yosi banai", 3, 3, "dxgfch")
#
#
#
#
#
# if __name__ == '__main__':
#     main()
