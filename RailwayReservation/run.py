from main import *

menu_options = [
    {
        'option': 1,
        'name': 'Create user',
    },
]

create_user_menu(menu_options)
option = ask_for_option()
run_option(option)
