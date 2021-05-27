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
    compliance_config_explanation = f.read()
with open("./texts/compliance/de/line-plot.md") as f:
    line_plot_explanation = f.read()
with open("./texts/compliance/de/bar-charts.md") as f:
    bar_charts_explanation = f.read()


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
    "data-dropdown-label": "Angezeigte Werte",
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
    "config-hint": "Bitte wählen Sie die Schärfe der einzuführenden Maßnahmen zur Kontaktbeschränkung und die Compliance-Rate in der Bevölkerung aus.",
    "plot-config-title": "Anzeigeoptionen",
    "plot-config-hint": "Bitte wählen Sie den angezeigten Ausgabewert.",

    "plots-explanation": "Klicken Sie auf die Bilder für Interpretationshilfe:",
    "line-plot-explanation-title": "Liniendiagramm: Verlauf der Epidemie",
    "line-plot-explanation": line_plot_explanation,
    "bar-charts-explanation-title": "Balkendiagramme: tägliche Änderungen",
    "bar-charts-explanation": bar_charts_explanation,
    "config-explanation": compliance_config_explanation,

    "graph-tab": "Gewählte Ausgabe",
    "barcharts-tab": "Entsprechende tägliche Inzidenz",

    "graph-title": "Visualisiere gemeldete aktive Fälle (im Falle einer strikten Intervention)",
    "graph-tooltip": "Simulierte Daten vor und nach Einfuehrung der Maßnahmen für die ausgewählte Schärfe der Maßnahmen und die gewählten Compliance-Raten.",
    "graph-btn-1": "Ab dem Start der Intervention",
    "graph-btn-2": "Ab dem Start der Simulation",
    
    "barcharts-btn-1": "Tägliche Inzidenz",
    "barcharts-btn-2": "7-Tages-Inzidenz"
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