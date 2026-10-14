with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines[754] = '    add_h2("3.2 Mini Project 1: Data Science with Generative AI")\n'
lines[859] = '    add_h2("3.3 Mini Project 2: Software Development Using Generative AI")\n'

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Restored add_h2 lines in body!")

