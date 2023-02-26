Mobile first version of site pics

## Introduction 

Construction Safety Information Blog (CSI) is a blog that focuses on different areas of the contruction industry.  Its aim is to provide informative content for the construction sector so that it can build a community who can share knowledge, ideas and experiences which will be separated into different categories.  These categoreis will be Health and Safety, Quality, Legislation, Projects and Holidays.   The main objective is to share information between different users and delveop robost platform for sharing of related content.  

## Table of Contents
====================

  * [User Experience](#User-Experience)
  * [Strategy - Project Goals](#strategy-project-goals)
  * [Strategy - User Goals](#strategy-user-goals)
  * [User Stories](#user-stories)
  * [Scope - Features Table](#scope-features-table)
  * [Structure - Database](#structure-database)
  * [Skeleton - Wireframes](#skeleton-wireframes)
  * [Surface - Colour Scheme](#surface-colour-scheme)
  * [Surface - Typography](#surface-typography)
  * [Surface - Images](#surface-images)
  * [Features - Features Used ](#features-used)
  * [Technologies - Technologies Used](#technologies-used)
  * [Deployment - Deployment](#deployment)
  * [Testing](#testing)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

 ## User Experience 
 
 ### Strategy Project Goals

The blog aims to provide users with inforamtion in certain categories in realtion to the Construction Industry.  
The blog will be a very simple design design so that it doesnt draw attention from the content on the blog.
Structure of the blog to be easily understood.  
Site navigation to be simple and easy to use so that a user can easily find their way around the site.
Site user to be able to register for an account so that they can log in and  interact with the content in the blog.

### Strategy User Goals

As an admin user they will be able to manage the blog posts and comments on the blog. 
As a site user i want to be able to manage the content that i create
It will allow logged in user to input a post, change and update their own posts
and also view other user posts and to like same.  A logged in user will not be able to change another users post so there will be restrictions on some views.  It will also allow logged in users to leave comments, update and delete their comments and view other users comments.  Again there will be a restriction on views here where a user will not be able to update other user comments.  

## User Stories

 Epics
    This blog project has 5 epics or milestones which are as follows: Create Workspace For Project, User Authentication, User Login, CRUD Functionality and General Functionality. 
   ![image](https://user-images.githubusercontent.com/106515976/221386870-65c76070-7ee1-47c9-adf8-568bf9234ecb.png)

    Each of the above epics have their own user stories with acceptance criteria

    There are 12 user stories in total 
  
    In relation to epic for create workspace for project we have two user stories 
    ![image](https://user-images.githubusercontent.com/106515976/221387101-6543d4fe-78ff-46f2-84bf-1fdfda8a0d55.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387125-5aa3c6cd-085d-488c-b51d-b5e547a7e231.png)

    Epic for user authentication has 2 user stories
    ![image](https://user-images.githubusercontent.com/106515976/221387169-8d725cd5-c77b-45c2-bf96-87a6ce2857d2.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387202-8515a1ce-53b1-423e-9afc-3d654db0cc2a.png)

    Epic for User Login has 2 user stories 
    ![image](https://user-images.githubusercontent.com/106515976/221387240-f4f1b11e-7f32-4091-ab60-f7bb593f6525.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387261-df214247-0da0-402e-924e-74b54aa9e040.png)

    Epic for CRUD functionality has 4 user stories 
    ![image](https://user-images.githubusercontent.com/106515976/221387325-81b42737-f637-4b60-8a5c-6f91f94f7fa7.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387342-d192e372-a6d3-4c9a-8ca6-4c14b6e61375.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387357-6656ca05-3da9-49a4-a935-e5e2c5ffcc15.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387370-5cfdb85a-a0d1-425f-beb1-c4325a23851d.png)

    Epic for General Functionality has 2 user stories 
    ![image](https://user-images.githubusercontent.com/106515976/221387401-0b32c1f4-a8ca-433b-a7b1-cf3d44c0ba1f.png)

    ![image](https://user-images.githubusercontent.com/106515976/221387422-38933c43-d0a8-4cda-90cf-65b8b66f6817.png)

   Each of the above user stories have been labelled as a must have in order to have a fully functional project.  
   Each user story has been labelled to indicate that it is a must have for the project. 

   In order to implement the user stories it is hoped that it will be completed in 4 iteratioins assing 1 week to each iteration 
   Week 1 - Iteration 1
   ![image](https://user-images.githubusercontent.com/106515976/221387626-08b60603-58ff-4df6-ad7e-f676d852915d.png)

   ![image](https://user-images.githubusercontent.com/106515976/221387669-439cd02f-f83b-4b71-aea0-0c178165d733.png)

   Week 2 - Iteration 2
  ![image](https://user-images.githubusercontent.com/106515976/221387708-822299fe-6ec4-4be1-80dc-9bd70fd84129.png)

  ![image](https://user-images.githubusercontent.com/106515976/221387736-dc3a4a98-4cfa-4eed-98e2-9541f3859de6.png)

  Week 3 - Iteration 3 
  ![image](https://user-images.githubusercontent.com/106515976/221387791-b6c99f7e-b61a-49d6-96c9-1b3cbc511aed.png)

  ![image](https://user-images.githubusercontent.com/106515976/221387809-07040347-a8a6-4c7d-b20a-2b1282303255.png)

  Week 4 - Iteration 4
  ![image](https://user-images.githubusercontent.com/106515976/221387850-b61082c6-aefa-414f-9314-b44463531ee5.png)

  ![image](https://user-images.githubusercontent.com/106515976/221387866-46f4dd04-eefc-47f8-920d-897700133b9e.png)
  
  ![image](https://user-images.githubusercontent.com/106515976/221387885-6cac9710-f90f-46fe-8c18-ccad297c2b2e.png)

  The above iterations are only an approximate.  As i am a student and very new to coding languages i found that I would have moved onto other user stories without finishing the previous user story because of errors that were arising and time being spent on a particular user story. 

  ## Scope - Features Table

    Features Tables - Here we have a features table which goes through the list of features that are required in order to render an MVP Product.   
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

    Epics / User Stories / Acceptance Criteria
    Github projects was used in the planning and setting up of this blog project. Here you will see a list of all epics, the user stories connected to these epics and  
    the acceptance criteria for each user story.  Each user story is catgorised into must haves, should have, could have. The Kanban board was used to draw up the individual tasks into different columns namely to do, in progress, done and and will not have..  As each task was worked on it moved from the to do column to the in progress column
    to the final column of done. 
      
  ## Structure - Database

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

## Skeleton - Wireframes

add wireframes

## Surface - Color Scheme

## Surface - Typography

## Surface - Images

## Features Used 
Features 

Items which i did not comp

## Technologies Used 

Languages Used
  - HTML5
  - CSS3
  - JavaScript
  - Python

Libraries and Frameworks and Programs Uses 
  - Django
    Django was used as a web framework
  - Django Template was used a a templating language for Django to display 
    backend date to HTML
  - Bootstrap 5 - used with styling and responsiveness of the blog 
  - Google Fonts - used to import fonts into base html file 
  - GitPod was used for writing code, committing and pushing to GitHub
  - GitHub was used to store the project code after being push from GitPod.
  - Heroku was used to deploy the blog 
  - Bootstrap4 - Bootstrap 4 CSS framework to create layout and styling
  - Python 3.8 - used to code blog
  - ElephantSQL - used for the applications database.

  Packages / Dependecies 
  - Gunicorn used as a Python WSGI HTTP Server to allow the deployment of 
    Django application
  - Summernote has been used as WYSIWYG editor 
  - Cloudinary has been used an an image management platform 

  Database
  - Heroku Postgres was used in production as a service based on PostgresSQL 
    provided by Heroku.

## Deployment 
This project was developed using a GitPod workspace. The code was commited to Git and pushed to GitHub using the terminal.

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1 Create the Heroku App:

2 Select "Create new app" in Heroku.

3 Choose a name for your app and select the location.

4 Attach the Postgres database:

5 In the Resources tab, under add-ons, type in Postgres and select the Heroku 
  Postgres option.

6 Prepare the environment and settings.py file:

6 In the Settings tab, click on Reveal Config Vars and copy the url next to 
  DATABASE_URL.

7 In your GitPod workspace, create an env.py file in the main directory.

8 Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py 
  file.

9 Add the SECRET_KEY value to the Config Vars in Heroku.

10 Update the settings.py file to import the env file and add the SECRETKEY 
   and DATABASE_URL file paths.

11 Update the Config Vars with the Cloudinary url, adding into the settings.py 
   file also.

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

14 Create three directories in the main directory; media, storage and 
   templates.

15 reate a file named "Procfile" in the main directory and add the following:
   web: gunicorn project-name.wsgi

16 Go to Deploy tab on Heroku and connect to the GitHub, then to the required 
   recpository. 

17 Click on Delpoy Branch and wait for the build to load. When the build is 
   complete, the app can be opened through Heroku.

## Testing 

While completing this project i came across a number of errors some exmples of same are below.  

- When saving models file for the Post Model  got the following error:
  TypeError: __init__() got an unexpected keyword argument 'max_lenght'
  content = RichTextField(max_lenght=5000, blank=True, null=True)
  max_length was spelled incorrect;y -  corrected same in post model  
- csiblog.Comment.contributor: (fields.E304) Reverse accessor for 'csiblog. 
  Comment.contributor' clashes with reverse accessor for 'csiblog.Post.contributor'.
  HINT: Add or change a related_name argument to the definition for 'csiblog.Comment.contributor' or 'csiblog.Post.contributor'.
  csiblog.Comment.contributor: (fields.E305) Reverse query name for 'csiblog.Comment.contributor' clashes with reverse query name for 'csiblog.Post.contributor'.
  HINT: Add or change a related_name argument to the definition for 'csiblog.Comment.contributor' or 'csiblog.Post.contributor'.
  csiblog.Post.contributor: (fields.E304) Reverse accessor for 'csiblog.Post.contributor' clashes with reverse accessor for 'csiblog.Comment.contributor'.
  HINT: Add or change a related_name argument to the definition for 'csiblog.Post.contributor' or 'csiblog.Comment.contributor'.
  csiblog.Post.contributor: (fields.E305) Reverse query name for 'csiblog.Post.contributor' clashes with reverse query name for 'csiblog.Comment.contributor'.
  HINT: Add or change a related_name argument to the definition for 'csiblog.Post.contributor' or 'csiblog.Comment.contributor'.
  models.ForeignKey(
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="csiblog_posts")
  got the error above when I tried to makemigrations on the comment model so changed my code to Post rather than user 
- Adding post update 
  Error -   File "/workspace/constructionblog/csiblog/urls.py", line 3, in <module>
  from .views import PostView, PostDetailView, PostAddView, PostUpdateView
  ImportError: cannot import name 'PostUpdateView' from 'csiblog.views' (/workspace/constructionblog/csiblog/views.py)
  File "/workspace/constructionblog/csiblog/urls.py", line 3, in <module>
  from .views import PostView, PostDetailView, PostAddView, PostUpdateView
  I mportError: cannot import name 'PostUpdateView' from 'csiblog.views' (/workspace/constructionblog/csiblog/views.py)
  In my views.py file 
  The code below was indented too far so corrected same and when I did it loaded update page

  class PostUpdate(UpdateView):
        model = Post
        fields = ('name', 'date', 'content',)
        success_url = reverse_lazy('postread.html')

- Add Delete Post functionality  

  Code for View, url and template
  Came across the following errors 
  TemplateSyntaxError at /delete/4
  Unclosed tag on line 3: 'block'. Looking for one of: endblock.

## Finished Product 

## Credits

Content
- Website content written by developer.
- Code Institute Course Material especially blog walkthough "I Think Therefore I Blog"
- Stack Overflow to source and read up on soliving problems with code 
- Tutor Assistance on help to assit errors in code 
- Websites referenced as follows to read up on the django framwork and use of 
  code and follow tutorials
  - https://www.javatpoint.com/django-usercreationform
  - https://realpython.com/
  - https://learndjango.com/
  - https://docs.djangoproject.com/
  - https://ordinarycoders.com/
  - https://www.w3schools.com/
  - https://www.geeksforgeeks.org/
  - https://codemy.com/

Media
- pexels.com 

known Bugs
- 

## Acknowledgements
- My tutor for his feedback and guidance throughout building this blog project.
- Code Institute class facilitator, tutor assistance and student support
- Class on knowlege, guidance and help 
- Cohort lead for her knowlege and help in sourcing study groups and 
  additional reading material  for our class 
- Slack community and study groups and CI mentors for providing tips and 
  knowlege.
- This blog project is for eductional use only and was created for project 
  submittal pp4 for CI.  
