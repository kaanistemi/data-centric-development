<h1>Cocktial Recipies</h1>
This platform is created to inspire, educate and entertain all cocktail-lovers, home-bar owners, professional bartenders & baristas or anyone who'd like to enjoy a cocktail today. Finding the recipe with true amounts
can sometimes be frustrating and there are very few websites dedicated to cocktail recipes only. This website makes it easier for users to search and find all the cocktail recipes they wish on just one page. 
The aim of the website is to provide users a platform where they can find cocktail recipes and create, share and edit their own cocktail recipes.

<h2>UX</h2>
User's have to log in/sign up in order to start using the platform, after they will be directed to the home page where they will be able to see all the cocktails. Picture and a little insight below the name is presented to introduce the coctails. By simply clicking on the cocktails picture, users will be able to see the type of the cocktail and the recipe; as divided into two subheads like "equipments" and “ingredients". If they wish, they will be able to edit or delete these details. 

The structure and navigation of the website is pretty straight-forward. The user can easily navigate through the home page and to other pages by using the nav-bar. On the "Add cocktail" section, they will be able to share their own recipe ideas with the other users. 

The user's primary goal would be easily searching and finding the complete cocktail recipes without no frustration, compare the recipes, ingredients and materials. So, the primary goal of the UX process of this website was to eliminate pain points, complications and interruptions as the other recipe websites have, and it has been made simpler for users to see the recipes with every important detail and being able to compare between them on the same page. This website would be the best way that the users can easily decide what they'll drink, learn new cocktails and how to do it or check what they are doing right or wrong with the cocktail. 

In addition to their primary goal, sharing their new ideas would be another goal of the users. If a user has any idea about the cocktail already given, or has a whole new cocktail recipe, he/she can easily edit the details or add new cocktail if they wish to.

User Story: A bartender would like to know if he does the tequila sunrise right or wrong after having a discussion with a customer. He needs a website that accurately shows the recipe of this cocktail, and approved by many. He logs in to website from his phone, searching for tequila sunrise on the home page. He clicks on the picture and see the ingredients, shows it to his customer and proves his point. However, the customer who likes making her own cocktails, insisting on her idea about making of this cocktail. She thinks it’s a great idea and wants to share it. She logs in to website from her phone, checks the other cocktails to get an insight and compare the recipes. Then, she adds a new cocktail with her own choice of ingredients and share it on the home page. 

- UX Diagram 

[UX Diagram](https://mail.google.com/mail/u/0?ui=2&ik=efec71413a&attid=0.1&permmsgid=msg-f:1671400505061681933&th=173201e7659c2b0d&view=att&disp=safe&realattid=f_kc9dlscp0)

<h2>Features</h2>

<h4>Existing Features</h4>

- Login page directs users main page if login is succesfull otherwise user is directed register page.

- Register page created for user who hasn't singed up yet. After succesful resgistiration user is directed to main page.

- There are 3 list item in nav-bar which are "Home", Add Cocktail" and Log Out. "Log out" allows exiting option from page, "Add Cocktail" provides form to user who wants to add cocktail recepies and
"Home" directs users to main page. On the left side nav-bar "Cockail Recipe" is wtirren which directs user main page as well.

- Cards display cocktails' name, photo, information, equipment, ingredient and level of alcohol. Bottom of the card there are two button that provide user edit and delete option. Edit button opens new page
to allow user editing cocktails by filling form.

- Footer part gives brief information about website, social media links and conctact details.


<h4>Features Left to Implement</h4>

- Adding star rate

- Search button

- Own profile page for each user

- Forgot my password and remember me to login and register page.

- Modal for dialog boxes

<h2>Technologies Used</h2>
[HTML](https://html.com/) and [CSS](https://html.com/)
- For webite's front-end

[JavaScript](https://www.javascript.com/)
- To use a hamburger menu

[Materialize](https://materializecss.com/)
- Materialize to style the website and make it responsive


[Python](https://www.python.org/)
- Python to develop CRUD in back-end

[MongoDB](https://www.mongodb.com/)
- MongoDB to store data records

[Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask to bulild web app

[Werkzeug](https://pypi.org/project/Werkzeug/) 
- Werkzeug to create log in and register page in back-end

[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- Jinja to adding functionality

<h2>Testing</h2>
All features of website work properly and it has tested by me and my mentor few times.
- Login:

    * Go to the "Login" page
    * Try to submit the empty form and verify that an "You must be registered!" appears directs you Register page.
    * Try to submit the form with correct username and wrong password and verify that a Wrong password or user name! message appears and user has to fill the form again
    * Try to submit the form with all inputs valid and verify that it directs user main page

- CRUD:

    * Go to the "Home" page

    * Click the card and read the added formation bottom of the card there are two buttons, when click delete button card dissapear.

    * Clicking Edit button directs user to Edit Cocktail Page with cocktails information to don't make user write all information again.

    * After fill the blanks when click edit cocktails, website take user the main page with changes.

- All links and cards are working as intended and edit cocktails, add cocktails, delete works without problem. Website designed responsive for every device and it is tested on inspected page
and not faced with any issue.

- Begining of the project I faced with cache bug and I couldn't activate css. Eventhough my mentor and tutors has helped me out a lot to solve that bug, it hasn't been sorted yet so I have to copy the link 
on by browser and paste it to incognito to see changings on front-end.

<h2>Deployment</h2>
I've deployed my Project GitHub and Heroku.

- To deploy my project on Github i followed these steps;

    * echo "# data-centric-development-ppp" >> README.md
    * git init
    * git add README.md
    * git commit -m "first commit"
    * git remote add origin https://github.com/kaanistemi/data-centric-development.git
    * git push -u origin master
 
- To deploy on Heroku

    * heroku login
    * heroku git:clone -a data-centronc-project
    * cd data-centronc-project

- and to make changes fot both

    * git add .
    * git commit -am "make it better"
    * git push heroku/origin master



    

<h2>Credit</h2>

<h4>Contents</h4>

The texts for 5 cocktails copied from Wikipedia;

- https://en.wikipedia.org/wiki/Tequila_sunrise_(cocktail)

- https://en.wikipedia.org/wiki/Long_Island_iced_tea

- https://en.wikipedia.org/wiki/Appletini

- https://en.wikipedia.org/wiki/Mojito

- https://en.wikipedia.org/wiki/Fizz_(cocktail)#Gin_fizz

A text for Rhubarb cordial copied from;
- https://www.bbcgoodfood.com/recipes/rhubarb-cordial

<h4>Media</h4>
The photos used in this site were obtained from;

- Tequila Sunrise : https://www.acouplecooks.com/tequila-sunrise/

- Long Island : https://blog.cocktailkit.com.au/wp-content/uploads/2017/05/long-island-iced-tea.jpg

- Appletine : https://i2.wp.com/dishesdelish.com/wp-content/uploads/2020/02/Sour-Appletini-Cocktail-14.jpg

- Mojito : https://www.liquor.com/thmb/qBrBRm02Y-l2BvmF_TZwTtII-EI=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__09__04153106__mojito-720x720-recipe-a55b114fc99c4a64b38c9ef6d1660e20.jpg

- Gin Fizz : https://www.liquor.com/thmb/-OMhbW2k9O0kyVunw85hdQbhdU8=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2017__08__25101601__gin-fizz-720-720-article-d3f54dc6c2d5466e861484a10e3f6f32.jpg

- Rhubarb Cardial : https://simply-delicious-food.com/wp-content/uploads/2018/11/strawberry-blush-gin-and-tonic-3.jpg

<h4>Acknowledgements</h4>

- I received inspiration for this project from Code Institute Data Centric Development Mini Porject and https://www.liquor.com/cocktail-and-other-recipes-4779343


