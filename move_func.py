with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract def add_frontmatter_table from the bottom
func_lines = []
start_idx = None
for i, line in enumerate(lines):
    if line.startswith('def add_frontmatter_table'):
        start_idx = i
        break

if start_idx is not None:
    func_lines = lines[start_idx:]
    lines = lines[:start_idx]

# Find where def add_table_data is
insert_idx = 0
for i, line in enumerate(lines):
    if line.startswith('def add_table_data'):
        # insert right after add_table_data
        # find end of add_table_data
        for j in range(i+1, len(lines)):
            if lines[j].startswith('def ') or lines[j].startswith('# ---'):
                insert_idx = j
                break
        break

# Insert func_lines at insert_idx
lines = lines[:insert_idx] + ['\n'] + func_lines + ['\n'] + lines[insert_idx:]

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Moved add_frontmatter_table to helper functions section!")

