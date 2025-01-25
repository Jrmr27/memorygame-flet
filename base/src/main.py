import flet as ft
from utils import customize_page, views_handler


def main(page: ft.Page):
    # Customize page settings
    customize_page(
        page=page,
        title='Memorama de Emojis',
        window_maximizable=False,
        window_resizable=False,
        theme_mode='light',
        height=800,
        width=1200
    )

    # Define on route change function. To "navigate" between pages we used
    # page.go(route) - a helper method that updates page.route, calls
    # page.on_route_change event handler to update views and finally calls
    # page.update().

    def route_change(e):
        page.views.clear()
        page.views.append(
            views_handler(page)
        )
        page.update()

    # Define on view pop function. It fires when the user clicks automatic
    # "Back" button in AppBar control.
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Set on_route_change and on_view_pop for page
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Go to home page (/)
    page.go(page.route)


ft.app(target=main, view=ft.AppView.FLET_APP)
