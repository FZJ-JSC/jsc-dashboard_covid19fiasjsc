import dash_core_components as dcc
import dash_html_components as html

from layouts.models import models_selection, models_explanation
from layouts.widgets import compliance_widgets

children = [
    # Navigation between models
    models_selection,
    # Model explanation
    models_explanation,
    # Page content
    compliance_widgets,
    dcc.Loading(
        html.Div(
            [
                html.H5(id="graph-title"),
                dcc.Graph(id="graph", style={"width": "100%"})
            ],
            style={"padding": "1.25rem"}
        )
    ),
    dcc.Loading(
        html.Div(
            [
                html.H5(id="barcharts-title", className="mt-3"),
                html.Div(id="barcharts", style={"width": "100%"}),
            ],
            style={"padding": "1.25rem"}
        )
    )
]