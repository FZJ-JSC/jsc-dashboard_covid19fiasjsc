import dash_bootstrap_components as dbc
import dash_html_components as html


def create_nav_button(title, name, href):
    return dbc.Button(
        title,
        id=name,
        href=href,
        color="dark",
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
        color="dark",
        className="nav-button mb-4 mx-3"
    )


nav_buttons = [
    create_nav_button("Modelle", "modell-nav", "/"),
    create_nav_button("Fragen&Antworten", "qa-nav", "faq"),
    create_external_link("Quellcode", "source-nav",
                         href="https://github.com/FZJ-JSC/jsc-dashboard_covid19fiasjsc")
]


sidebar = html.Div(
    [
        dbc.NavbarToggler(
            html.Span(className="navbar-toggler-icon"),
            id="sidebar-toggle"),
        dbc.Collapse(
            dbc.Nav(
                nav_buttons,
                vertical=True
            ),
            id="sidebar-collapse",
            navbar=True,
        ),
    ],
    id="sidebar"
)


