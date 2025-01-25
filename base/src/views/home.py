import flet as ft


class Home(ft.Column):

    def __init__(self, page: ft.Page):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page


    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE
    def build(self):
        # Header text
        header_image = ft.Container(
            content=ft.Image(
                src="/images/cover.png",
                fit=ft.ImageFit.CONTAIN,
                width=400,
                height=400
            ),
            alignment=ft.alignment.center
        )
        
        def go_to_game(self):
            self.page.go('/game')

        # Play button
        play_button = ft.Container(
            content=ft.Text('Jugar',
                            size=30,
                            color="#000000"
                            ),
            alignment=ft.alignment.center,
            bgcolor="#FFA500",
            border=ft.border.all(5, "#000000"),
            width=150,
            height=50,
            border_radius=10,
            on_click=go_to_game
        )

        self.controls = [
            header_image,
            play_button
        ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER