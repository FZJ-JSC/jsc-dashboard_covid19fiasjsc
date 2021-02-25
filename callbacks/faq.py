import dash

from app import app
from dash.dependencies import Input, Output, State


@app.callback(
    [Output(f"accordion-collapse-{i}", "is_open") for i in range(1, 4)] +
    [Output(f"accordion-group-{i}-toggle-icon", "className") for i in range(1, 4)],
    [Input(f"accordion-group-{i}-toggle", "n_clicks") for i in range(1, 4)],
    [State(f"accordion-collapse-{i}", "is_open") for i in range(1, 4)] +
    [State(f"accordion-group-{i}-toggle-icon", "className") for i in range(1, 4)],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3, icon1, icon2, icon3):
    ctx = dash.callback_context

    down = "fa fa-chevron-down"
    up = "fa fa-chevron-up"

    if not ctx.triggered:
        return False, False, False, down, down, down
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "accordion-group-1-toggle" and n1:
        if icon1 == "fa fa-chevron-down":
            return not is_open1, False, False, up, down, down
        else:
            return not is_open1, False, False, down, down, down
    elif button_id == "accordion-group-2-toggle" and n2:
        if icon2 == "fa fa-chevron-down":
            return False, not is_open2, False, down, up, down
        else:
            return False, not is_open2, False, down, down, down
    elif button_id == "accordion-group-3-toggle" and n3:
        if icon3 == "fa fa-chevron-down":
            return False, False, not is_open3, down, down, up
        else:
            return False, False, not is_open3, down, down, down
    return False, False, False, down, down, down