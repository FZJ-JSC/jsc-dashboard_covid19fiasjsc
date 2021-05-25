# For all elements that contain text which does not get set in callbacks: 
# Map id to English text

with open("./texts/compliance/de/model-short.md") as f:
    compliance_short = f.read()

with open("./texts/compliance/de/reduction-factor.md") as f:
    reduction_tooltip = f.read()
with open("./texts/compliance/de/compliance-level.md") as f:
    compliance_tooltip = f.read()
with open("./texts/compliance/de/plotted-data.md") as f:
    data_tooltip = f.read()
    
with open("./texts/compliance/de/plots-explanation.md") as f:
    compliance_plot_explanation = f.read()
    
    
compliance = {
    "page-title" : "Compliance Modell",
    "model-text": compliance_short,
    "toggle-btn": "...mehr",
    
    "faq-btn": "FAQ",
    "faq-close-btn": "Schließen",
    "general-faq-title": "Allgemeine FAQs",
    "compliance-faq-title": "Compliance Modell FAQs",
    
    "reduction-dropdown-label": "Schärfe der Maßnahmen",
    "reduction-dropdown-tooltip": reduction_tooltip,
    "reduction-dropdown": [
        {"label": "strikt", "value": "025"},
        {"label": "moderat", "value": "05"},
        {"label": "minimal", "value": "08"}
    ],
    "compliance-dropdown-label": "Compliance",
    "compliance-dropdown-tooltip": compliance_tooltip,
    "data-dropdown-label": "Plotted Data",
    "data-dropdown-tooltip": data_tooltip,
    "data-dropdown": [
        {"label": "Verstorbene", "value": "Dt"},
        {"label": "gemeldete Fälle", "value": "", "disabled": True},
        {"label": "gemeldete aktive Fälle", "value": "It"},
        {"label": "gemeldete kumulierte Fälle", "value": "cumCasT"},
        {"label": "gemeldete genesene Fälle", "value": "knownRt"},
        {"label": "Fälle gesamt (inkl. Undetektierter)", "value": "", "disabled": True},
        {"label": "aktive Fälle gesamt", "value": "actInfT"},
        {"label": "kumulierte Fälle gesamt", "value": "cumInfT"},
        {"label": "genesene Fälle gesamt", "value": "Rt"},
    ],
    
    "config-title": "Modellierungsszenario",
    "config-hint": "Bitte wählen Sie die Schärfe der einzuführenden Maßnahmen zur Kontaktbeschränkung und das Compliance-Level in der Bevölkerung aus.",
    "plot-config-title": "Plot Configuration",
    "plot-config-hint": "Please select simulation data to be visualized.",
    
    "plot-explanation": compliance_plot_explanation,
    
    "graph-tab": "Gewählte Ausgabe",
    "barcharts-tab": "Entsprechende tägliche Inzidenz",
    
    "graph-title": "Visualisiere gemeldete aktive Fälle (im Falle einer strikten Intervention)",
    "graph-tooltip": "Simulated data before and after introduction of control measures for selected intervention severity and compliance levels.",
    "graph-btn-1": "Ab dem Start der Intervention",
    "graph-btn-2": "Ab dem Start der Simulation"
}


other = {
    "about": "About",
    "about-path": "texts/about/de/about.md",
    "team": "Team",
    "team-path": "texts/about/de/team.md",
    "contrib": "Beiträge",
    "contrib-path": "texts/about/de/contributions.md",
    
    "impressum": "Impressum",
    "impressum-path": "texts/impressum/de/impressum.md",
    "disclaimer": "Haftungsausschluss",
    "disclaimer-path": "texts/impressum/de/haftungsausschluss.md",
    "hoster": "Hoster",
    "hoster-path": "texts/impressum/de/hoster.md",
    
    "privacy": "Datenschutz",
    "privacy-path": "texts/datenschutzerklaerung.md"
}


sidebar = {
    "compliance": "Compliance".upper(),
    "about": "About",
    "impressum": "Impressum",
    "privacy": "Datenschutz"
}