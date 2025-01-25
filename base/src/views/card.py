import flet as ft


class Card(ft.AnimatedSwitcher):
    def __init__(self, page: ft.Page, id: int, image_index: int):
        # Save page as class variable
        self.page = page

        # Class Variables
        self.id = id
        self.image_path = f'assets/images/{image_index}.png'

        # Front part of the card (Emoji)
        self.f_bgcolor = '#5db7fc'  # Blue
        self.frontside = self.__create_card_container(self.f_bgcolor,
                                                      self.image_path)

        # Back part of the card
        self.b_bgcolor = '#ff7200'  # Orange
        self.backside = self.__create_card_container(self.b_bgcolor, None)

        # Call super constructor
        super().__init__(content=self.backside)

        # Animator for back side and front side of the card
        self.transition=ft.AnimatedSwitcherTransition.FADE
        self.duration=500

    # TODO: FUNCTION THAT RETURNS THE FRONT OR BACK SIDE OF THE CARD, DEPENDING ON THE bgcolor PARAMETER
    def __create_card_container(self, bgcolor: str, image_path: str = None) -> ft.Control:
        container = ft.Container(
            width=120,
            height=150,
            bgcolor=bgcolor,
            border_radius=10,
            alignment=ft.alignment.center,
            content=None if image_path is None else ft.Image(src=image_path),
            on_click=lambda _: self.animate_card()

        )
        return container

    # TODO: FUNCTION NEEDED FOR THE AnimatedSwiteche TO ANIMATE THE TRANSITION BETWEEN THE FRONT AND THE BACK SIDES OF THE CARD
    def animate_card(self) -> None:
        #self.content = self.frontside if self.content == self.backside else self.backside
        if self.content == self.backside:
            self.content = self.frontside
        else:
            self.content = self.backside
        self.update()
        #self.page.update()

    # TODO: FUNCTION TO ENABLE THE CARD AND ALLOW IT TO BE PRESSED
    def enable_card(self) -> None:
        #self.on_click = lambda e: self.animate_card()
        self.backside.on_click = lambda _: self.animate_card()

    # TODO: FUNCTION TO DISABLE THE CARD AND NOT ALLOW IT TO BE PRESSED
    def disable_card(self) -> None:
        #self.on_click = None
        self.backside.on_click = None
        self.frontside.on_click = None

    # TODO: FUNCTION TO CHANGE THE bgcolor OF THE FRONT SIDE OF THE CARD
    def change_fronside_bgcolor(self, bgcolor: str = '#898989') -> None:
        self.f_bgcolor = bgcolor
        self.frontside = self.__create_card_container(self.f_bgcolor, self.image_path)
        if self.content == self.frontside:
            self.content = self.frontside
            self.update()
        #self.page.update()