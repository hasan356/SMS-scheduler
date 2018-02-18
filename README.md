# INSTRUCTIONS 

---

## DETAILS

TWILLO only allows to send to the members who are registerd on twilio . So first make an account 
and get your
    `Account_SID`
    `Account_Token`
and put this details in `credentials.py`

Non registered members cannot have sms from a free account

Also change the starttime and endtime between which you want to get sms in `credentials.py`

## INSTALLATION

- Clone the github repo into your system
- Open the terminal and went to that directory
- Install the redis-server by `sudo apt-get install redis-server` 
- Make the redis-server active by `redis-server`
- Install the dependency by running `pip install -r requirements.txt`

 ## RUNNING
 
 - Make the django application live by typing `python manage.py runserver` into the terminal
 - open the browser and type `localhost:8000/sms_app/`
 - open two other terminals went into that directory and type these commands respectively
   - `celery -A amnesia worker -l info`
   - `celery -A amnesia beat -l info`
   
 ## SCREENSHOTS
 
 #### HOME PAGE
 
 <img src="https://i.imgur.com/vshEY02.png" alt="Home Page" width="800">

#### Successfully registered

<img src="https://i.imgur.com/vshEY02.png" alt="reg Page" width="800">

#### SMS Recived in mobile

<img src="https://i.imgur.com/aPriNVl.png" alt="sms service" width="400" >

## LOG FILE

<img src="https://i.imgur.com/Z3iICRs.png" alt="log file" width="800">

## SEE IT IN ACTION

![GIF](https://thumbs.gfycat.com/HandmadeDependableFlea-size_restricted.gif)