import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import re


def create_accordion_item(i, title, text, component_name, lang):
    return dbc.Card(
        [
            html.Div(
                dbc.Row(
                    [
                        dbc.Col(
                            title,
                            width=True
                        ),
                        dbc.Col(
                            html.I(
                                className="fa fa-chevron-down",
                                style={"alignSelf": "center"},
                                id=f"{component_name}-accordion-group-{i}-toggle-icon-{lang}"
                            ),
                            width="auto"
                        )
                    ],
                    no_gutters=True,
                    justify="between"
                ),
                id=f"{component_name}-accordion-group-{i}-toggle-{lang}",
                className="card-header",
                style={"backgroundColor": "transparent"}
            ),
            dbc.Collapse(
                dbc.CardBody(
                    dcc.Markdown(text),
                    className="bg-light",
                    style={"borderTop": "1px solid rgba(0, 0, 0, 0.125)"}
                ),
                id=f"{component_name}-accordion-collapse-{i}-{lang}",
            ),
        ]
    )


def create_faq(file, component_name, lang):
    with open(file) as f:
        faq_md = re.split("[\n]{3}", f.read())
    
    faq_items = []
    for i, question in enumerate(faq_md, start=1):
        q = question.split('\n')
        faq_items.append(create_accordion_item(i, q[0], q[1:], component_name, lang))

    return html.Div(
        faq_items,
        className="accordion"
    )