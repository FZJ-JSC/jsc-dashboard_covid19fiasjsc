import dash

from app import app
from dash.dependencies import Input, Output, State


@app.callback(
    [Output("accordion-collapse-{}".format(i), "is_open") for i in range(1, 4)] +
    [Output("accordion-group-{}-toggle-icon".format(i), "className") for i in range(1, 4)],
    [Input("accordion-group-{}-toggle".format(i), "n_clicks") for i in range(1, 4)],
    [State("accordion-collapse-{}".format(i), "is_open") for i in range(1, 4)]
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    down = "fa fa-chevron-down"
    up = "fa fa-chevron-up"
    all_closed = (False,) * 3 + (down,) * 3

    if not ctx.triggered:
        return all_closed
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "accordion-group-1-toggle" and n1:
        if not is_open1:
            return True, False, False, up, down, down
        else:
            return all_closed
    elif button_id == "accordion-group-2-toggle" and n2:
        if not is_open2:
            return False, True, False, down, up, down
        else:
            return all_closed
    elif button_id == "accordion-group-3-toggle" and n3:
        if not is_open3:
            return False, False, True, down, down, up
        else:
            return all_closed
    return all_closed