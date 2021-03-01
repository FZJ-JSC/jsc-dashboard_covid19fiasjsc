import dash_core_components as dcc
import dash_html_components as html

from layouts.compliance_widgets import compliance_widgets

compliance_content = [
    compliance_widgets,
    dcc.Loading(
        html.Div(
            [
                html.H5(id="graph-title"),
                dcc.Graph(id="graph", className="w-1")
            ],
            style={"padding": "1.25rem"}
        )
    ),
    dcc.Loading(
        html.Div(
            [
                html.H5(id="barcharts-title", className="mt-3"),
                html.Div(id="barcharts", className="w-1"),
            ],
            style={"padding": "1.25rem"}
        )
    )
]