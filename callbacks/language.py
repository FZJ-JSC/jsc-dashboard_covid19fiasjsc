import en_EN

from app import app
from dash.dependencies import Input, Output, State


# Sidebar
# @app.callback(
#     [Output(ID, "children") for ID in en_EN.sidebar],
#     Input("language-en", "n_clicks")
# )
# def set_sidebar_to_EN(n_clicks):
#     return tuple(en_EN.sidebar.values())
