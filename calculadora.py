import flet as ft
import math

btns = [
    {'operador': 'AC', 'fonte': ft.colors.BLACK, 'bg': ft.colors.GREY},
    {'operador': '±', 'fonte': ft.colors.BLACK, 'bg': ft.colors.GREY},
    {'operador': '%', 'fonte': ft.colors.BLACK, 'bg': ft.colors.GREY},
    {'operador': '/', 'fonte': ft.colors.BLACK, 'bg': ft.colors.ORANGE},
    {'operador': '7', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '8', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '9', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '*', 'fonte': ft.colors.BLACK, 'bg': ft.colors.ORANGE},
    {'operador': '4', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '5', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '6', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '-', 'fonte': ft.colors.BLACK, 'bg': ft.colors.ORANGE},
    {'operador': '1', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '2', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '3', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '+', 'fonte': ft.colors.BLACK, 'bg': ft.colors.ORANGE},
    {'operador': '0', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '.', 'fonte': ft.colors.WHITE, 'bg': ft.colors.WHITE24},
    {'operador': '=', 'fonte': ft.colors.BLACK, 'bg': ft.colors.ORANGE},
]



def main(page: ft.Page):

    page.update()

    page.window.resizable = False
    page.window.width = 270
    page.window.height = 420
    page.title = 'Calculadora'
    page.bgcolor = 'black'
    page.window.always_on_top = True
    
    def calculate(operador, value_at):
        try:
            value = eval(value_at)

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
            return value
        except:
            return 'Error'
        

    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in {'/', '*', '-','+','.'}:
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±') :
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()
            



    result = ft.Text(value = '0', color = 'white', weight=ft.FontWeight.BOLD, size=30)

    display = ft.Row(
        width=250,
        height=45,
        controls=[
            result,
        ],
        alignment='end',
    )
    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color = btn['fonte'], weight=ft.FontWeight.BOLD),
        width=50,
        height=50,
        bgcolor=btn['bg'],
        border_radius= 80,
        alignment=ft.alignment.center, 
        on_click=select
    ) for btn in btns]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)















  
if __name__ == '__main__':
    ft.app(target=main)