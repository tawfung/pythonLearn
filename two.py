import one
print('TOP LEVEL IN TWO.PY')
one.func()

if __name__ == '__main__':
    print('two.py is running directly')
else:
    print('two.py has been imported')
    