import flet as ft

def main(page: ft.Page):
    page.title = "Olá Mago"
    page.add(ft.Text("Olá Mago, seja bem-vindo ao Flet!"))



#ft.run(main,view=ft.AppView.WEB_BROWSER)
ft.run(main)
