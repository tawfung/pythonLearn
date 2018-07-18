def func():
    print('function in one.py')
print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('one.py is running directly')
else:
    print('one.py has been imported')