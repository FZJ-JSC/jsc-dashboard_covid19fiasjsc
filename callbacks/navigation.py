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


nav_items = ["model-nav"]
extra_nav_items = ["impressum-nav", "privacy-nav"]

# Toggle active nav item in sidebar,
# depending on the current url
@app.callback(
    [Output(item, "active") for item in nav_items + extra_nav_items],
    Input('url', 'pathname')
)
def set_active(pathname):
    if pathname.endswith("/_update"):
        return (False,) * 3

    elif pathname.endswith("/impressum"):
        return (False,) * 1 + (True,) + (False,) * 1
    elif pathname.endswith("/privacy"):
        return (False,) * 2 + (True,) + (False,) * 0
    else:
        return (False,) * 0 + (True,) + (False,) * 2
