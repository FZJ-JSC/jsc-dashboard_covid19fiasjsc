import dash
import dash_core_components as dcc

from app import app
from dash.dependencies import Input, Output


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()
    
info_buttons = ["model-info-button", "publications-button", "press-button"]


# Toggle active modell in navigation
@app.callback(
    [Output(btn, "active") for btn in info_buttons],
    [Input(btn, "n_clicks") for btn in info_buttons]
)
def set_active(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True, False, False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == info_buttons[0]:
        return True, False, False
    elif button_id == info_buttons[1]:
        return False, True, False
    else:
        return False, False, True
    
    
# Update content in page depending on the model
@app.callback(
    Output("info-content", "children"),
    [Input(btn, "n_clicks") for btn in info_buttons],
    prevent_initial_call=True
) 
def update_model_content(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return compliance_content
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == info_buttons[0]:
        return dcc.Markdown(lorem_ipsum[:600])
    elif button_id == info_buttons[1]:
        return dcc.Markdown(lorem_ipsum[:398])
    elif button_id == info_buttons[2]:
        return dcc.Markdown(lorem_ipsum[398:])