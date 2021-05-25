import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from git import Git

import callbacks

from app import app, dataframes
from apps.appbar import appbar
from apps.sidebar import sidebar
from apps.de import compliance as compliance_de
from apps.de import other as other_de
from apps.en import compliance as compliance_en
from apps.en import other as other_en


app_layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id="resize-dummy-1"),
        html.Div(id="resize-dummy-2"),
        html.Div(id="resize-dummy-3"),
        html.Div(id="resize-dummy-4"),
        html.Div(
            [
                # Navbar
                appbar,
                # Store data
                dcc.Store(
                    id="dataframes-de",
                    storage_type="session"
                ),
                dcc.Store(
                    id="dataframes-en",
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
    compliance_de.page,
    compliance_de.graph_content,
    compliance_de.barchart_content,
    compliance_en.page,
    compliance_en.graph_content,
    compliance_en.barchart_content
])


# Change page depending on URL
# and language setting
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname.endswith("/_update"):
        # Update simdata via git pull
        g = Git("../simdata")
        output = g.pull('origin','master')
        return dbc.Container(output)

    elif pathname.endswith("/de/about"):
        return other_de.about_page

    elif pathname.endswith("/de/impressum"):
        return other_de.impressum_page

    elif pathname.endswith("/de/privacy"):
        return other_de.privacy_page

    elif pathname.startswith("/de"):
        return compliance_de.page

    elif pathname.endswith("/about"):
        return other_en.about_page

    elif pathname.endswith("/impressum"):
        return other_en.impressum_page

    elif pathname.endswith("/privacy"):
        return other_en.privacy_page

    else:
        return compliance_en.page


if __name__ == '__main__':
    app.run_server(debug=True)