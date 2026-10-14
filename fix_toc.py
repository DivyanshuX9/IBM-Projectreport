with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if '3.2 Mini Project 1: Data Science with Generative AI' in lines[i]:
        lines[i] = '        ["", "      3.2 Mini Project 1: Data Science with Generative AI", "09"],\n'
    elif '3.3 Mini Project 2: Software Development Using Generative AI' in lines[i]:
        lines[i] = '        ["", "      3.3 Mini Project 2: Software Development Using Generative AI", "17"],\n'
    elif 'CONCLUSION AND FUTURE SCOPE' in lines[i] and i < 520:
        lines[i] = '        ["4", "CONCLUSION AND FUTURE SCOPE", "26"],\n'
    elif 'REFERENCES' in lines[i] and i < 520:
        lines[i] = '        ["", "REFERENCES", "28"],\n'
    elif 'APPENDIX I' in lines[i] and i < 520:
        lines[i] = '        ["", "APPENDIX I", "29"]\n'

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("TOC safely updated via fix_toc.py")

