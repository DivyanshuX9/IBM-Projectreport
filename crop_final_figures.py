import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('processed_figures/final_clean', exist_ok=True)

# -------------------------------------------------------------
# 1. Figure 3.1: Heart Disease 3NF Relational Database Schema ERD
# Let's generate a crisp, beautiful, publication-quality ERD diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Style helper for table boxes
def draw_table(x, y, w, h, title, cols, bg_header='#1a365d', bg_body='#f7fafc', border='#2b6cb0'):
    # Header box
    hdr_h = 0.7
    hdr = patches.FancyBboxPatch((x, y + h - hdr_h), w, hdr_h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                 linewidth=1.5, edgecolor=border, facecolor=bg_header)
    ax.add_patch(hdr)
    ax.text(x + w/2, y + h - hdr_h/2, title, color='white', weight='bold', fontsize=11, ha='center', va='center')
    
    # Body box
    body = patches.FancyBboxPatch((x, y), w, h - hdr_h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                  linewidth=1.5, edgecolor=border, facecolor=bg_body)
    ax.add_patch(body)
    
    # Columns
    line_h = (h - hdr_h - 0.2) / len(cols)
    for i, (col, col_type, is_pk, is_fk) in enumerate(cols):
        cur_y = y + h - hdr_h - 0.2 - i * line_h
        prefix = "[PK] " if is_pk else ("[FK] " if is_fk else "      ")
        weight = 'bold' if (is_pk or is_fk) else 'normal'
        color = '#c53030' if is_pk else ('#2b6cb0' if is_fk else '#2d3748')
        ax.text(x + 0.2, cur_y, f"{prefix}{col}", color=color, weight=weight, fontsize=9, va='center', family='monospace')
        ax.text(x + w - 0.2, cur_y, col_type, color='#718096', fontsize=8, ha='right', va='center', family='monospace')

# Table 1: Patients
cols_patients = [
    ('patient_id', 'INTEGER (PK)', True, False),
    ('age', 'INTEGER', False, False),
    ('sex', 'INTEGER', False, False),
    ('cp', 'INTEGER', False, False)
]
draw_table(0.4, 1.2, 2.7, 2.8, "Patients (Demographics)", cols_patients)

# Table 2: Patient_Stats
cols_stats = [
    ('stat_id', 'INTEGER (PK)', True, False),
    ('patient_id', 'INTEGER (FK)', False, True),
    ('trestbps', 'REAL', False, False),
    ('chol', 'REAL', False, False),
    ('fbs', 'INTEGER', False, False),
    ('restecg', 'INTEGER', False, False)
]
draw_table(3.6, 0.6, 2.8, 3.8, "Patient_Stats (Vitals)", cols_stats)

# Table 3: Medical_Tests
cols_tests = [
    ('test_id', 'INTEGER (PK)', True, False),
    ('patient_id', 'INTEGER (FK)', False, True),
    ('thalch', 'REAL', False, False),
    ('exang', 'INTEGER', False, False),
    ('oldpeak', 'REAL', False, False),
    ('slope', 'INTEGER', False, False),
    ('ca', 'REAL', False, False),
    ('thal', 'REAL', False, False),
    ('num (target)', 'INTEGER', False, False)
]
draw_table(6.9, 0.2, 2.8, 4.4, "Medical_Tests (Cardiac)", cols_tests)

# Draw arrows for FK relationships
# Patients -> Patient_Stats
arrow1 = patches.FancyArrowPatch((3.1, 3.2), (3.6, 3.6), connectionstyle="arc3,rad=-0.15",
                                 arrowstyle="->", mutation_scale=15, color='#2b6cb0', linewidth=1.8)
ax.add_patch(arrow1)
ax.text(3.35, 3.6, "1:N", color='#2b6cb0', weight='bold', fontsize=8)

# Patients -> Medical_Tests
arrow2 = patches.FancyArrowPatch((3.1, 2.8), (6.9, 3.8), connectionstyle="arc3,rad=-0.25",
                                 arrowstyle="->", mutation_scale=15, color='#2b6cb0', linewidth=1.8)
ax.add_patch(arrow2)
ax.text(5.0, 3.65, "1:N", color='#2b6cb0', weight='bold', fontsize=8)

plt.tight_layout()
plt.savefig('processed_figures/final_clean/fig3_1_erd_heart.png', bbox_inches='tight', dpi=300)
plt.close()
print("Saved clean fig3_1_erd_heart.png")

# -------------------------------------------------------------
# 2. Figure 3.2: Univariate and Bivariate Distributions Dashboard (image15.png)
# -------------------------------------------------------------
im15 = Image.open('extracted_images/image15.png')
# Crop minimal border
arr15 = np.array(im15.convert('RGB'))
is_white = (arr15[:, :, 0] > 245) & (arr15[:, :, 1] > 245) & (arr15[:, :, 2] > 245)
r = np.where(~is_white.all(axis=1))[0]
c = np.where(~is_white.all(axis=0))[0]
crop15 = im15.crop((c[0], r[0], c[-1], r[-1]))
crop15.save('processed_figures/final_clean/fig3_2_eda_dashboard.png')
print("Saved clean fig3_2_eda_dashboard.png", crop15.size)

# -------------------------------------------------------------
# 3. Figure 3.3: Bivariate Scatter and Boxplots (image13.png & image14.png)
# -------------------------------------------------------------
im13 = Image.open('extracted_images/image13.png')
arr13 = np.array(im13.convert('RGB'))
is_white = (arr13[:, :, 0] > 245) & (arr13[:, :, 1] > 245) & (arr13[:, :, 2] > 245)
r = np.where(~is_white.all(axis=1))[0]
c = np.where(~is_white.all(axis=0))[0]
crop13 = im13.crop((c[0], r[0], c[-1], r[-1]))
crop13.save('processed_figures/final_clean/fig3_3_bivariate_scatter.png')
print("Saved clean fig3_3_bivariate_scatter.png", crop13.size)

# -------------------------------------------------------------
# 4. Figure 3.4: Random Forest Feature Importance (image18.png)
# -------------------------------------------------------------
im18 = Image.open('extracted_images/image18.png')
arr18 = np.array(im18.convert('RGB'))
is_white = (arr18[:, :, 0] > 245) & (arr18[:, :, 1] > 245) & (arr18[:, :, 2] > 245)
r = np.where(~is_white.all(axis=1))[0]
c = np.where(~is_white.all(axis=0))[0]
crop18 = im18.crop((c[0], r[0], c[-1], r[-1]))
crop18.save('processed_figures/final_clean/fig3_4_rf_importance.png')
print("Saved clean fig3_4_rf_importance.png", crop18.size)

# -------------------------------------------------------------
# 5. Figure 3.5: SHAP Beeswarm Plot (image19.png)
# -------------------------------------------------------------
im19 = Image.open('extracted_images/image19.png')
arr19 = np.array(im19.convert('RGB'))
is_white = (arr19[:, :, 0] > 245) & (arr19[:, :, 1] > 245) & (arr19[:, :, 2] > 245)
r = np.where(~is_white.all(axis=1))[0]
c = np.where(~is_white.all(axis=0))[0]
crop19 = im19.crop((c[0], r[0], c[-1], r[-1]))
crop19.save('processed_figures/final_clean/fig3_5_shap_beeswarm.png')
print("Saved clean fig3_5_shap_beeswarm.png", crop19.size)

# -------------------------------------------------------------
# 6. Figure 3.6: SHAP Force Plot (image20.png) - tightly cropped!
# -------------------------------------------------------------
im20 = Image.open('extracted_images/image20.png')
# Force plot has top text, bar, and arrows down to y~334
# Let's crop tightly from y=20 to y=336 and x=10 to x=2195
crop20 = im20.crop((10, 18, 2195, 336))
crop20.save('processed_figures/final_clean/fig3_6_shap_force.png')
print("Saved clean fig3_6_shap_force.png", crop20.size)

# -------------------------------------------------------------
# 7. Figure 3.7: Visily UI Wireframes (from crop_28.png)
# -------------------------------------------------------------
im_vis = Image.open('processed_figures/auto_crops/crop_28.png')
# Remove top commercial banner: top banner is y=0..38
crop_vis = im_vis.crop((0, 38, im_vis.size[0], im_vis.size[1]))
crop_vis.save('processed_figures/final_clean/fig3_7_visily_wireframes.png')
print("Saved clean fig3_7_visily_wireframes.png", crop_vis.size)

# -------------------------------------------------------------
# 8. Figure 3.8: Eraser.io Architecture Diagram (from crop_29.png top half)
# -------------------------------------------------------------
im_eraser = Image.open('processed_figures/auto_crops/crop_29.png')
# In crop_29, Architecture is roughly y=20 to y=330, width=0..945
crop_arch = im_eraser.crop((0, 20, im_eraser.size[0], 335))
crop_arch.save('processed_figures/final_clean/fig3_8_eraser_architecture.png')
print("Saved clean fig3_8_eraser_architecture.png", crop_arch.size)

# -------------------------------------------------------------
# 9. Figure 3.9: Eraser.io Database ERD (from crop_29.png bottom half)
# -------------------------------------------------------------
# In crop_29, ERD is roughly y=340 to y=855
crop_erd = im_eraser.crop((0, 340, im_eraser.size[0], 855))
crop_erd.save('processed_figures/final_clean/fig3_9_eraser_erd.png')
print("Saved clean fig3_9_eraser_erd.png", crop_erd.size)

# -------------------------------------------------------------
# 10. Figure 3.10: Interactive HTML Frontend (from crop_40.png top half)
# -------------------------------------------------------------
im_html = Image.open('processed_figures/auto_crops/crop_40.png')
# Top half of crop_40 is the HTML UI: y=0 to y=375
crop_html = im_html.crop((0, 0, im_html.size[0], 375))
crop_html.save('processed_figures/final_clean/fig3_10_html_frontend.png')
print("Saved clean fig3_10_html_frontend.png", crop_html.size)

# -------------------------------------------------------------
# 11. Figure 3.11: Automated Test Suite Output (from crop_42.png top half)
# -------------------------------------------------------------
im_test = Image.open('processed_figures/auto_crops/crop_42.png')
# Test suite report is y=0 to y=385
crop_test = im_test.crop((0, 0, im_test.size[0], 385))
crop_test.save('processed_figures/final_clean/fig3_11_test_suite_output.png')
print("Saved clean fig3_11_test_suite_output.png", crop_test.size)

# -------------------------------------------------------------
# 12. Figure 3.12: API Latency Telemetry Simulation (from crop_43.png top half)
# -------------------------------------------------------------
im_lat = Image.open('processed_figures/auto_crops/crop_43.png')
# Latency telemetry and alerts is y=140 to y=585
crop_lat = im_lat.crop((0, 140, im_lat.size[0], 585))
crop_lat.save('processed_figures/final_clean/fig3_12_telemetry_simulation.png')
print("Saved clean fig3_12_telemetry_simulation.png", crop_lat.size)

# -------------------------------------------------------------
# 13. Figure 3.13: Predictive Maintenance Telemetry (from crop_44.png)
# -------------------------------------------------------------
im_pred = Image.open('processed_figures/auto_crops/crop_44.png')
# Predictive metrics and recommendations is y=220 to y=695
crop_pred = im_pred.crop((0, 220, im_pred.size[0], 695))
crop_pred.save('processed_figures/final_clean/fig3_13_predictive_maintenance.png')
print("Saved clean fig3_13_predictive_maintenance.png", crop_pred.size)

print("\nALL 13 FIGURES PROCESSED CLEANLY AND STORED IN processed_figures/final_clean/")

