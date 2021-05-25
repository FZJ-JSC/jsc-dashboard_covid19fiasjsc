import dash

from app import app
from dash.dependencies import Input, Output, State


@app.callback(
    Output("lang-de", "active"),
    Output("lang-en", "active"),
    Input("lang-de", "n_clicks"),
    Input("lang-en", "n_clicks"),
)
def toggle_language(n1, n2):
    ctx = dash.callback_context

    if not ctx.triggered:
        # Default English
        return False, True
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if "en" in button_id:
            return False, True
        elif "de" in button_id:
            return True, False
        
@app.callback(       
    Output("url", "pathname"),
    Input("lang-de", "n_clicks"),
    Input("lang-en", "n_clicks"),
    State("url", "pathname")
)
def update_url(n1, n2, pathname):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return pathname
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if "en" in button_id:
            if "/de/" in pathname:
                pathname = pathname[3:]
            return pathname
        elif "de" in button_id:
            if "/de/" not in pathname:
                pathname = "/de" + pathname
            return pathname
    