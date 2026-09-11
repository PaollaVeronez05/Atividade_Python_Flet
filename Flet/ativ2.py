import flet as ft

def main(page: ft.Page):
    page.title = "perfil"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#F7F0EE"
    page.window.width = 300
    page.window.height = 300
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    page.add(
        ft.Container(
            width=300,
            height=170,
            bgcolor="#61B5FF",
            border_radius=10,
            padding= 20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Paolla Paula Veronez", color="#023664", text_align=ft.TextAlign.CENTER, size=20),
                    ft.Text("Analista de segurança Junior", size=14, color="#023664"),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.EMAIL, color="#023664", size=24),
                            ft.Text("paolla@gmail.com", color="#023664"),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.PHONE, color="#023664", size=24),
                            ft.Text("(11) 99999-9999", color="#023664   "),
                        ],
                    ),
                ],
            ),
        )
    )

ft.run(main)