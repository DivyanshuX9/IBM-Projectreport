import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(11, 4.8), dpi=300)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')

def draw_table(x, y, w, h, title, cols, bg_header='#1e3a8a', bg_body='#ffffff', border='#3b82f6'):
    hdr_h = 0.65
    # Full card border/shadow
    shadow = patches.FancyBboxPatch((x+0.04, y-0.04), w, h, boxstyle="round,pad=0.01,rounding_size=0.06",
                                    linewidth=0, facecolor='#e2e8f0')
    ax.add_patch(shadow)
    
    # Body box
    body = patches.FancyBboxPatch((x, y), w, h - hdr_h, boxstyle="round,pad=0.01,rounding_size=0.06",
                                  linewidth=1.2, edgecolor=border, facecolor=bg_body)
    ax.add_patch(body)
    
    # Header box
    hdr = patches.FancyBboxPatch((x, y + h - hdr_h), w, hdr_h, boxstyle="round,pad=0.01,rounding_size=0.06",
                                 linewidth=1.2, edgecolor=border, facecolor=bg_header)
    ax.add_patch(hdr)
    ax.text(x + w/2, y + h - hdr_h/2, title, color='white', weight='bold', fontsize=10, ha='center', va='center')
    
    # Columns
    line_h = (h - hdr_h - 0.25) / len(cols)
    for i, (col, col_type, is_pk, is_fk) in enumerate(cols):
        cur_y = y + h - hdr_h - 0.2 - i * line_h
        prefix = "[PK] " if is_pk else ("[FK] " if is_fk else "     ")
        weight = 'bold' if (is_pk or is_fk) else 'normal'
        color = '#dc2626' if is_pk else ('#2563eb' if is_fk else '#1f2937')
        ax.text(x + 0.15, cur_y, f"{prefix}{col}", color=color, weight=weight, fontsize=8.5, va='center', family='sans-serif')
        ax.text(x + w - 0.15, cur_y, col_type, color='#64748b', fontsize=8, ha='right', va='center', family='sans-serif')

# Table 1: Patients (x=0.5, y=1.2, w=2.8, h=2.8)
cols_patients = [
    ('patient_id', 'INTEGER (PK)', True, False),
    ('age', 'INTEGER', False, False),
    ('sex', 'INTEGER', False, False),
    ('cp', 'INTEGER', False, False)
]
draw_table(0.5, 1.2, 2.8, 2.8, "Patients (Demographics)", cols_patients)

# Table 2: Patient_Stats (x=4.1, y=0.5, w=2.9, h=3.8)
cols_stats = [
    ('stat_id', 'INTEGER (PK)', True, False),
    ('patient_id', 'INTEGER (FK)', False, True),
    ('trestbps', 'REAL', False, False),
    ('chol', 'REAL', False, False),
    ('fbs', 'INTEGER', False, False),
    ('restecg', 'INTEGER', False, False)
]
draw_table(4.1, 0.5, 2.9, 3.8, "Patient_Stats (Vitals)", cols_stats)

# Table 3: Medical_Tests (x=7.7, y=0.1, w=3.0, h=4.5)
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
draw_table(7.7, 0.1, 3.0, 4.5, "Medical_Tests (Cardiac)", cols_tests)

# Draw clean orthogonal bus connectors
# From Patients patient_id (x=3.3, y=3.05)
ax.plot([3.3, 3.7], [3.05, 3.05], color='#2563eb', linewidth=1.8)
ax.plot([3.7, 3.7], [3.05, 4.6], color='#2563eb', linewidth=1.8) # vertical bus up

# Branch to Patient_Stats (x=4.1, y=3.3)
ax.plot([3.7, 4.1], [3.3, 3.3], color='#2563eb', linewidth=1.8)
ax.plot(4.08, 3.3, marker='>', color='#2563eb', markersize=6)
ax.text(3.75, 3.42, "1 : N", color='#2563eb', weight='bold', fontsize=8)

# Bus continues over Patient_Stats to Medical_Tests (x=7.7, y=3.8)
ax.plot([3.7, 7.3], [4.6, 4.6], color='#2563eb', linewidth=1.8)
ax.plot([7.3, 7.3], [4.6, 3.8], color='#2563eb', linewidth=1.8)
ax.plot([7.3, 7.7], [3.8, 3.8], color='#2563eb', linewidth=1.8)
ax.plot(7.68, 3.8, marker='>', color='#2563eb', markersize=6)
ax.text(7.35, 3.92, "1 : N", color='#2563eb', weight='bold', fontsize=8)

ax.text(5.5, 4.75, "Foreign Key Relationships (patient_id)", color='#1e3a8a', weight='bold', fontsize=9, ha='center')

plt.tight_layout()
plt.savefig('processed_figures/final_clean/fig3_1_erd_heart.png', bbox_inches='tight', dpi=300)
plt.close()
print("Saved perfect orthogonal fig3_1_erd_heart.png")

