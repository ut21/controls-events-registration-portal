How to run?
```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Functionalities:
1) User authorisation and authentication
2) Consolidated platform to register events and their details
3) Allows admin to approve events. Users can view their approved events and which events are pending approval
4) Allows admin to generate excels and CSV of events as a whole and seperate excels based on different fieldsets on the Event model (excels of requisitions, travels, etc.

To Add (The site is currently mainly proof of concept, adding these features, though non trivial, is not difficult):
1) Make a seperate admin site
2) Connect to Google Sheets API
3) Add notifications and automated email sending
4) Create jobstream wise models that inherit from the Event model and create seperate admins for them
