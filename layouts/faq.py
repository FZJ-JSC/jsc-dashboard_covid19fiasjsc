import dash_bootstrap_components as dbc
import dash_html_components as html


def make_accordion_item(i, title, text):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div(
                    dbc.Row(
                        [
                            title,
                            html.I(
                                className="fa fa-chevron-down",
                                style={
                                    "color":"var(--secondary)",
                                    "alignSelf": "center"
                                },
                                id=f"accordion-group-{i}-toggle-icon"
                            ),
                        ],
                        no_gutters=True,
                        justify="between"
                    ),
                    id=f"accordion-group-{i}-toggle",
                ),
                style={"backgroundColor": "transparent"}
            ),
            dbc.Collapse(
                dbc.CardBody(text),
                id=f"accordion-collapse-{i}",
            ),
        ]
    )


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()


accordion = html.Div(
    [
        make_accordion_item(1, "Question 1", lorem_ipsum[:199]), 
        make_accordion_item(2, "Question 2", lorem_ipsum[:199]), 
        make_accordion_item(3, "Question 3", lorem_ipsum[:199]), 
    ], 
    className="accordion my-4"
)


title = dbc.Row(
    html.H5("FAQ"),
    no_gutters=True,
    justify="center",
    className="nav-row",
)