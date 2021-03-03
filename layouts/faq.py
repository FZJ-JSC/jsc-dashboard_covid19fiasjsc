import dash_bootstrap_components as dbc
import dash_html_components as html


def make_accordion_item(i, title, text, component_name):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div(
                    dbc.Row(
                        [
                            title,
                            html.I(
                                className="fa fa-chevron-down",
                                style={"alignSelf": "center"},
                                id=f"{component_name}-accordion-group-{i}-toggle-icon"
                            ),
                        ],
                        no_gutters=True,
                        justify="between"
                    ),
                    id=f"{component_name}-accordion-group-{i}-toggle",
                ),
                style={"backgroundColor": "transparent"}
            ),
            dbc.Collapse(
                dbc.CardBody(
                    text,
                    className="bg-light",
                    style={"borderTop": "1px solid rgba(0, 0, 0, 0.125)"}
                ),
                id=f"{component_name}-accordion-collapse-{i}",
            ),
        ]
    )


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()

model_accordion = html.Div(
    [
        dbc.Card(
            dbc.CardHeader(
                html.H4("About the model"),
            ),
            className="bg-light"
        ),
        make_accordion_item(
            1, "What are the strengths of this model?", 
            lorem_ipsum[:199],
            "model"
        ),
        make_accordion_item(
            2, "What are the weaknesses of this model?", 
            lorem_ipsum[:199],
            "model"
        ),
        make_accordion_item(
            3, "Question 3", 
            lorem_ipsum[:199],
            "model"
        ),
    ],
    className="accordion"
)

other_accordion = html.Div(
    [
        dbc.Card(
            dbc.CardHeader(
                html.H4("Other"),
            ),
            className="bg-light"
        ),
        make_accordion_item(
            1, "Who contributed to this model?", 
            lorem_ipsum[:199],
            "other"
        ),
    ],
    className="accordion mt-4"
)