import dash_bootstrap_components as dbc
import dash_html_components as html


def create_modell_button(title, component):
    return dbc.Button(
        title,
        id="{}-button".format(component),
        className="nav-button light mx-2"
    )


modell_buttons = [
    create_modell_button("Compliance Modell", "compliance"),
    create_modell_button("Impfung Modell", "impfung"),
    create_modell_button("Hospitalisierung Modell", "hospitalisierung")
]

models_selection = dbc.Row(
    modell_buttons,
    no_gutters=True,
    justify="center",
    className="nav-row",
)


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()

models_explanation = dbc.Card(
    dbc.CardBody(
        [
            html.H5(
                "What is the compliance modell?",
                className="card-title",
                id="model-text-title"),
            html.P(lorem_ipsum[:199], id="model-text"),
            dbc.Button("...more", id="model-text-toggle"),
        ],
    ),
    className="w-1 my-4"
)