import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import ClientsideFunction, Input, Output, State
from layouts.compliance import compliance_graph_content, compliance_barchart_content


# Callbacks for model explanation
with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

with open("./texts/compliance/en/model-long.md") as f:
    compliance_long = f.read()
    
@app.callback(
    Output("compliance-model-faq-modal", "is_open"),
    [Input("compliance-model-faq-toggle-open", "n_clicks"), 
     Input("compliance-model-faq-toggle-close", "n_clicks")],
    [State("compliance-model-faq-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    [Output("compliance-model-text", "children"),
     Output("compliance-model-text-toggle", "children")],
    Input("compliance-model-text-toggle", "n_clicks"),
    State("compliance-model-text-toggle", "children"),
    prevent_initial_call=True
)
def toggle_model_explanation(toggle_btn, btn_text):
    if btn_text == "...more":
        text = [
            dcc.Markdown(compliance_short),
            html.Hr(),
            html.Figure(
                [
                    html.Img(
                        src="assets/paper_screenshot_cropped_no_background.png",
                        width="350px", height="200px"
                    ),
                    html.Figcaption(
                        html.I("Sketch of the transmission dynamics model \
                        used for the simulations"),
                        style={
                            "fontSize": "85%",
                            "textAlign": "center"
                        }
                    )
                ],
                style={
                    "float": "right",
                    "width": "350px",
                    "margin": "1rem"
                }
            ),
            dcc.Markdown(compliance_long),
        ]
        button_text = "...less"
    else:
        text = dcc.Markdown(compliance_short)
        button_text = "...more"

    return text, button_text

    
# Callbacks for toggling form group accordions
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


# Callback for navigating between plots
@app.callback(
    Output("compliance-content", "children"),
    Input("compliance-tabs", "active_tab")
)
def switch_tab(at):
    if at == "compliance-graph-tab":
        return compliance_graph_content
    elif at == "compliance-barcharts-tab":
        return compliance_barchart_content


# Clientside callbacks for resizing plots
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