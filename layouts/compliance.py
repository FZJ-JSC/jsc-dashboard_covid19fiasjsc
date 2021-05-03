import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import compliance_percentages, initial_fig


###
# Model explanation
###
with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

compliance_model_explanation = html.Div([
    dbc.Card(
        html.H3(
            "Compliance model",
            className="mb-0 bold text-center",
            id="compliance-model-text-title"
        ),
        body=True,
        className="mb-4"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Div(
                        dcc.Markdown(compliance_short),
                        id="compliance-model-text"
                    ),
                    dbc.Row(
                        children=[
                            dbc.Button(
                                "...more",
                                color="primary",
                                style={"min-width": "80px"},
                                id="compliance-model-text-toggle"),
                            dbc.Button(
                                "FAQ",
                                color="warning",
                                style={"min-width": "80px"},
                                id="compliance-model-faq-toggle-open"),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Header"),
                                    dbc.ModalBody("This is the content of the modal"),
                                    dbc.ModalFooter(
                                        dbc.Button(
                                            "Close",
                                            id="compliance-model-faq-toggle-close",
                                            className="ml-auto"
                                        )
                                    ),
                                ],
                                id="compliance-model-faq-modal",
                            ),
                        ],
                        no_gutters=True,
                        justify="between"
                    )
                ],
            ),
        ],
        className="w-1"
    )
])


###
# Formgroups
###
def create_formgroup(label, tooltip, widget):
    component_name = label.replace(" ", "-").lower()
    return dbc.FormGroup(
        [
            dbc.Col(
                [
                    label,
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


with open("./texts/compliance/en/reduction-factor.md") as f:
    reduction_tooltip = f.read()
with open("./texts/compliance/en/compliance-level.md") as f:
    compliance_tooltip = f.read()
with open("./texts/compliance/en/plotted-data.md") as f:
    data_tooltip = f.read()
    
   
reduction_dropdown = dcc.Dropdown(
    id="reduction-dropdown",
    clearable=False,
    options=[
        {"label": "strict", "value": "025"},
        {"label": "moderate", "value": "05"},
        {"label": "minimal", "value": "08"},
    ],
    value="025"
)
reduction_formgroup = create_formgroup(
    "Reduction Factor", reduction_tooltip, reduction_dropdown)

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
    "Compliance", compliance_tooltip, compliance_dropdown)

data_dropdown = dcc.Dropdown(
    id="data-dropdown",
    clearable=False,
    searchable=False,
    options=[
        {"label": "deceased", "value": "Dt"},
        {"label": "known cases", "value": "", "disabled": True},
        {"label": "active", "value": "It"},
        {"label": "cumulative", "value": "cumCasT"},
        {"label": "recovered", "value": "knownRt"},
        {"label": "total cases", "value": "", "disabled": True},
        {"label": "active", "value": "actInfT"},
        {"label": "cumulative", "value": "cumInfT"},
        {"label": "recovered", "value": "Rt"},
    ],
    value="It",
    className="optgroup"
)
data_formgroup = create_formgroup(
    "Plotted Data", data_tooltip, data_dropdown)


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
                                className="mb-0"
                            ),
                            dbc.Col(
                                html.I(short_explanation),
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
            make_accordion_item("Modelling Scenario",
                                [reduction_formgroup, compliance_formgroup],
                                "Please select the contact restriction severity \
                                to be introduced and the compliance level in the population.",
                                "compliance-model"),
            className="mb-3",
            xs=12
        ),
        dbc.Col(
            make_accordion_item("Plot Configuration",
                                data_formgroup,
                                "Please select simulation data to be visualized.",
                                "compliance-plot"),
            className="mb-3",
            xs=12
        ),
    ],
    className="mt-4"
)


###
# Plots
###
with open("./texts/compliance/en/plots-explanation.md") as f:
    plots_explanation = f.read()

compliance_plots_explanation = dbc.Card(
    dbc.CardBody([
        dcc.Markdown(plots_explanation),
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
                        "Visualize known active cases (for contact reduction factor 0.25)", 
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
                        "Simulated data before and after introduction of control measures \
                        for selected restriction factor and compliance levels.",
                        target="compliance-graph-target",
                        style={"height": "auto"}
                    ),
                ],
                no_gutters=True
            ),
            dbc.Row(
                [
                    dbc.Button(
                        "From start of intervention",
                        id="compliance-graph-btn-1",
                        color="primary",
                        outline=True,
                        size="sm"
                    ),
                    dbc.Button(
                        "From start of simulation",
                        id="compliance-graph-btn-2",
                        className="ml-2",
                        color="primary",
                        outline=True,
                        size="sm"
                    )
                ],
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
                label="Selected output",
                tabClassName="bold",
                tab_id="compliance-graph-tab"
            ),
            dbc.Tab(
                label="Corresponding daily incidence",
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