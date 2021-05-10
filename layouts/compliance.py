import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import en_EN

from app import compliance_percentages, initial_fig
from layouts.faq import compliance_faq, general_faq


###
# Model explanation
###
compliance_model_explanation = html.Div([
    dbc.Card(
        html.H3(
            en_EN.compliance["compliance-model-text-title"],
            className="mb-0 bold text-center",
            id="compliance-model-text-title"
        ),
        body=True,
        className="mb-4"
    ),
    dbc.Card(
        [
            dcc.Markdown(
                en_EN.compliance["compliance-model-text"],
                id="compliance-model-text"
            ),
            dbc.Row(
                children=[
                    dbc.Button(
                        en_EN.compliance["compliance-model-text-toggle"],
                        color="primary",
                        style={"min-width": "80px"},
                        id="compliance-model-text-toggle"),
                    ###
                    # FAQ
                    ###
                    dbc.Button(
                        en_EN.compliance["compliance-model-faq-toggle-open"],
                        color="warning",
                        style={"min-width": "80px"},
                        id="compliance-model-faq-toggle-open"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(
                                en_EN.compliance["general-faq-title"],
                                id="general-faq-title"
                            ),
                            dbc.ModalBody(general_faq),
                            dbc.ModalHeader(
                                en_EN.compliance["compliance-faq-title"],
                                id="compliance-faq-title"
                            ),
                            dbc.ModalBody(
                                compliance_faq
                            ),
                            dbc.ModalFooter(
                                dbc.Button(
                                    en_EN.compliance["compliance-model-faq-toggle-close"],
                                    id="compliance-model-faq-toggle-close",
                                    className="ml-auto"
                                )
                            ),
                        ],
                        id="compliance-model-faq-modal",
                        size="xl",
                        scrollable=True
                    ),
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
def create_formgroup(label, tooltip, widget, component_name):
    return dbc.FormGroup(
        [
            dbc.Col(
                [
                    html.Div(
                        label,
                        id="{}-label".format(component_name)
                    ),
                    html.I(
                        className="fa fa-question-circle ml-2",
                        id="{}-target".format(component_name),
                        style={
                            "color": "var(--dark)",
                            "alignSelf": "center"
                        },
                    ),
                    dbc.Tooltip(
                        tooltip, 
                        target="{}-target".format(component_name),
                        style={"height": "auto"}
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

   
reduction_dropdown = dcc.Dropdown(
    id="reduction-dropdown",
    clearable=False,
    options=en_EN.compliance["reduction-dropdown"],
    value="025"
)
reduction_formgroup = create_formgroup(
    en_EN.compliance["reduction-dropdown-label"], 
    en_EN.compliance["reduction-dropdown-target"], 
    reduction_dropdown, 
    "reduction-dropdown"
)

compliance_dropdown = dcc.Dropdown(
    id="compliance-dropdown",
    options=[
        {"label": "{}%".format(percentage), "value": percentage}
        for percentage in compliance_percentages[1:]
    ],
    value=[30, 50, 70, 100],
    multi=True
)
compliance_formgroup = create_formgroup(
    en_EN.compliance["compliance-dropdown-label"], 
    en_EN.compliance["compliance-dropdown-target"], 
    compliance_dropdown, 
    "compliance-dropdown"
)

data_dropdown = dcc.Dropdown(
    id="data-dropdown",
    clearable=False,
    searchable=False,
    options=en_EN.compliance["data-dropdown"],
    value="It",
    className="optgroup"
)
data_formgroup = create_formgroup(
    en_EN.compliance["data-dropdown-label"], 
    en_EN.compliance["data-dropdown-target"], 
    data_dropdown,
    "data-dropdown"
)


###
# Accordions for formgroups
###
def make_accordion_item(title, widgets, short_explanation, component_name):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div(
                    dbc.Row(
                        [
                            html.H5(
                                [
                                    html.I(className="fa fa-cog mr-2"),
                                    title
                                ],
                                id="{}-title".format(component_name),
                                className="mb-0"
                            ),
                            dbc.Col(
                                html.I(
                                    short_explanation,
                                    id="{}-explanation".format(component_name)
                                ),
                                className="col-lg-auto col-12 order-below",
                                style={"fontSize": "medium"}
                            ),
                            html.I(
                                className="fa fa-chevron-down",
                                style={"alignSelf": "center"},
                                id="accordion-group-{}-toggle-icon".format(component_name)
                            ),
                        ],
                        no_gutters=True,
                        justify="between"
                    ),
                    id="accordion-group-{}-toggle".format(component_name)
                ),
                style={
                    "backgroundColor": "transparent",
                    "borderBottom": "None"
                }
            ),
            dbc.Collapse(
                dbc.CardBody(widgets),
                id="accordion-collapse-{}".format(component_name)
            ),
        ],
    )


compliance_widgets = dbc.Row(
    [
        dbc.Col(
            make_accordion_item(en_EN.compliance["compliance-model-config-title"], 
                                [reduction_formgroup, compliance_formgroup],
                                en_EN.compliance["compliance-model-config-explanation"], 
                                "compliance-model-config"),
            className="mb-3",
            xs=12
        ),
        dbc.Col(
            make_accordion_item(en_EN.compliance["compliance-plot-config-title"], 
                                data_formgroup,
                                en_EN.compliance["compliance-plot-config-explanation"], 
                                "compliance-plot-config"),
            className="mb-3",
            xs=12
        ),
    ],
    className="mt-4"
)


###
# Plots
###

compliance_plots_explanation = dbc.Card(
    dbc.CardBody([
        dcc.Markdown(
            en_EN.compliance["compliance-plot-explanation"], 
            id="compliance-plot-explanation"
        ),
        compliance_widgets
    ]),
    className="mt-4",
    style={"borderBottom": "none"}
)


compliance_graph_content = dcc.Loading(
    html.Div(
        [
            dbc.Row(
                [
                    html.H5(
                        en_EN.compliance["compliance-graph-title"], 
                        id="compliance-graph-title", 
                        className="card-title bold"
                    ),
                    html.I(
                        className="card-title fa fa-question-circle fa-lg ml-2",
                        id="compliance-graph-target",
                        style={
                            "color": "var(--dark)",
                            "alignSelf": "center"
                        },
                    ),
                    dbc.Tooltip(
                        en_EN.compliance["compliance-graph-target"], 
                        target="compliance-graph-target",
                        style={"height": "auto"}
                    ),
                ],
                no_gutters=True
            ),
            dbc.Row(
                dbc.ButtonGroup(
                    [
                        dbc.Button(
                            en_EN.compliance["compliance-graph-btn-1"], 
                            id="compliance-graph-btn-1",
                            color="primary",
                            outline=True
                        ),
                        dbc.Button(
                            en_EN.compliance["compliance-graph-btn-2"],
                            id="compliance-graph-btn-2",
                            color="primary",
                            outline=True
                        )
                    ],
                    size="sm"
                ),
                no_gutters=True
            ),
            dcc.Graph(
                figure=initial_fig,
                config={"modeBarButtonsToRemove": ["autoScale2d"]},
                id="compliance-graph",
                className="w-1")
        ],
        className="mt-4",
        style={"minHeight": "600px"}
    )
)

compliance_barchart_content = dcc.Loading(
    html.Div(
        [
            html.H5(id="compliance-barcharts-title", className="mt-3 bold"),
            html.Div(
                id="compliance-barcharts",
                className="w-1",
                style={"minHeight": "600px"}
            ),
        ],
        className="mt-4"
    )
)


###
# Layout
###
compliance_content = [
    compliance_model_explanation,
    compliance_plots_explanation,
    dbc.Tabs(
        [
            dbc.Tab(
                label=en_EN.compliance["compliance-graph-tab"],
                tabClassName="bold",
                tab_id="compliance-graph-tab"
            ),
            dbc.Tab(
                label=en_EN.compliance["compliance-barcharts-tab"],
                tabClassName="bold",
                tab_id="compliance-barcharts-tab"
            ),
        ],
        id="compliance-tabs",
        card=True,
        className="mx-0"
    ),
    dbc.CardBody(
        id="compliance-content",
        style={
            "border": "1px solid #e7eaed", 
            "borderTop": "None"
        }
    ),
]