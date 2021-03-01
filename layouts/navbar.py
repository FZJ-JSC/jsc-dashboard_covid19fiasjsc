import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# Appbar
jsc_logo = html.Img(src="assets/logo_jsc.png", height="30px")
fias_logo = html.Img(src="assets/logo_fias.svg", height="40px")

appbar = dbc.Navbar(
    [
        html.A(
            dbc.NavbarBrand("COVID FIAS JSC", className="ml-2"),
            href="h#",
        ),
        html.A(
            fias_logo,
            href="https://www.fias.science/de/lebenswissenschaften/gruppen/maria-barbarossa/",
            target="_blank",
            className="ml-auto mr-4",
            style={"backgroundColor": "white"}
        ),
        html.A(
            jsc_logo,
            href="https://www.fz-juelich.de/ias/jsc/DE/Home/home_node.html",
            target="_blank"
        )
    ],
    id="navbar",
    color="primary",
    dark=True
)