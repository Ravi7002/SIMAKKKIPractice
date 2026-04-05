import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find {"letter":"X":"Y"} or {"letter":"X":"Y"} or similarly malformed dicts
    # In python terms, it's a string where someone typed {"letter":"A":"Text"} instead of {"letter":"A","text":"Text"}
    # Let's fix missing comma and 'text' key.
    
    # We saw examples like: {"letter":"B":"absorbing"} or {"letter":"A":"Paragraph 1"}
    # Let's use regex: {"letter"\s*:\s*"([A-E])"\s*:\s*([^}]+)}
    
    def replacer(match):
        letter = match.group(1)
        text_val = match.group(2)
        return f'{{"letter":"{letter}", "text":{text_val}}}'

    new_content = re.sub(r'\{"letter"\s*:\s*"([A-E])"\s*:\s*([^}]+)\}', replacer, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("File fixed.")

if __name__ == '__main__':
    fix_file('english_pool_v4.py')
