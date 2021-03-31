import dash

from app import app
from dash.dependencies import Input, Output, State

   
with open("./texts/compliance/model-short.md") as f:
    compliance_short = f.read()
    
with open("./texts/compliance/model-long.md") as f:
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
        text = compliance_long
        button_text = "...less"
    else:
        text = compliance_short
        button_text = "...more"

    return  text, button_text