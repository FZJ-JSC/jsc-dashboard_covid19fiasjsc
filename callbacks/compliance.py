from app import app
from dash.dependencies import ClientsideFunction, Input, Output, State
from layouts.compliance import compliance_graph_content, compliance_barchart_content


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


@app.callback(
    Output("compliance-content", "children"),
    Input("compliance-tabs", "active_tab")
)
def switch_tab(at):
    if at == "compliance-graph-tab":
        return compliance_graph_content
    elif at == "compliance-barcharts-tab":
        return compliance_barchart_content


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("resize-dummy-1", "children"),
    Input("compliance-graph", "figure")
)


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("resize-dummy-2", "children"),
    Input("compliance-barcharts", "children")
)