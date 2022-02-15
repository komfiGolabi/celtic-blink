# Celtic Blink-E commerce jewellery store
##  Code created by Kamila Golebiowska for Code Institute
## Languages used: HMTL, CSS, Javascript, Python, Bootstrap, Django, AWS


[CoCo Live Page](https://celtic-blink-ms4.herokuapp.com/)


![project on different devices]()


## Project description and goals:

Celtic Blink is a online jewellery store, where you can purchase various celtic designs. Main goal is to sell items and provide a pleasant shopping experience for user.


### Navigation Bar & Footer
 Navigation Bar is a simple with a dropdown menu for login and registration and side menu for the mobile devices.
Footer will be pretty basic, containing the copyright only. It will have colors matching the navigation bar.

### Home Page:


## 
.

![Main collection site]()


### Register/Login



 ![Register/Login]()

 

### Features to add in future




 ## User Goals

 ### First Time User:


 
 ### Returning User
 

## Wireframes
 [Wireframes]()




## Credits

### Content

All text content was written by me-Kamila Golebiowska. 

### Images 
The images for the website were taken from the [Unsplash](https://unsplash.com/images)

[crowd with the mobile phone](https://unsplash.com/photos/JNuKyKXLh8U)
[crowd with a heart gesture](https://unsplash.com/photos/hzgs56Ze49s)
Artists photos that I put into the new concert form were taken from random websites.
[Chronixx](https://www.caribbeannationalweekly.com/caribbean-breaking-news-featured/chronixx-among-nominees-grammys-best-reggae-album/)
[Children of Zeus](https://www.manchestersfinest.com/music/children-of-zeus-announce-uk-tour/)
[Bjork](https://gif-ac.com/bjork-utopia-70/)
[Arrested Development](https://dfw.cbslocal.com/2016/06/22/raps-arrested-development-still-making-music-on-their-terms/)
[Protoje](https://www.rcarecords.com/news/protoje-unleashes-new-studio-album-in-search-of-lost-time-out-today/)
[Glastonbury](https://meaww.com/taylor-swift-headline-glastonbury-2020-paul-mc-cartney-diana-ross-aerosmith-michael-eavis-emily-eavis)



### Icons and Fonts


Logo and Icons used free icons from [Font Awesome](https://fontawesome.com/?from=io)



### Code

 
 
* [Stack Overflow](https://stackoverflow.com/)
* [Free Code Camp](https://www.freecodecamp.org/)
* [W3 schools](https://www.w3schools.com/html/default.asp)
* [Random Key](https://randomkeygen.com/)



#### Django

* First Step was to create the collections in database-MongoDB
 ![Concerts Collection](static/images/concertDB.jpg)
 ![Reviews Collection](static/images/reviews.jpg)
 ![Python Installments](static/images/python-installments.jpg)
* installed Flask and Python libraries, plus created the env.py file to store sensitive data
* connected Github to Heroku to make the deployment automatic.
* wired Flask to MongoDB database, installed flask-pymongo, dnspython and updating requirements,txt file for Heroku
* in app.py file made all the imports and configurations to get info from database
* in MongoDB cluster overview pressed the connect button and chose option to connect with the application, using drivers, where Python is the driver and the version we re working with.
Copied the string underneath to the clipboard, pasted it to the empty space for Mongo_URI in our app.py,we need to add a name of our database there and the password to our dtabase password(not login password).
* the same string will be copied in Heroku settings, with our config var list(check deployment section)



## Handling Bugs and what is remaining
### My struggles


### Existing Bugs

* 

## Testing

[Check responsiveness]()

[HTML Validator Page)

Html validation was throwing errors when used the code from the working environment, so the validation was made by opening the website and using the view source option, when right clicking on the mouse and then validated.
It passed the validation, all pages had the same warning, which refers to the section with flash messages. The rest of the errors has been fixed.

![image of passed html validator page]()


[CSS Validator Page](https://jigsaw.w3.org/css-validator/)
* Code from style.css was copied as a direct input into the CSS validator page and no errors were found.
![image of passed css validator page]()

* ![Jshint validation]()

* Google Dev Tool: Lighthouse 

![Desktop Lighthouse Testing]()
![Mobile Lighthouse Testing]()

Lighthouse testing was fluctuating slightly due to the course of the project and the photos are showing the final results.


* Website was tested on various browsers: Chrome, Microsoft Edge and Mozzila Firefox and on all of those performed well.
 

 ### First Time User:


 ### Returning User
 


## Deployment

1. Created repository with the title of the page "" in GitHub.
2. Created the files in the project required for deployment in Heroku: Procfile and requirements.txt
3. In Heroku web I created a new app and I chose the option that connects GitHub and Heroku, so deploymemt happens automatically, which option Connect to GitHub and choosing the right depository name and pressing Connect button.
3. Before we enable connection went to Settings tab, pressed Reveal Config Vars, where we can tell which variables we need.
4. In the list without the quotation marks I added IP-0.0.0.0, PORT-5000,SECREt_KEY, copieed from env.py file, MONGO_URI and MONGO_DBNAME with the name of our database
5. In coding environment pushed the files created for running Heroku into the repository.
6. Came back to Heroku and pressed Enable Automatic Deployment button and Deploy Branch.

 

 ## Steps to get into the project and how to clone the repository
* Click on the provided link to my Github repository. [Click here for the project]()
* Once inside click on the Code button and press either clone or download.
* Under the option HTTP, press the clipboard, that has the link inside and copy it.
* open the terminal you are using for your computer
* choose the location where you would like to store the repo, locally
* in the terminal now you can use the command git clone and the link.

