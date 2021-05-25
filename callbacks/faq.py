import dash

from app import app
from dash.dependencies import Input, Output, State


def toggle_accordion(n, is_open):
    down = "fa fa-chevron-down"
    up = "fa fa-chevron-up"
    
    if not is_open:
        return True, up
    else:
        return False, down
    

for LANG in ["de", "en"]:    
    for i in range(1, 8):
        app.callback(
            Output(f"general-faq-accordion-collapse-{i}-{LANG}", "is_open"),
            Output(f"general-faq-accordion-group-{i}-toggle-icon-{LANG}", "className"),
            Input(f"general-faq-accordion-group-{i}-toggle-{LANG}", "n_clicks"),
            State(f"general-faq-accordion-collapse-{i}-{LANG}", "is_open"),
            prevent_initial_call=True
        )(toggle_accordion)

    for i in range(1, 7):
        app.callback(
            Output(f"compliance-faq-accordion-collapse-{i}-{LANG}", "is_open"),
            Output(f"compliance-faq-accordion-group-{i}-toggle-icon-{LANG}", "className"),
            Input(f"compliance-faq-accordion-group-{i}-toggle-{LANG}", "n_clicks"),
            State(f"compliance-faq-accordion-collapse-{i}-{LANG}", "is_open"),
            prevent_initial_call=True
        )(toggle_accordion)
    

# @app.callback(
#     [Output("general-faq-accordion-collapse-{}", "is_open") for i in range(1, 8)] +
#     [Output("general-faq-accordion-group-{}-toggle-icon", "className") for i in range(1, 8)],
#     [Input("general-faq-accordion-group-{}-toggle", "n_clicks") for i in range(1, 8)],
#     [State("general-faq-accordion-collapse-{}", "is_open") for i in range(1, 8)]
# )
# def toggle_general_faq_accordion(n1, n2, n3, n4, n5, n6, n7, 
#                                  is_open1, is_open2, is_open3, is_open4, is_open5, is_open6, is_open7):
#     ctx = dash.callback_context

#     down = "fa fa-chevron-down"
#     up = "fa fa-chevron-up"
#     all_closed = (False,) * 7 + (down,) * 7

#     if not ctx.triggered:
#         return all_closed
#     else:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
#     if "1" in button_id and n1:
#         if not is_open1:
#             return (False,) * 0 + (True,) + (False,) * 6 + (down,) * 0 + (up,) + (down,) * 6
#         else:
#             return all_closed
#     elif "2" in button_id and n2:
#         if not is_open2:
#             return (False,) * 1 + (True,) + (False,) * 5 + (down,) * 1 + (up,) + (down,) * 5
#         else:
#             return all_closed
#     elif "3" in button_id and n3:
#         if not is_open3:
#             return (False,) * 2 + (True,) + (False,) * 4 + (down,) * 2 + (up,) + (down,) * 4
#         else:
#             return all_closed
#     elif "4" in button_id and n4:
#         if not is_open4:
#             return (False,) * 3 + (True,) + (False,) * 3 + (down,) * 3 + (up,) + (down,) * 3
#         else:
#             return all_closed
#     elif "5" in button_id and n5:
#         if not is_open5:
#             return (False,) * 4 + (True,) + (False,) * 2 + (down,) * 4 + (up,) + (down,) * 2
#         else:
#             return all_closed
#     elif "6" in button_id and n6:
#         if not is_open6:
#             return (False,) * 5 + (True,) + (False,) * 1 + (down,) * 5 + (up,) + (down,) * 1
#         else:
#             return all_closed
#     elif "7" in button_id and n7:
#         if not is_open7:
#             return (False,) * 6 + (True,) + (False,) * 0 + (down,) * 6 + (up,) + (down,) * 0
#         else:
#             return all_closed
#     return all_closed