from app import app, update_dataframes
from dash.dependencies import Input, Output


app.callback(
    Output("dataframes", "data"),
    Input("reduction-dropdown", "value")
)(update_dataframes)