# WhatsApp-Automation
Automate WhatsApp group url using Python Flask

### Steps

- Step 1 : Clone the git project.

- Step 2 : Create a new virtual environment
```
# Install virtualenv if you don't have it
pip install virtualenv

# Create and activate a virtual environment
virtualenv venv
`venv\Scripts\activate` # On Linux use  source venv/bin/activate  
```

- Step 3 : Update WhatsApp group invite urls in groups.json file.

- Step 4 : Install packages
```
pip install -r requirements.txt
```

- Step 5 : Zappa deploy to lambda.
```
zappa init
zappa deploy dev
zappa update dev # If you need update whatsapp group urls or current_group
zappa undeploy dev # If you need destroy full application
```