import dash_bootstrap_components as dbc
import dash_html_components as html


def create_nav_button(title, name, href):
    return dbc.Button(
        title,
        id=name,
        href=href,
        color="light",
        className="nav-button mb-4 mx-3"
)


def create_external_link(title, name, href):
    return dbc.Button(
        [
            title,
            html.I(className="fa fa-external-link-alt ml-2")
        ],
        id=name,
        href=href,
        target="_blank",
        color="light",
        className="nav-button mb-4 mx-3"
    )


nav_buttons = [
    create_nav_button("Models", "model-nav", "/"),
    create_nav_button("Background Information", "info-nav", "information"),
    create_nav_button("FAQ", "qa-nav", "faq"),
    create_nav_button("About Us", "about-nav", "about"),
    create_external_link("Source Code", "source-nav",
                         href="https://github.com/FZJ-JSC/jsc-dashboard_covid19fiasjsc")
]

extra_nav_buttons = [
    create_nav_button("Disclaimer", "disclaimer-nav", "disclaimer"),
    create_nav_button("Legal Disclosure", "impressum-nav", "impressum"),
    create_nav_button("Data Protection", "privacy-nav", "privacy")
]


sidebar = html.Div(
    [
        dbc.NavbarToggler(
            html.Span(className="navbar-toggler-icon"),
            id="sidebar-toggle"),
        dbc.Collapse(
            dbc.Nav(
                nav_buttons + 
                [
                    html.Div(style={"flexGrow": "1"})
                ] +
                extra_nav_buttons,
                vertical=True,
                className="h-1 flex-nowrap"
            ),
            id="sidebar-collapse",
            navbar=True,
            className="h-1",
            style={"overflow": "auto"}
        ),
    ],
    id="sidebar",
#     style={"paddingBottom": "calc(56px + 2rem)"}
)


