import dash

from app import app
from dash.dependencies import Input, Output, State
from de_DE import sidebar as sidebar_de
from en_EN import sidebar as sidebar_en


# Toggle navigation menu
@app.callback(
    Output("sidebar-collapse", "is_open"),
    Input("sidebar-toggle", "n_clicks"),
    State("sidebar-collapse", "is_open"),
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


nav_items = ["model-nav"]
extra_nav_items = ["about-nav", "impressum-nav", "privacy-nav"]

# Toggle active nav item in sidebar,
# depending on the current url
@app.callback(
    [Output(item, "active") for item in nav_items + extra_nav_items],
    Input('url', 'pathname')
)
def set_active(pathname):
    if pathname.endswith("/_update"):
        return (False,) * 4
    
    elif pathname.endswith("/about"):
        return (False,) * 1 + (True,) + (False,) * 2
    elif pathname.endswith("/impressum"):
        return (False,) * 2 + (True,) + (False,) * 1
    elif pathname.endswith("/privacy"):
        return (False,) * 3 + (True,) + (False,) * 0
    else:
        return (False,) * 0 + (True,) + (False,) * 3
    

# Change language and href in sidebar, depending on chosen language
@app.callback(
    [Output(item, "children") for item in nav_items + extra_nav_items],
    [Output(item, "href") for item in nav_items + extra_nav_items],
    Input("lang-de", "n_clicks"),
    Input("lang-en", "n_clicks")
)
def toggle_language(n1, n2):
    ctx = dash.callback_context
    
    de = [val for val in sidebar_de.values()]
    en = [val for val in sidebar_en.values()]
    
    href_de = ["/de/compliance", "/de/about", "/de/impressum", "/de/privacy"]
    href_en = ["/", "/about", "/impressum", "/privacy"]

    if not ctx.triggered:
        # Default English
        return en + href_en
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                
        if "en" in button_id:
            return en + href_en
        elif "de" in button_id:
            return de + href_de