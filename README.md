# raccoon-v2
clone the code :)

create an exe file :

First time:

in console write the following:
```commandline
pip install pyinstaller
```
navigate to the appropriate folder using cd

```commandline
pyinstaller reminder.py
pyinstaller --noconsole --onefile reminder.py
```

then all subsequent times just write the below in the command prompt to create the command file,
however rename the original executable
```commandline
pyinstaller --noconsole --onefile reminder.py
```

if the above doesn't work try:
idk what is going on
```commandline
py -m PyInstaller -F --noconsole reminder.py
```

and if the install aint working try:
```commandline
 py -m pip install pyinstaller
```
