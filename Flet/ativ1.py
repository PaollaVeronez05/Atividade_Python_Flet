import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de Apresentação"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#008B8B"
    page.window.width = 320
    page.window.height = 600
    page.padding=(ft.Padding (top=60, bottom=60, left=0, right=0))

    page.add(
        ft.Text("Paolla Paula Veronez", color="#9fff", text_align=ft.TextAlign.CENTER, size=28),
        ft.Text("Desenvolvedora de sistemas", size=14, color="#00ffff")
    )

ft.run(main)
