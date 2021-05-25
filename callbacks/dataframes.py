from app import app, update_dataframes
from dash.dependencies import Input, Output


LANG = "de"

@app.callback(
    Output(f"dataframes-{LANG}", "data"),
    Input(f"reduction-dropdown-{LANG}", "value")
)
def update_dfs_de(r):
    return update_dataframes(r, "Tag")


LANG = "en"

@app.callback(
    Output(f"dataframes-{LANG}", "data"),
    Input(f"reduction-dropdown-{LANG}", "value")
)
def update_dfs_de(r):
    return update_dataframes(r, "Day")