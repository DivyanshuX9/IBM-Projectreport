with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Update TOC
old_toc = '''    toc_rows = [
        ["1", "INTRODUCTION", "01"],
        ["2", "THEORETICAL FOUNDATIONS AND COURSE WORK", "04"],
        ["3", "TECHNICAL IMPLEMENTATION AND MINI PROJECTS", "09"],
        ["", "      3.1 Practical Coursework Exercises and Assignment 1", "09"],
        ["", "      3.2 Mini Project 1: Data Science with Generative AI", "10"],
        ["", "      3.3 Mini Project 2: Software Development Using Generative AI", "16"],
        ["4", "CONCLUSION AND FUTURE SCOPE", "23"],
        ["", "REFERENCES", "25"],
        ["", "APPENDIX I", "26"]
    ]'''

new_toc = '''    toc_rows = [
        ["1", "INTRODUCTION", "01"],
        ["2", "THEORETICAL FOUNDATIONS AND COURSE WORK", "04"],
        ["3", "TECHNICAL IMPLEMENTATION AND MINI PROJECTS", "09"],
        ["", "      3.1 Practical Coursework Exercises and Assignment 1", "09"],
        ["", "      3.2 Mini Project 1: Data Science with Generative AI", "09"],
        ["", "      3.3 Mini Project 2: Software Development Using Generative AI", "17"],
        ["4", "CONCLUSION AND FUTURE SCOPE", "26"],
        ["", "REFERENCES", "28"],
        ["", "APPENDIX I", "29"]
    ]'''

text = text.replace(old_toc, new_toc)

# Update LOT
old_lot = '''    lot_rows = [
        ["Table 3.1", "Heart Disease Normalized SQLite Database Schema (3NF Structure)", "10"],
        ["Table 3.2", "Summary of Clinical Hypotheses, Statistical Findings, and Decisions", "12"],
        ["Table 3.3", "Performance Evaluation and Comparison of Machine Learning Models", "13"],
        ["Table 3.4", "Hyperparameter Tuning and Overfitting Mitigation Comparison", "15"],
        ["Table 3.5", "College Library Management System Requirements Specification Table", "16"],
        ["Table 3.6", "Non-Functional Requirements (NFRs) for Library Application", "16"],
        ["Table 3.7", "Automated Test Suite Execution Summary across Four Testing Modules", "19"],
        ["Table 3.8", "Server Performance Telemetry and Critical Threshold Predictions", "21"]
    ]'''

new_lot = '''    lot_rows = [
        ["Table 3.1", "Heart Disease Normalized SQLite Database Schema (3NF Structure)", "10"],
        ["Table 3.2", "Summary of Clinical Hypotheses, Statistical Findings, and Decisions", "13"],
        ["Table 3.3", "Performance Evaluation and Comparison of Machine Learning Models", "14"],
        ["Table 3.4", "Hyperparameter Tuning and Overfitting Mitigation Comparison", "17"],
        ["Table 3.5", "College Library Management System Requirements Specification Table", "17"],
        ["Table 3.6", "Non-Functional Requirements (NFRs) for Library Application", "18"],
        ["Table 3.7", "Automated Test Suite Execution Summary across Four Testing Modules", "21"],
        ["Table 3.8", "Server Performance Telemetry and Critical Threshold Predictions", "23"]
    ]'''

text = text.replace(old_lot, new_lot)

# Update LOF
old_lof = '''    lof_rows = [
        ["Fig 3.1", "Entity Relationship Diagram for Normalized Heart Disease Database Schema", "11"],
        ["Fig 3.2", "Univariate and Bivariate Clinical Distributions Dashboard", "12"],
        ["Fig 3.3", "Bivariate Clinical Feature Scatter Distributions and Associations", "12"],
        ["Fig 3.4", "Random Forest Feature Importance Assessment across 13 Clinical Attributes", "14"],
        ["Fig 3.5", "SHAP Beeswarm Summary Plot for Global Feature Impact on Predictions", "14"],
        ["Fig 3.6", "SHAP Force Plot for Local Single Patient Decision Explanation", "15"],
        ["Fig 3.7", "Visily UI Wireframes for College Library Management System Screens", "17"],
        ["Fig 3.8", "Multi-Tier System Architecture Diagram Generated with Eraser.io", "18"],
        ["Fig 3.9", "Eraser.io Entity Relationship Diagram for Library Relational Database", "18"],
        ["Fig 3.10", "Interactive HTML Frontend Interface Rendered inside Google Colab", "19"],
        ["Fig 3.11", "Automated Test Suite Execution Output Showing 100% Pass Rate", "20"],
        ["Fig 3.12", "API Latency Telemetry Simulation with Real-time Surge and AI Mitigation", "21"],
        ["Fig 3.13", "Predictive Maintenance Telemetry Forecast and Resource Saturation Curves", "21"]
    ]'''

new_lof = '''    lof_rows = [
        ["Fig 3.1", "Entity Relationship Diagram for Normalized Heart Disease Database Schema", "11"],
        ["Fig 3.2", "Univariate and Bivariate Clinical Distributions Dashboard", "12"],
        ["Fig 3.3", "Bivariate Clinical Feature Scatter Distributions and Associations", "13"],
        ["Fig 3.4", "Random Forest Feature Importance Assessment across 13 Clinical Attributes", "15"],
        ["Fig 3.5", "SHAP Beeswarm Summary Plot for Global Feature Impact on Predictions", "16"],
        ["Fig 3.6", "SHAP Force Plot for Local Single Patient Decision Explanation", "16"],
        ["Fig 3.7", "Visily UI Wireframes for College Library Management System Screens", "19"],
        ["Fig 3.8", "Multi-Tier System Architecture Diagram Generated with Eraser.io", "19"],
        ["Fig 3.9", "Eraser.io Entity Relationship Diagram for Library Relational Database", "20"],
        ["Fig 3.10", "Interactive HTML Frontend Interface Rendered inside Google Colab", "21"],
        ["Fig 3.11", "Automated Test Suite Execution Output Showing 100% Pass Rate", "22"],
        ["Fig 3.12", "API Latency Telemetry Simulation with Real-time Surge and AI Mitigation", "23"],
        ["Fig 3.13", "Predictive Maintenance Telemetry Forecast and Resource Saturation Curves", "24"]
    ]'''

text = text.replace(old_lof, new_lof)

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated TOC, LOT, and LOF numbers in compile_perfect_report.py")

