import dash_bootstrap_components as dbc
import dash_core_components as dcc


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()


def create_info_button(title, component):
    return dbc.Button(
        title,
        id="{}-button".format(component),
        className="nav-button light mx-2 mb-3"
    )


info_buttons = [
    create_info_button("Calibrated vs Abstract Models", "model-info"),
    create_info_button("Publications", "publications"),
    create_info_button("Press Releases", "press")
]

info_selection = dbc.Row(
    info_buttons,
    no_gutters=True,
    justify="center",
    className="nav-row"
)

info_content = dbc.Card(
    dbc.CardBody(
        dcc.Markdown(lorem_ipsum[:199]),
        id="info-content"
    )
)
