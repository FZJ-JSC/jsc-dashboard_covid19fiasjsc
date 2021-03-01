import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import callbacks
import os  # temporary import for jupyterhub service prefix

from app import app, dataframes
from apps import faq, legal, models

from layouts.navbar import appbar
from layouts.sidebar import sidebar


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
        html.Div(faq.children),
    ]
)


# Change page depending on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):   
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/information" \
    or pathname == "/information":
        return []
    
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/faq" \
    or pathname == "/faq":
        return faq.children
    
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/about" \
    or pathname == "/about":
        return []
    
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/disclaimer" \
    or pathname == "/disclaimer":
        return legal.disclaimer
    
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/impressum" \
    or pathname == "/impressum":
        return legal.impressum
    
    if pathname == os.environ["JUPYTERHUB_SERVICE_PREFIX"]+"proxy/5099/privacy" \
    or pathname == "/privacy":
        return legal.privacy
    
    else:
        return models.children


# if __name__ == '__main__':
#     app.run_server(debug=True)