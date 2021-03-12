import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import callbacks
import os  # temporary import for jupyterhub service prefix

from app import app, dataframes
from apps import faq, info, legal, models

from layouts.navbar import appbar
from layouts.sidebar import sidebar
from layouts.compliance import compliance_graph_content, compliance_barchart_content


layout_index = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(
            [
                # Navbar
                appbar,
                # Store data
                dcc.Store(
                    id="dataframes",
                    data=dataframes,
                    storage_type="session"
                ),
                # Body
                html.Div(
                    [
                        # Sidebar
                        sidebar,
                        # Page content
                        dbc.Col(
                            id="page-content",
                        )
                    ],
                    style={
                        "display": "flex",
                        "flexGrow": "1"
                    }
                )
            ],
            style={
                "display": "flex",
                "flexDirection": "column",
                "flexGrow": "1"
            }
        )
    ],
    style={
        "display": "flex",
        "height": "100%"
    }
)

app.layout = layout_index

# "Complete" layout to avoid callback errors
# because components are not loaded on the initial page
app.validation_layout = html.Div(
    [
        layout_index,
        html.Div(models.children),
        html.Div([compliance_graph_content, compliance_barchart_content]),
        html.Div(info.children),
        html.Div(faq.children),
    ]
)


# Change page depending on URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):   
    if pathname.endswith("/information"):
        return info.children

    elif pathname.endswith("/faq"):
        return faq.children

    elif pathname.endswith("/about"):
        return []

    elif pathname.endswith("/disclaimer"):
        return legal.disclaimer

    elif pathname.endswith("/impressum"):
        return legal.impressum

    elif pathname.endswith("/privacy"):
        return legal.privacy

    else:
        return models.children


if __name__ == '__main__':
    app.run_server(debug=True)