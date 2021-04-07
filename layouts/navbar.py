import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# Appbar
jsc_logo = html.Img(src="assets/logo_jsc.png", height="35px")
fias_logo = html.Img(src="assets/logo_fias_inverse.svg", height="50px")

appbar = dbc.Navbar(
    [
        html.A(
            dbc.NavbarBrand("CoSiMo - Covid Simulation Model", className="ml-2"),
            href="h#",
        ),
        html.A(
            fias_logo,
            href="https://www.fias.science/de/lebenswissenschaften/gruppen/maria-barbarossa/",
            target="_blank",
            className="ml-auto mr-4"
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