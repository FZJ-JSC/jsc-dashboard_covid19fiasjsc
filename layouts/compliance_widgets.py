import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import columns, compliance_percentages


def create_formgroup(label, tooltip, widget):
    component_name = label.replace(" ", "-").lower()
    return dbc.FormGroup(
        [
            dbc.Col(
                [
                    label,
                    html.I(
                        className="fa fa-question-circle ml-2",
                        id="{}_target".format(component_name),
                        style={
                            "color": "var(--dark)",
                            "alignSelf": "center"
                        },
                    ),
                    dbc.Tooltip(
                        tooltip, 
                        target="{}_target".format(component_name),
                        style={"height": "auto"}
                    )
                ],
                style={"display": "flex", "alignItems": "center"},
                xs=12, lg=4),
            dbc.Col(
                widget,
                xs=12, lg=8
            )
        ],
        row=True
    )


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()


reduction_dropdown = dcc.Dropdown(
    id="reduction-dropdown",
    clearable=False,
    options=[
        {"label": "0.25", "value": "025"},
        {"label": "0.5", "value": "05"},
        {"label": "0.8", "value": "08"},
    ],
    value="025"
)
reduction_formgroup = create_formgroup(
    "Reduction Factor", lorem_ipsum[:199], reduction_dropdown)


data_dropdown = dcc.Dropdown(
    id="data-dropdown",
    clearable=False,
    options=[
        {"label": columns[key], "value": key}
        for key in columns
    ],
    value="It"
)
data_formgroup = create_formgroup(
    "Plotted Data", lorem_ipsum[:199], data_dropdown)


compliance_dropdown = dcc.Dropdown(
    id="compliance-dropdown",
    options=[
        {"label": "{}%".format(percentage), "value": percentage}
        for percentage in compliance_percentages[1:]
    ],
    value=[10, 30, 50, 70, 100],
    multi=True
)
compliance_tooltip = "Acceptance to comply with regulations"
compliance_formgroup = create_formgroup(
    "Compliance", compliance_tooltip, compliance_dropdown)


def make_accordion_item(title, widgets, short_explanation, component_name):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div(
                    dbc.Row(
                        [
                            html.H5(
                                [
                                    html.I(className="fa fa-cog mr-2"),
                                    title
                                ],
                                className="mb-0"
                            ),
                            dbc.Col(
                                html.I(short_explanation),
                                className="col-lg-auto col-12 order-below"
                            ),
                            html.I(
                                className="fa fa-chevron-down",
                                style={"alignSelf": "center"},
                                id="accordion-group-{}-toggle-icon".format(component_name)
                            ),
                        ],
                        no_gutters=True,
                        justify="between"
                    ),
                    id="accordion-group-{}-toggle".format(component_name)
                ),
                style={
                    "backgroundColor": "transparent",
                    "borderBottom": "None"
                }
            ),
            dbc.Collapse(
                dbc.CardBody(widgets),
                id="accordion-collapse-{}".format(component_name)
            ),
        ],
    )


compliance_widgets = dbc.Row([
    dbc.Col(
        html.H4("Plots", className="card-title"),
        xs=12
    ),
    dbc.Col(
        make_accordion_item("Modelling Scenario",
                            reduction_formgroup,
                            "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
                            "compliance-model"),
        className="mb-3",
        xs=12
    ),
    dbc.Col(
        make_accordion_item("Plot Configuration",
                            [data_formgroup, compliance_formgroup],
                            "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.",
                            "compliance-plot"),
        className="mb-3",
        xs=12
    ),
])