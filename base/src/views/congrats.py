import flet as ft


class Congrats(ft.Column):

    def __init__(self, page: ft.Page, matches: int, errors: int):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

        # Class Variables
        self.matches = matches
        self.errors = errors

    # TODO: WRITEN THE CONTROLS STRUCTURE BELOW
    def build(self):
        # Congratulations image imported locally
        congrats_image = ft.Container(
            content=ft.Image(
                src="/images/congrats.png", #we access the right directory to use it in the same program
                fit=ft.ImageFit.CONTAIN,
                width=600,
                height=575 
            ),
            alignment=ft.alignment.center, #centered the image horizontally on the screen page
            margin=ft.margin.only(bottom=0) 
        )

        #STATS ROW
        stats_row = ft.Row(
            controls=[
                ft.Text(
                    f"Matches: {self.matches}", #matches text + value from game.py
                    color="green", #color of the text
                    size=20, #tall...
                    weight=ft.FontWeight.BOLD #written in bold to make it thicker
                ),
                #vertical line between the matches & errors
                ft.Text(" | ",
                        size=27,
                        weight=ft.FontWeight.BOLD), #also bold for thickness
                ft.Text(
                    f"Errors: {self.errors}", #error text + value from game.py of final errors counted
                    color="red", #in red
                    size=20, #same size as the matches text
                    weight=ft.FontWeight.BOLD #bold x2
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER #located the 3 stats on the center horizontally
        )
        #DIVIDER (between the stats row & buttons below)
        divider = ft.Divider(
            height=20,
            color=ft.colors.GREY_400, #color more adjusted to the one seen
            thickness=5 #height of the divider
        )

        #BUTTONS ROW
        buttons_row = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.HOME, #icon required
                                    color="green", #in green as the text
                                    size=50), #bigger than the text 
                            ft.Text("Go Home", #the corresponding text
                                    size=20, #smaller than the icom
                                    weight=ft.FontWeight.BOLD) #in bold like the output shown in the guide
                        ],
                        spacing=5 #space between them
                    ),
                    on_click=lambda _: self.page.go("/") #action: click ==> we go to the home page B)
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[ #dif icon and text, similar structure
                            ft.Icon(name=ft.icons.REFRESH,
                                    color="orange",
                                    size=50),
                            ft.Text("Restart Game",
                                    size=20,
                                    weight=ft.FontWeight.BOLD)
                        ],
                        spacing=5
                    ),
                    on_click=lambda _: self.page.go("/game") #action: click ==> we are directed to the game page :D
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[ #similar x3
                            ft.Icon(name=ft.icons.POWER_SETTINGS_NEW,
                                    color="red",
                                    size=50),
                            ft.Text("End Game",
                                    size=20,
                                    weight=ft.FontWeight.BOLD)
                        ],
                        spacing=5
                    ),
                    on_click=lambda _: self.page.window_close() #action: click ==> the running ends and the window of the program pages is closed automatically :v
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,#type of space between the buttons (better this one 4 being more unified but separated horizontaly)
            spacing=20 #marging btwn the 3 buttons horizontally
        )

        #FINAL STRUCTURE (it contains all of the elements declared by rows during the code ==> defines their vertical display height on the page layout)
        self.controls = [
            congrats_image, #1º the image
            stats_row, #2º the 2 texts with the matches and errors and the "|" btwn them
            divider,#the divider
            buttons_row #the 3 action buttons
        ]
        
        self.spacing = 10 #vertical space btwn elements
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER #page alignment horizontally