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
        html.Div(
            fias_logo, 
            className="ml-auto mr-4",
            style={"backgroundColor": "white"}),
        jsc_logo
    ],
    id="navbar",
    color="dark",
    dark=True
)


def create_modal_footer_content(component_name, modal_title, markdown):
    return html.Div(
        [
            dbc.Button(
                component_name.capitalize(),
                id="{}_modal_open".format(component_name),
                # outline=True,
                color="light",
                className="ml-2"
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(modal_title),
                    dbc.ModalBody(
                        dcc.Markdown(markdown),
                        style={"overflow": "auto"}
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Schließen",
                            id="{}_modal_close".format(component_name),
                            className="ml-auto"
                        )
                    )
                ],
                id="{}_modal".format(component_name),
                size="xl"
            )
        ]
    )


# Impressum
with open("texts/impressum.md") as md_file:
    impressum_md = md_file.read()
impressum_modal = create_modal_footer_content(
    "impressum", "Impressum und Haftungsausschluss", impressum_md)

# Datenschutzerklärung
with open("texts/datenschutzerklaerung.md") as md_file:
    datenschutz_md = md_file.read()
datenschutz_modal = create_modal_footer_content(
    "datenschutz", "Datenschutzerklärung", datenschutz_md)

# Footer
footer = dbc.NavbarSimple(
    [
        dbc.NavItem(impressum_modal),
        dbc.NavItem(datenschutz_modal),
    ],
    color="light"
)