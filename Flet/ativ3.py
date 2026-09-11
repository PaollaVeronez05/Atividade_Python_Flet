import flet as ft

def main(page: ft.Page):
    page.title = "Formulario"
    page.window.width = 400
    page.window.height = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.Padding(top=70, bottom=0, left=0, right=0)

    t_nome = ft.TextField(
        label="Nome Completo",
        hint_text="Digite seu nome",
        width=220,
        text_size=14,
    )
    termos = ft.Checkbox(label="Aceito os Termos", value=False)
    resultado = ft.Text(size=13, weight=ft.FontWeight.BOLD, color="green")

    def enviar_formulario(i):
        if not t_nome.value:
            t_nome.error_text = "Por favor, digite seu nome"
            page.update()
            return

        nome = t_nome.value
        resultado.value = f"Obrigado, {nome}!"
        t_nome.error_text = None
        page.update()

    butao = ft.Button(content="Enviar", on_click=enviar_formulario)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Formulário de Cadastro", size=18, weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[t_nome, termos],
                    width=220,
                    spacing=2,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                butao,
                resultado,
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.run(main)