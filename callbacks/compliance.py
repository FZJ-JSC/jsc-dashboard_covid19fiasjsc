import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import ClientsideFunction, Input, Output, State
from apps.en.compliance import graph_content, barchart_content


# Callbacks for model explanation
with open("./texts/compliance/en/model-short.md") as f:
    compliance_short_en = f.read()

with open("./texts/compliance/en/model-long.md") as f:
    compliance_long_en = f.read()

LANG = "en"    

@app.callback(
    Output(f"compliance-model-faq-modal-{LANG}", "is_open"),
    Input(f"compliance-model-faq-toggle-open-{LANG}", "n_clicks"), 
    Input(f"compliance-model-faq-toggle-close-{LANG}", "n_clicks"),
    State(f"compliance-model-faq-modal-{LANG}", "is_open"),
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output(f"compliance-model-text-{LANG}", "children"),
    Output(f"compliance-model-text-toggle-{LANG}", "children"),
    Input(f"compliance-model-text-toggle-{LANG}", "n_clicks"),
    State(f"compliance-model-text-toggle-{LANG}", "children"),
    prevent_initial_call=True
)
def toggle_model_explanation(toggle_btn, btn_text):
    if btn_text == "...more":
        text = [
            dcc.Markdown(compliance_short_en),
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
            dcc.Markdown(compliance_long_en),
        ]
        button_text = "...less"
    else:
        text = dcc.Markdown(compliance_short_en)
        button_text = "...more"

    return text, button_text

    
# Callbacks for toggling form group accordions
def toggle_accordion(n1, is_open):
    if is_open:
        return False, "fa fa-chevron-down"
    else:
        return True, "fa fa-chevron-up"


for component in [f"compliance-model-config", f"compliance-plot-config"]:
    app.callback(
        Output(f"accordion-collapse-{component}-{LANG}", "is_open"),
        Output(f"accordion-group-{component}-toggle-icon-{LANG}", "className"),
        Input(f"accordion-group-{component}-toggle-{LANG}", "n_clicks"),
        State(f"accordion-collapse-{component}-{LANG}", "is_open"),
        prevent_initial_call=True,
    )(toggle_accordion)


# Callback for navigating between plots
@app.callback(
    Output(f"compliance-content-{LANG}", "children"),
    Input(f"compliance-tabs-{LANG}", "active_tab")
)
def switch_tab(at):
    if at == "compliance-graph-tab":
        return graph_content
    elif at == "compliance-barcharts-tab":
        return barchart_content


# Clientside callbacks for resizing plots
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("resize-dummy-1", "children"),
    Input(f"compliance-graph-{LANG}", "figure")
)

app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("resize-dummy-2", "children"),
    Input(f"compliance-barcharts-{LANG}", "children")
)