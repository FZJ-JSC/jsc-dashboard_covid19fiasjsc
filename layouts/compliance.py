import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


###
# Model explanation
### 
def create_faq_modal(title1, faq1, title2, faq2, btn, lang):
    return dbc.Modal(
        [
            dbc.ModalHeader(
                title1,
                id=f"general-faq-title-{lang}"
            ),
            dbc.ModalBody(faq1),
            dbc.ModalHeader(
                title2,
                id=f"compliance-faq-title-{lang}"
            ),
            dbc.ModalBody(faq2),
            dbc.ModalFooter(
                dbc.Button(
                    btn,
                    id=f"compliance-model-faq-toggle-close-{lang}",
                    className="ml-auto"
                )
            ),
        ],
        id=f"compliance-model-faq-modal-{lang}",
        size="xl",
        scrollable=True
    )


def create_model_explanation(page_title, explanation_short, btn1, btn2, modal_widget, lang):
    return html.Div([
        dbc.Card(
            html.H3(
                page_title,
                className="mb-0 bold text-center",
                id=f"compliance-model-text-title-{lang}"
            ),
            body=True,
            className="mb-4"
        ),
        dbc.Card(
            [
                html.Div(
                    dcc.Markdown(explanation_short),
                    id=f"compliance-model-text-{lang}"
                ),
                dbc.Row(
                    children=[
                        dbc.Button(
                            btn1,
                            color="primary",
                            style={"minWidth": "80px"},
                            id=f"compliance-model-text-toggle-{lang}"),
                        ###
                        # FAQ
                        ###
                        dbc.Button(
                            btn2,
                            color="warning",
                            style={"minWidth": "80px"},
                            id=f"compliance-model-faq-toggle-open-{lang}"
                        ),
                        modal_widget
                    ],
                    no_gutters=True,
                    justify="between"
                )
            ],
            body=True,
            className="w-1"
        )
    ])


###
# Formgroups
###
def create_formgroup(label, tooltip, widget, component_name, lang):
    return dbc.FormGroup(
        [
            dbc.Col(
                [
                    html.Div(
                        label,
                        id=f"{component_name}-label-{lang}"
                    ),
                    html.I(
                        className="fa fa-question-circle ml-2",
                        id=f"{component_name}-target-{lang}",
                        style={
                            "color": "var(--dark)",
                            "alignSelf": "center"
                        },
                    ),
                    dbc.Tooltip(
                        tooltip,
                        target=f"{component_name}-target-{lang}",
                        placement="auto"
#                         style={"height": "auto"}
                    )
                ],
                style={"display": "flex", "alignItems": "center"},
                xs=12, lg=4),
            dbc.Col(
                widget,
                xs=12, lg=8
            )
        ],
        row=True
    )


###
# Accordions for formgroups
###
def create_config_accordion_item(title, hint, widgets, component_name, lang):
    return dbc.Card(
        [
            html.Div(
                dbc.Row(
                    [
                        html.H5(
                            [
                                html.I(className="fa fa-cog mr-2"),
                                title
                            ],
                            className="mb-0"
                        ),
                        dbc.Col(
                            html.I(hint),
                            className="col-lg-auto col-12 order-below",
                            style={"fontSize": "medium"}
                        ),
                        html.I(
                            className="fa fa-chevron-down",
                            style={"alignSelf": "center"},
                            id=f"accordion-group-{component_name}-toggle-icon-{lang}"
                        ),
                    ],
                    no_gutters=True,
                    justify="between"
                ),
                id=f"accordion-group-{component_name}-toggle-{lang}",
                className="card-header",
                style={
                    "backgroundColor": "transparent",
                    "borderBottom": "None"
                }
            ),
            dbc.Collapse(
                dbc.CardBody(widgets),
                id=f"accordion-collapse-{component_name}-{lang}"
            ),
        ],
    )


def create_compliance_widgets(accordion1, accordion2):
    return dbc.Row(
        [
            dbc.Col(
                accordion1,
                className="mb-3",
                xs=12
            ),
            dbc.Col(
                accordion2,
                className="mb-3",
                xs=12
            ),
        ],
        className="mt-4"
    )


###
# Plots
###
def create_compliance_plots_explanation(img1, img2, explanation, compliance_widgets, lang):
    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Img(src=img1, height="auto", width="auto")),
                dbc.Col(html.Img(src=img2, height="auto", width="auto"))
            ]),
            dcc.Markdown(
                explanation, 
                id=f"compliance-plot-explanation-{lang}"
            ),
            compliance_widgets
        ]),
        className="mt-4",
        style={"borderBottom": "none"}
    )


def create_compliance_graph_content(title, tooltip, btn1, btn2, fig, lang):
    return dcc.Loading(
        html.Div(
            [
                dbc.Row(
                    [
                        html.H5(
                            title, 
                            id=f"compliance-graph-title-{lang}", 
                            className="card-title bold"
                        ),
                        html.I(
                            className="card-title fa fa-question-circle fa-lg ml-2",
                            id=f"compliance-graph-target-{lang}",
                            style={
                                "color": "var(--dark)",
                                "alignSelf": "center"
                            },
                        ),
                        dbc.Tooltip(
                            tooltip, 
                            target=f"compliance-graph-target-{lang}",
                            placement="auto"
#                             style={"height": "auto"}
                        ),
                    ],
                    no_gutters=True
                ),
                dbc.Row(
                    dbc.ButtonGroup(
                        [
                            dbc.Button(
                                btn1, 
                                id=f"compliance-graph-btn-1-{lang}",
                                color="primary",
                                outline=True
                            ),
                            dbc.Button(
                                btn2,
                                id=f"compliance-graph-btn-2-{lang}",
                                color="primary",
                                outline=True
                            )
                        ],
                        size="sm"
                    ),
                    no_gutters=True
                ),
                dcc.Graph(
                    figure=fig,
                    config={"modeBarButtonsToRemove": ["autoScale2d"]},
                    id=f"compliance-graph-{lang}",
                    className="w-1")
            ],
            className="mt-4",
            style={"minHeight": "600px"}
        )
    )


def _create_compliance_barchart_incidence_buttons(btn1, btn2, lang):
    return dbc.Row(
        dbc.ButtonGroup(
            [
                dbc.Button(
                    btn1,
                    id=f"compliance-barchart-btn-1-{lang}",
                    color="primary",
                    outline=True,
                    style={"minWidth": "175px"}
                ),
                dbc.Button(
                    btn2,
                    id=f"compliance-barchart-btn-2-{lang}",
                    color="primary",
                    outline=True,
                    style={"minWidth": "175px"}
                )
            ],
            size="sm"
        ),
        id=f"compliance-barchart-btns-{lang}",
        no_gutters=True
    )


def create_compliance_barchart_content(btn1, btn2, lang):
    buttons = _create_compliance_barchart_incidence_buttons(btn1, btn2, lang)
    
    return dcc.Loading(
        html.Div(
            [
                html.H5(id=f"compliance-barcharts-title-{lang}", className="mt-3 bold"),
                buttons,
                dcc.Graph(
                    id=f"compliance-barcharts-{lang}",
                    config={"modeBarButtonsToRemove": [  # pan2d
                        "zoom2d", "select2d", "lasso2d", "autoScale2d", 
                        "hoverClosestCartesian", "hoverCompareCartesian"
                    ]},
                    className="w-1",
                    style={"minHeight": "600px"}
                )  
#                 html.Div(
#                     id=f"compliance-barcharts-{lang}",
#                     className="w-1",
#                     style={"minHeight": "600px"}
#                 ),
            ],
            className="mt-4"
        )
    )


###
# Layout
###
def create_compliance_page(model_explanation_layout, plot_explanation_layout, label1, label2, lang):
    return html.Div([
        model_explanation_layout,
        plot_explanation_layout,
        dbc.Tabs(
            [
                dbc.Tab(
                    label=label1,
                    tabClassName="bold",
                    tab_id="compliance-graph-tab"
                ),
                dbc.Tab(
                    label=label2,
                    tabClassName="bold",
                    tab_id="compliance-barcharts-tab"
                ),
            ],
            id=f"compliance-tabs-{lang}",
            card=True,
            className="mx-0"
        ),
        dbc.CardBody(
            id=f"compliance-content-{lang}",
            style={
                "border": "1px solid #e7eaed", 
                "borderTop": "None"
            }
        ),
    ])