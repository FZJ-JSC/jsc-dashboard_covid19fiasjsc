import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import initial_fig
from layouts.compliance_widgets import compliance_widgets


compliance_graph_content = dcc.Loading(
    html.Div(
        [
            dbc.Row(
                [
                    html.H5(
                        "Visualize known active cases (for contact reduction factor 0.25)", 
                        id="compliance-graph-title", 
                        className="card-title bold"
                    ),
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
            dcc.Graph(figure=initial_fig, id="compliance-graph", className="w-1")
        ],
        className="mt-4",
        style={"minHeight": "600px"}
    )
)

compliance_barchart_content = dcc.Loading(
    html.Div(
        [
            html.H5(id="compliance-barcharts-title", className="mt-3 bold"),
            html.Div(
                id="compliance-barcharts",
                className="w-1",
                style={"minHeight": "600px"}
            ),
        ],
        className="mt-4"
    )
)


with open("./texts/compliance/en/plots-explanation.md") as f:
    plots_explanation = f.read()

compliance_plots_explanation = dbc.Card(
    dbc.CardBody([
        dcc.Markdown(plots_explanation),
        compliance_widgets
    ]),
    className="mt-4",
    style={"borderBottom": "none"}
)


compliance_content = [
    compliance_plots_explanation,
    dbc.Tabs(
        [
            dbc.Tab(
                label="Selected output",
                tabClassName="bold",
                tab_id="compliance-graph-tab"
            ),
            dbc.Tab(
                label="Corresponding daily incidence",
                tabClassName="bold",
                tab_id="compliance-barcharts-tab"
            ),
        ],
        id="compliance-tabs",
        card=True,
        className="mx-0"
    ),
    dbc.CardBody(
        id="compliance-content",
        style={
            "border": "1px solid #e7eaed", 
            "borderTop": "None"
        }
    ),
]