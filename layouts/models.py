import dash_bootstrap_components as dbc
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


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()

models_explanation = dbc.Card(
    dbc.CardBody(
        [
            html.H4(
                "What is the compliance model?",
                className="card-title",
                id="model-text-title"),
            html.P(lorem_ipsum[:199], id="model-text"),
            dbc.Button("...more", color="primary", id="model-text-toggle"),
        ],
    ),
    className="w-1"
)