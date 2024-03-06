# raccoon-v2
create an exe file : 
First time:
in console write:
pip install pyinstaller
navigate to the appropriate folder using cd then,
pyinstaller reminder.py
pyinstaller --noconsole --onefile reminder.py
then all subsiquint times just write the below in the command prompt to create the command file, however rename the original executable
pyinstaller --noconsole --onefile reminder.py