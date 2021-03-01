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


nav_items = ["model-nav", "info-nav", "qa-nav", "about-nav", "source-nav"]
extra_nav_items = ["disclaimer-nav", "impressum-nav", "privacy-nav"]

# Toggle active nav item in sidebar,
# but not if external link is clicked
@app.callback(
    [Output(item, "active") for item in nav_items + extra_nav_items],
    [Input(item, "n_clicks") for item in nav_items + extra_nav_items]
)
def set_active(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8):
    ctx = dash.callback_context

    if not ctx.triggered:
        return (True,) + (False,) * 7
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == nav_items[0]:
        return (False,) * 0 + (True,) + (False,) * 7
    elif button_id == nav_items[1]:
        return (False,) * 1 + (True,) + (False,) * 6
    elif button_id == nav_items[2]:
        return (False,) * 2 + (True,) + (False,) * 5
    elif button_id == nav_items[3]:
        return (False,) * 3 + (True,) + (False,) * 4
    elif button_id == nav_items[4]:
        return (False,) * 4 + (True,) + (False,) * 3
    elif extra_nav_items == nav_items[0]:
        return (False,) * 5 + (True,) + (False,) * 2
    elif extra_nav_items == nav_items[1]:
        return (False,) * 6 + (True,) + (False,) * 1
    elif extra_nav_items == nav_items[2]:
        return (False,) * 7 + (True,) + (False,) * 0
    else:
        return (False,) * 8
