# For all elements that contain text which does not get set in callbacks: 
# Map id to English text

with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

with open("./texts/compliance/en/reduction-factor.md") as f:
    reduction_tooltip = f.read()
with open("./texts/compliance/en/compliance-level.md") as f:
    compliance_tooltip = f.read()
with open("./texts/compliance/en/plotted-data.md") as f:
    data_tooltip = f.read()
    
with open("./texts/compliance/en/plots-explanation.md") as f:
    compliance_plot_explanation = f.read()
    
    
compliance = {
    "compliance-model-text-title" : "Compliance model",
    "compliance-model-text": compliance_short,
    "compliance-model-text-toggle": "...more",
    
    "compliance-model-faq-toggle-open": "FAQ",
    "compliance-model-faq-toggle-close": "Close",
    "general-faq-title": "General FAQs",
    "compliance-faq-title": "Compliance Model FAQs",
    
    "reduction-dropdown-label": "Intervention Severity",
    "reduction-dropdown-target": reduction_tooltip,
    "reduction-dropdown": [
        {"label": "strict", "value": "025"},
        {"label": "moderate", "value": "05"},
        {"label": "minimal", "value": "08"}
    ],
    "compliance-dropdown-label": "Compliance",
    "compliance-dropdown-target": compliance_tooltip,
    "data-dropdown-label": "Plotted Data",
    "data-dropdown-target": data_tooltip,
    "data-dropdown": [
        {"label": "deceased", "value": "Dt"},
        {"label": "reported cases", "value": "", "disabled": True},
        {"label": "active", "value": "It"},
        {"label": "cumulative", "value": "cumCasT"},
        {"label": "recovered", "value": "knownRt"},
        {"label": "total cases (incl. undetected)", "value": "", "disabled": True},
        {"label": "active", "value": "actInfT"},
        {"label": "cumulative", "value": "cumInfT"},
        {"label": "recovered", "value": "Rt"},
    ],
    
    "compliance-model-config-title": "Modelling Scenario",
    "compliance-model-config-explanation": "Please select the contact restriction severity to be introduced and the compliance level in the population.",
    "compliance-plot-config-title": "Plot Configuration",
    "compliance-plot-config-explanation": "Please select simulation data to be visualized.",
    
    "compliance-plot-explanation": compliance_plot_explanation,
    
    "compliance-graph-tab": "Selected output",
    "compliance-barcharts-tab": "Corresponding daily incidence",
    
    "compliance-graph-title": "Visualize known active cases (for contact reduction factor 0.25)",
    "compliance-graph-target": "Simulated data before and after introduction of control measures for selected intervention severity and compliance levels.",
    "compliance-graph-btn-1": "From start of intervention",
    "compliance-graph-btn-2": "From start of simulation",
}