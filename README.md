Mobile first version of site pics

## Introduction 

Construction Safety Information Blog (CSI) is a blog that focuses on different areas of the contruction industry.  Its aim is to provide informative content for the construction sector so that it can build a community who can share knowledge, ideas and experiences which will be separated into different categories.  These categoreis will be Health and Safety, Quality, Legislation, Projects and Holidays.   The main objective is to share information between different users and delveop robost platform for sharing of related content.  

## Table of Contents
---

1. User Experience (UX)
   (a) Stratgey
       - Project Goals
       - User Goals


    (a) Strategy
        - Project Goals
          The blog aims to provide users with inforamtion in certain categories in realtion to the Construction Industry.  
          The blog will be a very simple design design so that it doesnt draw attention from the content on the blog.
          Structure of the blog to be easily understood.  
          Site navigation to be simple and easy to use so that a user can easily find their way around the site.
          Site user to be able to register for an account so that they can log in and  interact with the content in the blog.

        - User Goals
          As an admin user they will beable to manage the blog posts and comments on the blog. 
          Adn ad 
          As a site user i want to be able to manage the content that i create
          It will allow logged in user to input a post, change and update their own posts
          and also view other user posts and to like same.  A logged in user will not be able to change another users post so there will be restrictions on some views.  It will also allow logged in users to leave comments, update and delete their comments and view other users comments.  Again there will be a restriction on views here where a user will not be able to update other user comments.  

    Table
    | User Type | Feature | Importance | Viability | Delivered | MVP |
    |----------| ----------| ----------| ---------- | ---------- | ---------- |
    |          | User Roles  | 5 | 5  | &check; | MVP|
    |Site Users and Site Admin | Responsive Design | 5 | 5 | &check; | MVP |
    |Site Users & Site Admin | Account Registration | 5 | 5 | &check; | MVP |
    |Site Users & Site Admin | Create, Update and Delete Post  |  5 | 5 | &check; | MVP |
    |Site Users & Site Admin | Create, Update and Delete Comments |  5 | 5 | &check; | MVP |
    |Site Users & Site Admin | Search Construction Categories |  5 | 5 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Responsive Design | Row 2, Column 2 | Row 2, Column 3 |Row 2, Column 1 | &check; | MVP |
    | Total  || x | x|  | |




    Scope

    User Stories 
    GitHub was used in this project to manage and track the user stories.  The Kanban board was used to draw up the individual tasks
    into different columns namely to do, in progress and done.  As each task was worked on it moved from the to do column to the in progress column
    to the final column of done. 

    Week 1 






    Structure of Blog Site 
    diagram of pages and blog site

    Header, footer and navigation bar consistent through all pages.
    links, buttons and forms provide feedback to the user of the site. 
    When a user signs up to the blog they have the opportunity to interact with the content by adding, deleting, updating their own posts and comments and  viewing, liking other posts and comments 

    Database Model 
    The database model is displayed on drawsql.  The type of database being used for this project is relational database which is managaed by PostgreSQL.
    
    put in draw sql diagram

    The CSI blog has four Models 
    Post Model
    Name - this is the name given to the post by the contributor .
    Category - the post will fall into a category from the folloiwng list - Health and Safety, Quality, Legislation, Project and Holidays. 
    Slug - a unique slug to identify the post. 
    Contributor - the user who is adding the post.  
    Date - stores the current date of the post.
    Revised - stores the revision date of a post by contributor.
    Image - stores the image that will be displayed with the post.
    Content - content that is inputted by the contributor.  
    No of Likes - the number of likes that a post has received.
    Excerpt - snippet of the post.  
    Status - this will store wheather the post is approved or not approved.  

    Comment Model 
    Post - a foreign key from the post model storeing post being commented.
    on.  
    Title - stores the title of the comment. 
    Author - a foreign key from the post  model storing the author.
    Added - date the comment was added.
    Mainbody - content that is inputted by the author.  
    Approved - indicates where the comment is approved or not 

    Review Model
    Score - will store a score ---------come back to 

    Category Model
    Name - stores the name of each category.  

    Wireframes 


    Color Schemes 

    Typography

    Features 


    ## Technologies Used 
    ------
    Languages Used
    - HTML5
    - CSS3
    - JavaScript
    - Python

    ## Libraries and Frameworks and Programs Uses 
    - Django
      Django was used as a web framework
    - Django Template was used a a templating language for Django to display backend date to HTML
    - Bootstrap 5 - used with styling and responsiveness of the blog 
    - Google Fonts - used to import fonts into base html file 
     - GitPod was used for writing code, committing and pushing to GitHub
    - GitHub was used to store the project code after being push from GitPod.
    - Heroku was used to deploy the blog 
    - Bootstrap4 - Bootstrap 4 CSS framework to create layout and styling
    - Python 3.8 - used to code blog
    - ElephantSQL - used for the applications database.

    ## Packages / Dependecies 
    - Gunicorn used as a Python WSGI HTTP Server to allow the deployment of Django application
    - Summernote has been used as WYSIWYG editor 
    - Cloudinary has been used an an image management platform 

    ## Database
    - Heroku Postgres was used in production as a service based on PostgresSQL provided by Heroku.


    ## Testing 


    ## Deployment 
    This project was developed using a GitPod workspace. The code was commited to Git and pushed to GitHub using the terminal.

Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1 Create the Heroku App:

2 Select "Create new app" in Heroku.

3 Choose a name for your app and select the location.

4 Attach the Postgres database:

5 In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

6 Prepare the environment and settings.py file:

6 In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.

7 In your GitPod workspace, create an env.py file in the main directory.

8 Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.

9 Add the SECRET_KEY value to the Config Vars in Heroku.

10 Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.

11 Update the Config Vars with the Cloudinary url, adding into the settings.py file also.

12 In settings.py add the following sections:
- Cloudinary to the INSTALLED_APPS list
- STATICFILE_STORAGE
- STATICFILES_DIRS
- STATIC_ROOT
- MEDIA_URL
- DEFAULT_FILE_STORAGE
- TEMPLATES_DIR
- Update DIRS in TEMPLATES with TEMPLATES_DIR
- Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

13 Store Static and Media files in Cloudinary and Deploy to Heroku:

14 Create three directories in the main directory; media, storage and templates.

15 reate a file named "Procfile" in the main directory and add the following:
web: gunicorn project-name.wsgi

16 Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository. 

17 Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

## Finished Product 

# Credits
------
Content
- Website content written by developer.
- Code Institute Course Material especially blog walkthough "I Think Therefore I Blog"
- Stack Overflow to source and read up on soliving problems with code 
- Tutor Assistance on help to assit errors in code 
- Websites referenced as follows to read up on the django framwork and use of code and follow tutorials
  - https://www.javatpoint.com/django-usercreationform
  - https://realpython.com/
  - https://learndjango.com/
  - https://docs.djangoproject.com/
  - https://ordinarycoders.com/
  - https://www.w3schools.com/
  - https://www.geeksforgeeks.org/
  - https://codemy.com/

Media
- 

Code
- 

known Bugs
- 


Acknowledgements
- My tutor for his feedback and guidance throughout building this blog project.
- Code Institute class facilitator, tutor assistance and student support
- Class on knowlege and guidance
- Slack community and study groups and CI mentors for providing tips and knowlege.
- This blog project is for eductional use only and was created for project submittal pp4 for CI.  


