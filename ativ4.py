import flet as ft


def main(page: ft.Page):
    page.title = "Mercado do mago"
    page.window.width = 400
    page.window.height = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.Padding(top=70, bottom=0, left=0, right=0)

    t_nome = ft.TextField(
        label="Nome do item",
        hint_text="Digite seu item",
        width=220,
        text_size=14,
    )

    resultado = ft.Text(size=13, weight=ft.FontWeight.BOLD, color="green")
    lista = ft.Column(width=300, spacing=0)  

    def criar_item(nome):
        quantidade = ft.Text("1", size=14, width=30, text_align=ft.TextAlign.CENTER)

        def diminuir(i):
            if int(quantidade.value) > 1:
                quantidade.value = str(int(quantidade.value) - 1)
                page.update()

        def aumentar(i):
            quantidade.value = str(int(quantidade.value) + 1)
            page.update()

        # Função para remover esta linha da lista
        def remover(i):
            lista.controls.remove(linha)
            page.update()

        # Criamos a linha em uma variável para podermos removê-la depois
        linha = ft.Row(
            controls=[
                ft.Text(nome, size=14, expand=True),
                ft.IconButton(ft.Icons.REMOVE, on_click=diminuir),
                quantidade,
                ft.IconButton(ft.Icons.ADD, on_click=aumentar),
                ft.IconButton(ft.Icons.DELETE, icon_color="red", on_click=remover), # Lixeira adicionada
            ],
        )
        return linha

    def enviar_formulario(i):
        if not t_nome.value:
            t_nome.error_text = "Por favor, digite seu item"
            page.update()
            return

        nome = t_nome.value
        resultado.value = f"você adicionou o item: {nome}!"
        lista.controls.append(criar_item(nome))  # põe o item com contador e lixeira na lista
        t_nome.value = ""                        # limpa a caixa
        t_nome.error_text = None
        page.update()

    butao = ft.Button(content="Enviar", on_click=enviar_formulario)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Mercadinho", size=18, weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[t_nome],
                    width=220,
                    spacing=2,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                butao,
                resultado,
                lista,
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.run(main)
