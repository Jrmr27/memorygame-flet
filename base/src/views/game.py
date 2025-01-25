import random
import time
import threading

import flet as ft

from .card import Card


class Game(ft.Container):
    def __init__(self, page: ft.Page):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

        # CLASS VARIABLES
        self.n_pairs = 10  # Number of card pairs (int)
        self.card_images_indexes = []  # List of indexes of card images (list)
        self.cards = []  # List of Cards (list)

        self.matches = None  # Number of matches between cards (int)
        self.errors = None  # Number of errors during the game (int)

        self.selected_card = None  # First card selected from the pair (Card)
        # List of identifiers for those pairs of cards already found (list)
        self.cards_ids_matched = []

        self.__initialize_game()

    # DON´T TOUCH THIS FUNCTION
    def did_mount(self):
        self.running = True
        self.th = threading.Thread(
            target=self.__game_logic, args=(), daemon=True)
        self.th.start()

    # DON´T TOUCH THIS FUNCTION
    def __game_logic(self) -> None:
        # Loop inside while the number of found matches is different to the
        # total number of pairs
        while self.matches != self.n_pairs and self.running:
            for card in self.cards:
                if card.content == card.frontside:
                    self.__is_a_match(card)

        # The game is over
        self.running = False
        print('Game Over!')
        time.sleep(1)

        # Go to Congrats view
        self.page.go(f'/congrats/{self.matches}/{self.errors}')

    # TODO: FUNCTION TO INITIALIZE THE CLASS VARIABLES OF THE GAME
    def __initialize_game(self):
        self.matches = 0
        self.errors = 0
        self.card_images_indexes = random.sample(range(0, 20), self.n_pairs)
        self.cards = [
            Card(self.page, 0, self.card_images_indexes[0]),
            Card(self.page, 1, self.card_images_indexes[0]),
            Card(self.page, 2, self.card_images_indexes[1]),
            Card(self.page, 3, self.card_images_indexes[1]),
            Card(self.page, 4, self.card_images_indexes[2]),
            Card(self.page, 5, self.card_images_indexes[2]),
            Card(self.page, 6, self.card_images_indexes[3]),
            Card(self.page, 7, self.card_images_indexes[3]),
            Card(self.page, 8, self.card_images_indexes[4]),
            Card(self.page, 9, self.card_images_indexes[4]),
            Card(self.page, 10, self.card_images_indexes[5]),
            Card(self.page, 11, self.card_images_indexes[5]),
            Card(self.page, 12, self.card_images_indexes[6]),
            Card(self.page, 13, self.card_images_indexes[6]),
            Card(self.page, 14, self.card_images_indexes[7]),
            Card(self.page, 15, self.card_images_indexes[7]),
            Card(self.page, 16, self.card_images_indexes[8]),
            Card(self.page, 17, self.card_images_indexes[8]),
            Card(self.page, 18, self.card_images_indexes[9]),
            Card(self.page, 19, self.card_images_indexes[9]),
        ]
        random.shuffle(self.cards)

        self.text_matches = ft.Text(f"Matches: {self.matches}", color="green", size=20)
        self.text_errors = ft.Text(f"Errors: {self.errors}", color="red", size=20)

    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE

    def build(self):
        self.content = ft.Column(
            controls=[
                # This control is for the Header section
                ft.Row(
                    controls=[
                        self.text_matches,
                        self.text_errors,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
                ft.Divider(thickness=5),
                # The next control in for the cards container
                ft.Container(
                    content=ft.Row(
                        controls=self.cards,
                        alignment=ft.MainAxisAlignment.CENTER,
                        wrap=True,
                    ),
                    width=650
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        return self #return self statement

    # TODO: FUNCTION TO UPDATE THE VALUES OF THE NUMBER OF MATCHES AND ERRORS

    def __update_texts(self) -> None:
        self.content.controls[0].controls[0].value = f"Matches: {self.matches}"
        self.content.controls[0].controls[1].value = f"Errors: {self.errors}"
        self.page.update()

    # TODO: FUNCTION TO CHECK IF EXISTS A MATCH BETWEEN THE PREVIOUS SELECTED CARD AND THE NEW SELECTION
    def __is_a_match(self, card: Card) -> None:
        if self.selected_card is None:
            self.selected_card = card
        else:
            if self.selected_card.id != card.id:  # NOT comparing the same card and count it as match or error
                if self.selected_card.image_path == card.image_path:
                    self.matches += 1
                    self.cards_ids_matched.extend([self.selected_card.id, card.id])
                    self.selected_card.change_fronside_bgcolor('#898989')
                    card.change_fronside_bgcolor('#898989')
                    self.selected_card.disable_card()
                    card.disable_card()
                    
                    #verification for the game to be ended (being able to go to the congrats page, the next one)
                    if self.matches == self.n_pairs: #if we get all the pairs matched between them correctly (comparation)
                        self.running = False #we stop running the game.py page (with the asignation)

                else:
                    self.errors += 1
                    self.__disable_all_remaining_cards()
                    time.sleep(1)
                    self.selected_card.animate_card()
                    card.animate_card()
                    self.__enable_all_remaining_cards()
            
                self.__update_texts()
                self.selected_card = None


    # TODO: FUNCTION TO DISABLE ALL REMAINING CARDS

    def __disable_all_remaining_cards(self) -> None:
        for card in self.cards:
            #we disable the cards that are not being used
            if card.id not in self.cards_ids_matched:
                card.disable_card()

    # TODO: FUNCTION TO ENABLE ALL REMAINING CARDS
    def __enable_all_remaining_cards(self) -> None:
        for card in self.cards:
            if card.id not in self.cards_ids_matched:
                card.enable_card()

    # DON´T TOUCH THIS FUNCTION

    def __game_logic(self) -> None:
        # Loop inside while the number of found matches is different to the
        # total number of pairs
        while self.matches != self.n_pairs and self.running:
            for card in self.cards:
                if card.content == card.frontside:
                    self.__is_a_match(card)

        # The game is over
        self.running = False
        print('Game Over!')
        time.sleep(1)

        # Go to Congrats view
        self.page.go(f'/congrats/{self.matches}/{self.errors}')