import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')

def draw_table(x, y, w, h, title, cols, bg_header='#1e3a8a', bg_body='#f8fafc', border='#2563eb'):
    # Header box
    hdr_h = 0.65
    hdr = patches.FancyBboxPatch((x, y + h - hdr_h), w, hdr_h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                 linewidth=1.5, edgecolor=border, facecolor=bg_header)
    ax.add_patch(hdr)
    ax.text(x + w/2, y + h - hdr_h/2, title, color='white', weight='bold', fontsize=10.5, ha='center', va='center')
    
    # Body box
    body = patches.FancyBboxPatch((x, y), w, h - hdr_h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                  linewidth=1.5, edgecolor=border, facecolor=bg_body)
    ax.add_patch(body)
    
    # Columns
    line_h = (h - hdr_h - 0.2) / len(cols)
    for i, (col, col_type, is_pk, is_fk) in enumerate(cols):
        cur_y = y + h - hdr_h - 0.2 - i * line_h
        prefix = "[PK] " if is_pk else ("[FK] " if is_fk else "     ")
        weight = 'bold' if (is_pk or is_fk) else 'normal'
        color = '#dc2626' if is_pk else ('#2563eb' if is_fk else '#1f2937')
        ax.text(x + 0.15, cur_y, f"{prefix}{col}", color=color, weight=weight, fontsize=8.5, va='center', family='sans-serif')
        ax.text(x + w - 0.15, cur_y, col_type, color='#64748b', fontsize=8, ha='right', va='center', family='sans-serif')

# Table 1: Patients (x=0.4, y=1.2, w=2.8, h=2.8)
cols_patients = [
    ('patient_id', 'INTEGER (PK)', True, False),
    ('age', 'INTEGER', False, False),
    ('sex', 'INTEGER', False, False),
    ('cp', 'INTEGER', False, False)
]
draw_table(0.4, 1.2, 2.8, 2.8, "Patients (Demographics)", cols_patients)

# Table 2: Patient_Stats (x=3.9, y=0.5, w=2.9, h=3.8)
cols_stats = [
    ('stat_id', 'INTEGER (PK)', True, False),
    ('patient_id', 'INTEGER (FK)', False, True),
    ('trestbps', 'REAL', False, False),
    ('chol', 'REAL', False, False),
    ('fbs', 'INTEGER', False, False),
    ('restecg', 'INTEGER', False, False)
]
draw_table(3.9, 0.5, 2.9, 3.8, "Patient_Stats (Vitals)", cols_stats)

# Table 3: Medical_Tests (x=7.5, y=0.1, w=3.1, h=4.5)
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
draw_table(7.5, 0.1, 3.1, 4.5, "Medical_Tests (Cardiac)", cols_tests)

# Arrow 1: Patients.patient_id -> Patient_Stats.patient_id
arrow1 = patches.ConnectionPatch(xyA=(3.2, 3.1), xyB=(3.9, 3.15), coordsA='data', coordsB='data',
                                 arrowstyle="->", shrinkA=2, shrinkB=2, mutation_scale=14,
                                 color='#2563eb', linewidth=1.8, connectionstyle="arc3,rad=-0.1")
ax.add_artist(arrow1)
ax.text(3.55, 3.3, "1:N", color='#2563eb', weight='bold', fontsize=8.5, ha='center')

# Arrow 2: Patients.patient_id -> Medical_Tests.patient_id (curving over the top)
arrow2 = patches.ConnectionPatch(xyA=(1.8, 4.0), xyB=(9.0, 4.6), coordsA='data', coordsB='data',
                                 arrowstyle="->", shrinkA=2, shrinkB=2, mutation_scale=14,
                                 color='#2563eb', linewidth=1.8, connectionstyle="arc3,rad=0.25")
ax.add_artist(arrow2)
ax.text(5.5, 4.8, "1:N Relationship (patient_id)", color='#2563eb', weight='bold', fontsize=8.5, ha='center')

plt.tight_layout()
plt.savefig('processed_figures/final_clean/fig3_1_erd_heart.png', bbox_inches='tight', dpi=300)
plt.close()
print("Saved perfected fig3_1_erd_heart.png")

