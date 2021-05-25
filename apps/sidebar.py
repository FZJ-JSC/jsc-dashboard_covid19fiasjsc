import en_EN
from layouts.sidebar import *


TEXT = en_EN.sidebar


nav_buttons = [
    create_nav_button(TEXT["compliance"], "model-nav", "/",),
]

extra_nav_buttons = [
    create_nav_button(TEXT["about"], "about-nav", "about",),
    create_nav_button(TEXT["impressum"], "impressum-nav", "impressum" ),
    create_nav_button(TEXT["privacy"], "privacy-nav", "privacy")
]
# Remove margin for last button
extra_nav_buttons[-1].className = "nav-button mx-3"


sidebar = create_sidebar(nav_buttons, extra_nav_buttons)