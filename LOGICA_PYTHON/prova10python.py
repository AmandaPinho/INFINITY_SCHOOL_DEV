# Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. 
# O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email 
# e um campo de texto para a mensagem. Após o usuário preencher esses campos, deve haver um botão de envio. 
# Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação 
# deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.


import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "white"
    page.window.width = 450
    page.padding = 20

    mensagem_confirmacao = ft.Text("", color="green", size=16)

    def enviar_click(e):
        nome = nome_field.value
        email = email_field.value
        mensagem = mensagem_field.value

        if nome and email and mensagem:
            nome_field.value = ""
            email_field.value = ""
            mensagem_field.value = ""
            mensagem_confirmacao.value = "Formulário enviado com sucesso!"
        else:
            mensagem_confirmacao.value = "Por favor, preencha todos os campos."

        page.update()

    nome_field = ft.TextField(label="Nome", width=400)
    email_field = ft.TextField(label="E-mail", width=400)
    mensagem_field = ft.TextField(label="Mensagem", multiline=True, width=400, min_lines=4)

    enviar_button = ft.ElevatedButton("ENVIAR", bgcolor="#a281e9", color="white", on_click=enviar_click, width=400)

    barra = ft.Container(
        bgcolor="#a281e9",
        height=15,
        expand=False,
        margin=ft.margin.only(bottom=6),
    )

    titulo = ft.Text(
        "FALE CONOSCO",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#7c7c7c",
        text_align=ft.TextAlign.CENTER,
    )

    page.add(
        ft.Column(
            [
                barra,
                titulo,
                nome_field,
                email_field,
                mensagem_field,
                enviar_button,
                mensagem_confirmacao,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)

