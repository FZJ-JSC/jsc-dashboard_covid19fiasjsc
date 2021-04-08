import dash_bootstrap_components as dbc
import dash_html_components as html


def create_nav_button(title, name, href, icon=None):
    if icon:
        children = [
            html.I(
                className="fa fa-{} fa-lg mr-2".format(icon),
            ),
            title.upper(),
        ]
    else:
        children = title
    
    return dbc.Button(
        children,
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
    create_nav_button("Compliance", "model-nav", "/", icon="home"),
]

extra_nav_buttons = [
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
                    html.Div(style={"flexGrow": "1"}),
                    html.Br()
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
    style={"paddingBottom": "2rem"}
)


