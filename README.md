
# Alert Notifications

A simple python script that sends linux system information as an email/txt alert message. By default it sends a email/txt when the host computer's external IP address changes or if their is a reboot to the computer.

## Motivation

Initially I wanted to set up a media server I can access outside of my home network. I was tempted to use dynamic DNS service so I can get a static url but the best free option (no-ip) I could find required 30 day check ins. I wanted to get a text or email notification when my external IP address changes. 

## Installation
### Dependancies
You need Dig installed globally:

```sh
$ sudo apt-get install dnsutils
```
### setup
I reccomand creating an email account (@gmail.com) for your machine since password must be stored as plaintext locally but it is being sent encrpyted.

To set the configuration file run 'setup.py' inside the program folder. Follow the directions provided by providing a **name for the machine**, a **gmail {email address and password}** and the **e-mail address of where to send the notifications**. You will have to allow less secure access for google so that the script can send out e-mail [here](https://www.google.com/settings/security/lesssecureapps). See section 'configuration' to learn how to use a diffrent email provider, text message setups and extra alerts.

```sh
$ python setup.py
```
After the configuration file is created using 'setup.py' it is time to setup our interval checks. You would use a crontab to periodically alert script every 5 miniutes. Add alertNotifications.py to the crontab if you know how. 

To add the script the the crontab run:
```sh
$ crontab -l > my-crontab
```
Edit my-crontab file (it could be empty) and add a new line as followed for 5 minute intervals. A proper example is provided after you run the setup script.
```sh
*/5 * * * * python /home/yourname/Program/alertNotifications.py
```
After saving the file my-crontab do:
```sh
$ crontab my-crontab
$ rm my-crontab
```

## Configuration
### Getting text messages
To recieve text messages as apposed to email, you can use a email to sms gateway provided by many of the phone carrier companies. For a bigger list check out
[here](http://www.opentextingonline.com/emailtotext.aspx) or [here](http://www.emailtextmessages.com/). For a phone number 123-456-7890 depending on the carrier of your phone, you would use the following e-mail address.

* T-Mobile ------ 1234567890@tmomail.net
* AT&T ---------- 1234567890@txt.att.net
* metro PCS ---- 1234567890@mymetropcs.com
* Sprint ---------- 1234567890@messaging.sprintpcs.com
* Verizon -------- 1234567890@vtext.com

### Using a diffrent email provider
If you have a local smtp server you can
### text message setups and extra alerts.
Sending extra alert messages.
## License
MIT

