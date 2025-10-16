# ScuffedDiscord
School Web App Development Task

Purpose: Allow viewing of past messages on an online platform.

Plan: Make site to view past messages first, then make non functional requirements such as gacha, javascript and then sendinng messages


| Functional Requirement | Reasoning |
| ------------------------------------------------------------------ | ----------- |
| Sign In Page with User IDs | Allows the same account to send multiple messages |
| Connect Backend allowing the display of messages | Allows messages to be viewed |
| Gacha displaying thing | Allows maybe customisation |
| Audio recordings being sent | Greater file type upload accessability |


| Nonfunctional Requirements | Reasoning |
| ----------- | ----------- |
| IMMACULATE BACKEND | Ease of coding|
| ABSOLUTELY PERFECT COLOURS | Ease to eyes|


**Design Choices:**

*Simple colour scheme:*

A simple colour scheme was to be used, too many complicated colours would increase difficulty in the creation of the website and also potentially make it much more difficult to look at with eyes.

*Colour Choice:*

4 shades of navy, 3 highlight colours (cyan, blueish gray and cream white)

These colours were picked, mainly because Dark Navy is an adequate replacement for black and is softer on eyes. Most borders would be made with a blueish gray outline, which is easy to look at and still distinguishable.

Cyan would be rareley used, and only really used as borders/outlines on important things like the sign out button.

Cream White is going to be the text colour of the messages.

*Font Choice:*

Font IS ANITO. Chosen by Lucas Chen

*Message Display notes:*

Time when the message sent should be displayed. The date on which it was sent should be displayed too!

*Icon Notes*

Icons should be simple and understandable. I will choose extremely simple icons and extremely easy understandable icons.

*Settings Notes*
In the setting users should have the ablity to change the background
Users can upload Images as long as they are safe and for work audiences

Language support.



| Other Design Choices | Reasoning |
| ----------- | ----------- |
| Dark Colour Scheme | Allows colours like grey to be used as accent colours, instead of really bright colours |
| No Dedicated Navigation | Website isnt large enough for dedicated navigation |
| Background image for desktop design |Simple to make (hopefully) and also aesthetically pleasing|



**Week 4 notes**
*Algorithm Design*
Created 2 algorithms, one for logging in and one for signing up. Messages will be integrated much later into the project.

Reset password feature probably will be impossible.

Future algorithms to be made:
- Edit profile
- Send Messages

*Test cases*
Test 1
- ID: t1
- Case name: Log in
- Preconditions: fake account in sql
- Test Steps
1. Type in correct username
2. Type in correct password
3. Hit login
4. Should be sent to homepage.

Test 2
- ID: t2
- Case name: Log in but stupid
- Preconditions: fake account in sql
- Test Steps
1. Type in correct username
2. Type in incorrect password
3. Hit login
4. New text shows up stating that username/password is incorrect.
5. Type in incorrect username
6. Type in correct password
7. Hit login
8. New text shows up stating that username/password is incorrect.

Test 3
- ID: t3
- Case name: Sign up but everything
- Preconditions: fake account in sql
- Test Steps
1. Type in username for existing account
2. Type in 2 identical passwords
3. Hit sign in
4. New text shows up stating that username is taken
5. Change username and one of the password boxes
6. Hit login
7. New text shows up stating that passwords are not identical
8. Change password to correct password
9. Log in!!!
10. Should be sent to homepage

**Documention Logs for Week 6**

table was created
foreign key was createds

Started and finished setting up different webpages except for invalid credentials page.



**Documentation Logs for Week 7 - 10**
absolutely failed to add a new javascript info button. Formatting doesnt like working, gave up.

**Docuementation Log for Holidays**
was overseas. did nothing

**Documentation post holidays (15.10.24)**

1. Made messsages work
Made a whole bunch of code and functions in Database_manager, allowing messages to be finally sent, recieved and instantly recieved. Times are now being displayed on the messages finally with full date and time (including seconds). 

Your own message is now highlighted in a different colour, showing accounts which messages have been sent on it.

Attempted to add cosmetic system (changing the highlight colour), and gave up.

Will require actual database work, and therefore will take too long.

2. Made latest message preview work on main menu
Now shows the latest sent message on the main menu, almost instantaneously. This one doesnt include the time.

Some problems with the message cutting off, but formatting the text which appears conditionally is incredibly difficult, so this has been stopped.

3. Lighthouse reports

![alt text](<Screenshot 2025-10-16 at 9.58.05 am.png>)

GOT THE FINAL 3 TO 100, performance is still at 80 because of image formats, may be fixed and may be completely ignored. Final 3 are completely done for most pages (i may have missed one or two).

Still currently have issues, (non important), but are weigning down the performance numbers. Image formatting is leading to some slowdown.

Update: i have fixed the image formatting issue, the final one is at 99 because of a font style choice, by using google fonts instead, so it cant be increased further. Maybe with design changes it might be possible

4. Working Javascript functinality
Both for sending stuff, but also javascript popups which appear on click. Now backend is fully linked, and is completely attatched to the database. Sign up features and sign in features now completely work.

# How to run the app
clone respitory or download everything.

run main.py in terminal/command prompt

`python3 main.py` or `python main.py`


feel free to use the sign up page, if you would like to use an old login:

username: test
password: test


## ackowledgements

copilot
- help in javascript messaging system
- figuring out meta viewpoint 


rico
- showing me that it was possible to do a message system


TESTING TESTING