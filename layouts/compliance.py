import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from layouts.compliance_widgets import compliance_widgets

compliance_graph_content = dcc.Loading(
    html.Div(
        [
            dbc.Row(
                [
                    html.H5(id="compliance-graph-title", className="card-title"),
                    html.I(
                        className="card-title fa fa-question-circle fa-lg ml-2",
                        id="compliance-graph-target",
                        style={
                            "color": "var(--dark)",
                            "alignSelf": "center"
                        },
                    ),
                    dbc.Tooltip(
                        "Simulated data before and after introduction of control measures \
                        for selected restriction factor and compliance levels.",
                        target="compliance-graph-target",
                        style={"height": "auto"}
                    ),
                ],
                no_gutters=True
            ),
            dcc.Graph(id="compliance-graph", className="w-1")
        ],
        className="mt-4",
        style={"minHeight": "600px"}
    )
)

compliance_barchart_content = dcc.Loading(
    html.Div(
        [
            html.H5(id="compliance-barcharts-title", className="mt-3"),
            html.Div(
                id="compliance-barcharts",
                className="w-1",
                style={"minHeight": "600px"}
            ),
        ],
        className="mt-4"
    )
)

compliance_content = [
    dbc.Card(
        [
            dbc.CardHeader([
                compliance_widgets,
                dbc.Tabs(
                    [
                        dbc.Tab(
                            label="Plot",
                            tab_id="compliance-graph-tab"
                        ),
                        dbc.Tab(
                            label="Daily incidence",
                            tab_id="compliance-barcharts-tab"
                        ),
                    ],
                    id="compliance-tabs",
                    card=True,
                    className="mx-0"
                )
            ]),
            dbc.CardBody(id="compliance-content"),
        ],
        className="my-4"
    )
]