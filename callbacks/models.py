import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output, State


with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

with open("./texts/compliance/en/model-long.md") as f:
    compliance_long = f.read()


# Update explanation title and text depending on the model
@app.callback(
    [Output("model-text", "children"),
     Output("model-text-toggle", "children")],
    Input("model-text-toggle", "n_clicks"),
    State("model-text-toggle", "children"),
    prevent_initial_call=True
)
def update_model_text(toggle_btn, btn_text):
    ctx = dash.callback_context
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