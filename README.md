**Geodjango Series 1**

This is a geodjango tutorial project(Agricom) developed under the Geodjango Tutorial Series at <a href="https://www.youtube.com/playlist?list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ"> This Playlist</a> . 
It uses the Geodjango module in Django to include the mapping aspect of the project. This is the entire project covered in all the episodes. 

## Set Up
To set up the project, follow the steps;
```
sudo apt-get install postgresql postgresql-contrib \ postgis \ git
```
## On a Virtual Environment

```
Sudo apt-get install python-virtualenv
virtualenv venv
cd venv && . bin/activate
```
## Clone the system
```
git clone https://github.com/wanjohikibui/Geodjango-series.git
```
## Setting up DB
```
sudo -u postgres createuser -P USER_NAME_HERE
sudo -u postgres createdb -O USER_NAME_HERE DATABASE_NAME_HERE #Remember to change in settings.py
#Enable PostGIS
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" DATABASE_NAME_HERE
```
## Installing Requirements
```
pip install -r requirements.txt
```
## Sync and Running application
```
cd agricom
python manage.py migrate
python manage.py runserver
on browser: localhost:8000
```
## Support
For any issue with the application, drop a message via swanjohi@lifeingis.com or join the Telegram Group at https://t.me/joinchat/D6VfOBIfhHh4i8yZ19sqbQ
