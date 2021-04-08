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
            html.Img(
                src="assets/paper_screenshot_cropped_no_background.png",
                style={"float": "right"}
            ),
            dcc.Markdown(compliance_long),
            html.A(
                "https://www.preprints.org/manuscript/202102.0178/v2",
                href="https://www.preprints.org/manuscript/202102.0178/v2",
                target="_blank",
                style={
                    "position": "relative",
                    "top": "-1rem"
                }
            )
        ]
        button_text = "...less"
    else:
        text = dcc.Markdown(compliance_short)
        button_text = "...more"

    return text, button_text