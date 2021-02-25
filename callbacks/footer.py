from app import app
from dash.dependencies import Input, Output, State


def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Footer
app.callback(
    Output('datenschutz_modal', 'is_open'),
    [Input('datenschutz_modal_open', 'n_clicks'), 
     Input('datenschutz_modal_close', 'n_clicks')],
    [State('datenschutz_modal', 'is_open')],
)(toggle_modal)

app.callback(
    Output('impressum_modal', 'is_open'),
    [Input('impressum_modal_open', 'n_clicks'), 
     Input('impressum_modal_close', 'n_clicks')],
    [State('impressum_modal', 'is_open')],
)(toggle_modal)