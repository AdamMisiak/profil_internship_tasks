# Profil intern tasks

Tasks created for back-end intern in Profil Software company.


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Technologies
* Python version: 3.7

## Setup
To create virtual environment:
```
python3 -m venv venv
```

To install requirements:
```
pip install -r requirements.txt
```

To create database:
```
python script.py create-db
```

To get percentage of men/women:
```
python script.py male-female-percentage
```

To get average age of men/women/all:
```
python script.py average-age --arg [male/female/all]
```

To get N most popular cities:
```
python script.py most-common-cities --arg [N]
```

To get N most popular passwords:
```
python script.py most-common-passwords --arg [N]
```

To get people born between 2 dates:
```
python script.py dob-between --start [yyyy/mm/dd] --end [yyyy/mm/dd]
```

To get descending list of the safest passwords:
```
python script.py safety-of-passwords
```
To delete error:
```
django.db.utils.OperationalError: no such table: queries_person
```
or
```
sqlite3.OperationalError: no such table: queries_person
```
Use:
```
python manage.py migrate
```

To run tests:
```
python -m unittest -v test_script/test_script.py
```

## Contact
Created by Adam Misiak
