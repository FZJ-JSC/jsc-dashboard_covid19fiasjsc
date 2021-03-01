from app import app
from dash.dependencies import Input, Output, State


def toggle_accordion(n1, is_open):
    if is_open:
        return False, "fa fa-chevron-down"
    else:
        return True, "fa fa-chevron-up"
    

for component in ["compliance-model", "compliance-plot"]:
    app.callback(
        [Output("accordion-collapse-{}".format(component), "is_open"),
         Output("accordion-group-{}-toggle-icon".format(component), "className")],
        Input("accordion-group-{}-toggle".format(component), "n_clicks"),
        State("accordion-collapse-{}".format(component), "is_open"),
        prevent_initial_call=True
    )(toggle_accordion)