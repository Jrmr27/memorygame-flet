import flet as ft
from views import Home, Game, Congrats


def views_handler(page: ft.Page):
    # Create TemplateRoute from page.route to can use params
    troute = ft.TemplateRoute(page.route)

    # Route for Home view
    if troute.match('/'):
        return ft.View(
            route=page.route,
            controls=[
                Home(page)
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor='#EDE8EF'
        )
    # Route for Game view
    elif troute.match('/game'):
        return ft.View(
            route=page.route,
            controls=[
                Game(page)
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor='#EDE8EF'
        )
    # Route for Congrats view
    elif troute.match('/congrats/:matches/:errors'):
        return ft.View(
            route=page.route,
            controls=[
                Congrats(page, troute.matches, troute.errors)
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor='#EDE8EF'
        )
