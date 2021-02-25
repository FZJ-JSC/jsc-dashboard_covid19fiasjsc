import dash

from app import app
from dash.dependencies import Input, Output, State


with open("./texts/lorem_ipsum.txt") as f:
    lorem_ipsum = f.read()

modell_buttons = ["compliance-button", "impfung-button", "hospitalisierung-button"]


# Toggle active modell in navigation
@app.callback(
    [Output(modell_buttons[0], "active"),
     Output(modell_buttons[1], "active"),
     Output(modell_buttons[2], "active")],
    [Input(modell_buttons[0], "n_clicks"),
     Input(modell_buttons[1], "n_clicks"),
     Input(modell_buttons[2], "n_clicks")]
)
def set_active(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True, False, False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == modell_buttons[0]:
        return True, False, False
    elif button_id == modell_buttons[1]:
        return False, True, False
    else:
        return False, False, True


# Update explanation title and text depending on the model
@app.callback(
    [Output("model-text-title", "children"),
     Output("model-text", "children"),
     Output("model-text-toggle", "children")],
    [Input(modell_buttons[0], "n_clicks"),
     Input(modell_buttons[1], "n_clicks"),
     Input(modell_buttons[2], "n_clicks"),
     Input("model-text-toggle", "n_clicks")],
    [State(modell_buttons[0], "active"),
     State(modell_buttons[1], "active"),
     State(modell_buttons[2], "active"),
     State("model-text-toggle", "children")],
    prevent_initial_call=True
)
def update_model_text(btn1, btn2, btn3, toggle_btn, active1, active2, active3, btn_text):
    ctx = dash.callback_context
    title = "What is the "

    if not ctx.triggered:
        return title + "compliance model?"
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == modell_buttons[0]:
        title = title + "compliance model?"
        text = lorem_ipsum[:199]
        button_text = "...more"
    elif button_id == modell_buttons[1]:
        title = title + "vaccination model?"
        text = lorem_ipsum[:199]
        button_text = "...more"
    elif button_id == modell_buttons[2]:
        title = title + "hospitalisation model?"
        text = lorem_ipsum[:199]
        button_text = "...more"

    else:  # The more button was clicked
        if btn_text == "...more":
            if active1:
                title = title + "compliance model?"
                text = lorem_ipsum
            elif active2:
                title = title + "vaccination model?"
                text = lorem_ipsum
            elif active3:
                title = title + "hospitalisation model?"
                text = lorem_ipsum
            button_text = "...less"
        else:
            if active1:
                title = title + "compliance model?"
                text = lorem_ipsum[:199]
            elif active2:
                title = title + "vaccination model?"
                text = lorem_ipsum[:199]
            elif active3:
                title = title + "hospitalisation model?"
                text = lorem_ipsum[:199]
            button_text = "...more"

    return title, text, button_text