import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def create_modell_button(title, component):
    return dbc.Button(
        title,
        id="{}-button".format(component),
        className="nav-button light mx-2 mb-3"
    )


modell_buttons = [
    create_modell_button("Compliance Model", "compliance"),
    create_modell_button("Vaccination Model", "vaccination"),
    create_modell_button("Hospitalization Model", "hospitalization")
]

models_selection = dbc.Row(
    modell_buttons,
    no_gutters=True,
    justify="center",
    className="nav-row"
)


with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

models_explanation = html.Div([
    dbc.Card(
        html.H3(
            "Compliance model",
            className="mb-0 bold text-center",
            id="model-text-title"
        ),
        body=True,
        className="my-4"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Div(
                        dcc.Markdown(compliance_short),
                        id="model-text"
                    ),
                    dbc.Button("...more", color="primary", id="model-text-toggle"),
                ],
            ),
        ],
        className="w-1"
    )
])