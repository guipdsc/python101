# Virtual Environment and Requirements

### venv
```
python3 -m venv <name>
. <name>/bin/activate
```

### pip
```
python3 -m pip install <package-name>
python3 -m pip uninstall <package-name>

python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
```

### example
```
python3 -m venv kivy_venv
. kivy_venv/bin/activate
pip install -r requirements.txt
python kivy_venv/share/kivy-examples/camera/main.py
```