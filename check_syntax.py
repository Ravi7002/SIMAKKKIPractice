import traceback
try:
    with open('english_pool_v4.py', 'r') as f:
        content = f.read()
    compile(content, 'english_pool_v4.py', 'exec')
    print("OK")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg} at line {e.lineno}")
except Exception as e:
    print(f"Error: {e}")
