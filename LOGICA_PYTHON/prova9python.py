# Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
# A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa 
# e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado 
# a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. 
# A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.


import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "white"

    lista_tarefas = ft.Column()

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip():
            lista_tarefas.controls.append(criar_tarefa(campo_tarefa.value))
            campo_tarefa.value = ""
            page.update()

    def criar_tarefa(nome):
        texto_tarefa = ft.Text(nome, expand=True, size=18)
        checkbox = ft.Checkbox(value=False)
        campo_edicao = ft.TextField(value=nome, visible=False, expand=True)

        def editar_tarefa(e):
            texto_tarefa.visible = False
            campo_edicao.visible = True
            btn_editar.visible = False
            btn_salvar.visible = True
            page.update()

        def salvar_edicao(e):
            texto_tarefa.value = campo_edicao.value
            texto_tarefa.visible = True
            campo_edicao.visible = False
            btn_editar.visible = True
            btn_salvar.visible = False
            page.update()

        def remover_tarefa(e):
            lista_tarefas.controls.remove(linha_tarefa)
            page.update()

        def marcar_tarefa(e):
            if checkbox.value:
                texto_tarefa.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
                texto_tarefa.color = "grey"
            else:
                texto_tarefa.style = ft.TextStyle(decoration=None)
                texto_tarefa.color = "black"
            page.update()

        checkbox.on_change = marcar_tarefa

        btn_editar = ft.IconButton(icon=ft.Icons.EDIT, tooltip="Editar", on_click=editar_tarefa)
        btn_salvar = ft.IconButton(icon=ft.Icons.SAVE, tooltip="Salvar", visible=False, on_click=salvar_edicao)
        btn_remover = ft.IconButton(icon=ft.Icons.DELETE, tooltip="Excluir", on_click=remover_tarefa)

        linha_tarefa = ft.Row(
            [
                checkbox,
                texto_tarefa,
                campo_edicao,
                btn_editar,
                btn_salvar,
                btn_remover
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return linha_tarefa

    barra = ft.Container(
        bgcolor="#a281e9",
        height=15,
        expand=False,
        margin=ft.margin.only(bottom=6),
    )

    titulo = ft.Text(
        "LISTA DE TAREFAS",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="grey",
        text_align=ft.TextAlign.CENTER,
    )

    campo_tarefa = ft.TextField(
        hint_text="ADICIONAR NOVA TAREFA...",
        expand=True,
    )

    botao_adicionar = ft.Container(
        content=ft.IconButton(icon=ft.Icons.ADD, icon_color="#a281e9", bgcolor="white", on_click=adicionar_tarefa),
        bgcolor="white",
        border_radius=ft.border_radius.all(14),
        shadow=ft.BoxShadow(blur_radius=4, color="grey"),
        width=48,
        height=48,
        alignment=ft.alignment.center,
    )

    page.add(
        barra,
        titulo,
        ft.Row([campo_tarefa, botao_adicionar], alignment=ft.MainAxisAlignment.START),
        lista_tarefas,
    )

ft.app(target=main)
