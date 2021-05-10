import dash_bootstrap_components as dbc
import dash_html_components as html
import re


def make_accordion_item(i, title, text, component_name):
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
                                id=f"{component_name}-accordion-group-{i}-toggle-icon"
                            ),
                            width="auto"
                        )
                    ],
                    no_gutters=True,
                    justify="between"
                ),
                id=f"{component_name}-accordion-group-{i}-toggle",
                className="card-header",
                style={"backgroundColor": "transparent"}
            ),
            dbc.Collapse(
                dbc.CardBody(
                    text,
                    className="bg-light",
                    style={"borderTop": "1px solid rgba(0, 0, 0, 0.125)"}
                ),
                id=f"{component_name}-accordion-collapse-{i}",
            ),
        ]
    )


###
# General FAQ
###
with open("texts/faq/en/general.md") as f:
    general_faq_md = re.split("[\n]{3}", f.read())
    
general_faq_items = []
for i, question in enumerate(general_faq_md, start=1):
    q = question.split('\n')
    general_faq_items.append(make_accordion_item(i, q[0], q[1:], "general-faq"))
    
general_faq = html.Div(
    general_faq_items,
    className="accordion"
)


###
# Compliance FAQ
###
with open("./texts/faq/en/compliance.md") as f:
    compliance_faq_md = re.split("[\n]{3}", f.read())
    
compliance_faq_items = []
for i, question in enumerate(compliance_faq_md, start=1):
    q = question.split('\n')
    compliance_faq_items.append(make_accordion_item(i, q[0], q[1:], "compliance-faq"))
    
compliance_faq = html.Div(
    compliance_faq_items,
    className="accordion"
)