import flet as ft
cities = [
    # Central District
    "Tel Aviv-Yafo",
    "Petah Tikva",
    "Rishon LeZion",
    "Ramat Gan",
    "Givatayim",
    "Bnei Brak",
    "Holon",
    "Bat Yam",
    "Herzliya",
    "Ra'anana",
    "Kfar Saba",
    "Hod HaSharon",
    "Ramat HaSharon",
    "Rosh HaAyin",
    "Kiryat Ono",
    "Or Yehuda",
    "Yehud-Monosson",
    "Giv'at Shmuel",
    "Ramat Efal",
    "Ness Ziona",
    "Rehovot",
    "Yavne",
    "Ramla",
    "Lod",
    "Modi'in-Maccabim-Re'ut",
    "Shoham",
    "Gedera",
    "Kiryat Ekron",

    # Jerusalem and surroundings
    "Jerusalem",
    "Beit Shemesh",
    "Ma'ale Adumim",
    "Mevaseret Zion",
    "Abu Ghosh",
    "Giv'at Ze'ev",
    "Beitar Illit",
    "Modi'in Illit",
    "Ariel",

    # Sharon
    "Netanya",
    "Even Yehuda",
    "Tel Mond",
    "Pardesiya",
    "Kfar Yona",
    "Kadima-Zoran",
    "Tira",
    "Tayibe",
    "Qalansawe",
    "Kafr Qasim",
    "Ramat HaSharon",

    # Haifa and North
    "Haifa",
    "Kiryat Bialik",
    "Kiryat Motzkin",
    "Kiryat Yam",
    "Kiryat Ata",
    "Nesher",
    "Tirat Carmel",
    "Acre",
    "Nahariya",
    "Karmiel",
    "Ma'alot-Tarshiha",
    "Safed",
    "Tiberias",
    "Kiryat Shmona",
    "Hatzor HaGlilit",
    "Migdal HaEmek",
    "Nof HaGalil",
    "Afula",
    "Yokneam Illit",
    "Beit She'an",
    "Sakhnin",
    "Shefa-'Amr",
    "Tamra",
    "Umm al-Fahm",
    "Baqa al-Gharbiyye",
    "Nazareth",

    # South
    "Beersheba",
    "Ashdod",
    "Ashkelon",
    "Kiryat Gat",
    "Kiryat Malakhi",
    "Sderot",
    "Netivot",
    "Ofakim",
    "Dimona",
    "Arad",
    "Eilat",
    "Rahat",
    "Mitzpe Ramon",
    "Yeruham",
]


settlements = [
    # Galilee
    "Rosh Pina",
    "Yesod HaMa'ala",
    "Metula",
    "Kfar Vradim",
    "Shlomi",
    "Peki'in",
    "Kafr Kanna",
    "Yavne'el",
    "Migdal",
    "Jish",
    "Kafr Kanna",
    "Ilut",
    "Kafr Manda",

    # Golan Heights
    "Katzrin",
    "Majdal Shams",
    "Mas'ade",
    "Buq'ata",
    "Ein Qiniyye",
    "Merom Golan",
    "Alonei HaBashan",
    "Neve Ativ",

    # Jezreel Valley and surroundings
    "Nahalal",
    "Kfar Yehoshua",
    "Ramat Yishai",
    "Kiryat Tiv'on",
    "Yokneam Moshava",
    "Merhavia",

    # Carmel and Coast
    "Zikhron Ya'akov",
    "Binyamina-Giv'at Ada",
    "Pardes Hanna-Karkur",
    "Or Akiva",
    "Atlit",
    "Zikhron Ya'akov",

    # Hefer Valley
    "Hefer Valley",
    "Kfar Vitkin",
    "Mikhmoret",
    "Beit Yitzhak-Sha'ar Hefer",

    # Jerusalem area
    "Ein Karem",
    "Tzur Hadassah",
    "Nes Harim",
    "Bar Giora",
    "Eshtaol",
    "Tzuba",
    "Nataf",

    # Dead Sea
    "Ein Bokek",
    "Neve Zohar",
    "Ein Gedi",
    "Kalia",
    "Mitzpe Shalem",
    "Almog",

    # Negev
    "Lehavim",
    "Omer",
    "Meitar",
    "Kuseife",
    "Ar'ara BaNegev",
    "Hura",
    "Tel Sheva",
    "Segev Shalom",
    "Nevatim",
    "Mitzpe Ramon",
    "Sde Boker",
    "Ein Yahav",
    "Hatzeva",
    "Paran",
    "Tzofar",
    "Sapir",
    "Midreshet Ben-Gurion",
]
def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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
                ft.Text(f"Host name: {i}"),
                alignment=ft.Alignment.CENTER,
                bgcolor=ft.Colors.AMBER_100,
                border=ft.Border.all(1, ft.Colors.AMBER_400),
                border_radius=ft.BorderRadius.all(10),
            )
        )
    page.update()










if __name__ == "__main__":
    ft.run(main)