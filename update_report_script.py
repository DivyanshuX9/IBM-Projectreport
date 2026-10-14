import re

with open('compile_final_report.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect figure replacements
replacements = {
    # Fig 3.1
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image6.jpg", "Fig 3.1: Entity Relationship Diagram for Normalized Heart Disease Database Schema", height=Inches(2.4))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_1_erd_heart.png", "Fig 3.1: Entity Relationship Diagram for Normalized Heart Disease Database Schema", width=Inches(6.0))',

    # Fig 3.2
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image10.jpg", "Fig 3.2: Univariate Distributions of Key Clinical Numerical and Categorical Attributes", height=Inches(2.3))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_2_eda_dashboard.png", "Fig 3.2: Univariate and Bivariate Clinical Distributions Dashboard", width=Inches(5.6))',

    # Fig 3.3
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image15.png", "Fig 3.3: Bivariate Clinical Feature Correlation Dashboard and Target Associations", height=Inches(2.4))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_3_bivariate_scatter.png", "Fig 3.3: Bivariate Clinical Feature Scatter Distributions and Associations", width=Inches(6.0))',

    # Fig 3.4
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image18.png", "Fig 3.4: Random Forest Feature Importance Assessment across 13 Clinical Attributes", height=Inches(2.1))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_4_rf_importance.png", "Fig 3.4: Random Forest Feature Importance Assessment across 13 Clinical Attributes", width=Inches(5.2))',

    # Fig 3.5
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image19.png", "Fig 3.5: SHAP Beeswarm Summary Plot for Global Feature Impact on Predictions", height=Inches(2.1))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_5_shap_beeswarm.png", "Fig 3.5: SHAP Beeswarm Summary Plot for Global Feature Impact on Predictions", width=Inches(4.8))',

    # Fig 3.6
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image20.png", "Fig 3.6: SHAP Force Plot for Local Single Patient Decision Explanation", width=Inches(5.6))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_6_shap_force.png", "Fig 3.6: SHAP Force Plot for Local Single Patient Decision Explanation", width=Inches(6.0))',

    # Fig 3.7
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image25.jpg", "Fig 3.7: Visily UI Wireframes for College Library Management System Screens", height=Inches(2.2))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_7_visily_wireframes.png", "Fig 3.7: Visily UI Wireframes for College Library Management System Screens", width=Inches(6.0))',

    # Fig 3.8
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image28.jpg", "Fig 3.8: Multi-Tier System Architecture Diagram Generated with Eraser.io", height=Inches(2.2))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_8_eraser_architecture.png", "Fig 3.8: Multi-Tier System Architecture Diagram Generated with Eraser.io", width=Inches(6.0))',

    # Fig 3.9
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image29.jpg", "Fig 3.9: Eraser.io Entity Relationship Diagram for Library Relational Database", height=Inches(2.3))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_9_eraser_erd.png", "Fig 3.9: Eraser.io Entity Relationship Diagram for Library Relational Database", width=Inches(5.5))',

    # Fig 3.10
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image37.jpg", "Fig 3.10: Interactive HTML Frontend Interface Rendered inside Google Colab", height=Inches(2.3))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_10_html_frontend.png", "Fig 3.10: Interactive HTML Frontend Interface Rendered inside Google Colab", width=Inches(6.0))',

    # Fig 3.11
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image42.jpg", "Fig 3.11: Automated Test Suite Execution Output Showing 100% Pass Rate", height=Inches(2.0))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_11_test_suite_output.png", "Fig 3.11: Automated Test Suite Execution Output Showing 100% Pass Rate", width=Inches(5.0))',

    # Fig 3.12
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image46.jpg", "Fig 3.12: API Latency Telemetry Simulation with Real-time Surge and AI Mitigation", height=Inches(2.3))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_12_telemetry_simulation.png", "Fig 3.12: API Latency Telemetry Simulation with Real-time Surge and AI Mitigation", width=Inches(4.8))',

    # Fig 3.13
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\image50.jpg", "Fig 3.13: Predictive Maintenance Telemetry Forecast and Resource Saturation Curves", height=Inches(2.3))':
    r'add_fig(r"c:\Users\symdr\Downloads\adddr\processed_figures\final_clean\fig3_13_predictive_maintenance.png", "Fig 3.13: Predictive Maintenance Telemetry Forecast and Resource Saturation Curves", width=Inches(5.4))',
}

# Update LOF captions if needed
lof_old = '["Fig 3.2", "Univariate Distributions of Key Clinical Numerical and Categorical Attributes", "12"],'
lof_new = '["Fig 3.2", "Univariate and Bivariate Clinical Distributions Dashboard", "12"],'
content = content.replace(lof_old, lof_new)

lof_old2 = '["Fig 3.3", "Bivariate Clinical Feature Correlation Dashboard and Target Associations", "12"],'
lof_new2 = '["Fig 3.3", "Bivariate Clinical Feature Scatter Distributions and Associations", "12"],'
content = content.replace(lof_old2, lof_new2)

for old_str, new_str in replacements.items():
    if old_str in content:
        content = content.replace(old_str, new_str)
        print("Replaced:", old_str[:40], "...")
    else:
        print("NOT FOUND:", old_str[:40], "...")

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved compile_perfect_report.py")

