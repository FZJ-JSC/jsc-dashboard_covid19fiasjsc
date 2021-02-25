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
        row=True,
        className="mt-3"
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


column_dropdown = dcc.Dropdown(
    id="column-dropdown",
    clearable=False,
    options=[
        {"label": columns[key], "value": key}
        for key in columns
    ],
    value="It"
)
column_formgroup = create_formgroup(
    "Column", lorem_ipsum[:199], column_dropdown)


compliance_dropdown = dcc.Dropdown(
    id="compliance-dropdown",
    options=[
        {"label": "{}%".format(percentage), "value": percentage}
        for percentage in compliance_percentages[1:]
    ],
    value=[10, 30, 50, 70, 100],
    multi=True
)
compliance_formgroup = create_formgroup(
    "Compliance", lorem_ipsum[:199], compliance_dropdown)


# compliance_widgets = dbc.Row(
#     [
#         dbc.Col(
#             dbc.Card(
#                 dbc.CardBody(
#                     [
#                         html.H5("Modell Parameter", className="card-title"),
#                         reduction_formgroup
#                     ]
#                 ),
#                 className="mb-4"
#             ),
#             xs=12#, xl=8
#         ),
#         dbc.Col(
#             dbc.Card(
#                 dbc.CardBody(
#                     [
#                         html.H5("Graph Parameter", className="card-title"),
#                         column_formgroup,
#                         compliance_formgroup
#                     ]
#                 ),
#                 className="mb-4"
#             ),
#             xs=12#, xl=8
#         ),
#     ],
#     justify="center"
# )

compliance_widgets = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Parameter"),
            html.Hr(),
            html.B("Modell"),
            reduction_formgroup,
            html.Hr(),
            html.B("Graph"),
            column_formgroup,
            compliance_formgroup
        ]
    ),
    className="mb-4"
)

