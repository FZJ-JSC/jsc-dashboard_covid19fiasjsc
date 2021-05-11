import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from git import Git

import callbacks

from app import app, dataframes
from apps.en import compliance, other
from apps.appbar import appbar
from apps.sidebar import sidebar


app_layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id="resize-dummy-1"),
        html.Div(id="resize-dummy-2"),
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
                            style={"paddingTop": "calc(2rem + 68px)"}
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
app.layout = app_layout

app.validation_layout = html.Div([
    app_layout,
    compliance.page,
    compliance.graph_content,
    compliance.barchart_content
])


# Change page depending on URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname.endswith("/_update"):
        # Update simdata via git pull
        g = Git('../simdata')
        output = g.pull('origin','master')
        return dbc.Container(output)

    elif pathname.endswith("/about"):
        return other.about_page

    elif pathname.endswith("/impressum"):
        return other.impressum_page

    elif pathname.endswith("/privacy"):
        return other.privacy_page

    else:
        return compliance.page


if __name__ == '__main__':
    app.run_server(debug=True)