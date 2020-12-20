#nothing important here
def setup():
    import os
    choice = input('Skip installing (y/n) > ')
    if choice == 'n':
        print("installing modules...")
        cmds = [
            "pip install setuptools",
            "pip install twine",
            "pip install wheel"
        ]
        for i in cmds:
            os.system(i)
    os.system("python3 setup.py sdist bdist_wheel")
    print("Login:")
    os.system("python3 -m twine upload --repository pypi dist/*")
    # you will have to maually enter your username and password.

input("[ENTER]")
setup()