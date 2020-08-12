# autoinvest
AutoInvest will automatically notify you through email when your bitcoins value is increased by a specified value.

# Prerequisites
There are 2 things we need to do before this will work. First of all, install [git](https://git-scm.com). Second of all, turn on [less secure apps](https://myaccount.google.com/lesssecureapps) on the sender mail. If you have this turned off google will not allow `runserver.py` to send an email.
```
$ git clone https://github.com/vsp0/autoinvest.git
$ cd autoinvest/
$ python gui.py  # Insert your data
$ python runserver.py
...
```

# Server
I would understand if you don't want to go through all the trouble of doing all the things in `Prerequisites`.

Therefore I have hosted a server where `runserver.py` is running 24/7. You can fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLSdJhu4BT988Inf8VZZmir9Za-FHEcYuF9JBZF9i63QgsQGE7A/viewform?usp=sf_link) and I will add you to `users.json` in my server. 

The advantage is that the only thing I need is your email, your amount of bitcoins and lastly the value that'll check how much your bitcoins are in profit.

# Authors
- [vsp](https://github.com/vsp0)

