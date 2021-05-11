from layouts.sidebar import *


nav_buttons = [
    create_nav_button("Compliance".upper(), "model-nav", "/",),
]

extra_nav_buttons = [
    create_nav_button("About", "about-nav", "about",),
    create_nav_button("Legal Disclosure", "impressum-nav", "impressum" ),
    create_nav_button("Data Protection", "privacy-nav", "privacy")
]
# Remove margin for last button
extra_nav_buttons[-1].className = "nav-button mx-3"


sidebar = create_sidebar(nav_buttons, extra_nav_buttons)