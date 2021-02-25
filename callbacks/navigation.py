import dash

from app import app
from dash.dependencies import Input, Output, State


# Toggle navigation menu
@app.callback(
    Output("sidebar-collapse", "is_open"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


nav_items = ["modell-nav", "qa-nav",  "source-nav"]


# Toggle active nav item in sidebar,
# but not if external link is clicked
@app.callback(
    [Output(nav_items[0], "active"),
     Output(nav_items[1], "active")],
    [Input(nav_items[0], "n_clicks"),
     Input(nav_items[1], "n_clicks")]
)
def set_active(btn1, btn2):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True, False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == nav_items[0]:
        return True, False
    elif button_id == nav_items[1]:
        return False, True
    else:
        return False, False
