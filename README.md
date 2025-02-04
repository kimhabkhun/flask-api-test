## Getting Start
Before starting the project, Please clone the project via [link](http://www.example.com) by run the following command.

## 1.Clone Project
  ```bash
    git clone http://www.example.com/repo
    cd repo
  ```
## 2.Then setup requirement environment with "requirements.txt"
For Debain/Linux:
```bash
    python -m venv env
    source venv/bin/activate # On Windows: venv\Scripts\activate
```

## 3.Install Dependencies:
```bash
pip install -r requirements.txt [install dependency in requirements.txt]
pip freeze > requirements.txt [update a new install dependency to requirements.txt]

```
## 4.Run Server:
```bash
py main.py
```

# Structure Project

```bash
flask-api/               # Root folder
│── /env/                # Virtual environment (optional)
│── /instance/           # Instance folder (holds config, db)
│── /migrations/         # Flask-Migrate files (if using Flask-Migrate)
│── /configs/            # Configurations
│   ├── __init__.py      # Initializes config module
│   ├── config.py        # Database & app configurations
│── /app/                # Main application package
│   ├── __init__.py      # Initializes app & database
│   ├── models.py        # Database models
│   ├── routes.py        # Routes (Views)
│   ├── forms.py         # Flask-WTF Forms (if needed)
│   ├── services.py      # Business logic (optional)
│   ├── utils.py         # Utility/helper functions (optional)
│── /templates/          # HTML templates
│   ├── layout.html      # Base layout
│   ├── index.html       # Home page
│── /static/             # Static files (CSS, JS, images)
│   ├── css/             # CSS files
│   ├── js/              # JavaScript files
│   ├── images/          # Image assets
│── .gitignore           # Git ignore file
│── requirements.txt     # Dependencies : run (pip freeze > requirements.txt)
│── config.py            # Global configurations
│── run.py               # Entry point to run the Flask app
│── init_db.py           # Script to initialize the database
│── README.md            # Project documentation
```

