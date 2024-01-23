import sys, keyword
print('Python version:', sys.version)
print('Python Interpreter Location:', sys.executable)
print('Python Module search path:')
for dir in sys.path:
    print(dir)
print('Python keywords:')
for word in keyword.kwlist:
    print(word)

