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


def create_sidebar(nav_btns, extra_nav_btns):
    return html.Div(
        [
            dbc.NavbarToggler(
                html.Span(className="navbar-toggler-icon"),
                id="sidebar-toggle"),
            dbc.Collapse(
                dbc.Nav(
                    nav_btns + 
                    [
                        html.Div(style={"flexGrow": "1"}),
                        html.Br()
                    ] +
                    extra_nav_btns,
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
        style={
            "paddingTop": "calc(2rem + 68px)",
            "width": "194px"
        }
    )


