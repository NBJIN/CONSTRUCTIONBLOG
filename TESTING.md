[Link Back to Main Readme Document](README.md)

## 14. Testing
#

## Table of Contents
1. Testing User Stories

2. Code Validation

3. Accessibility

4. Manual and Tools Testing






### 1. Testing User Stories 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| |          |          |          |
|1. Admin User - Set Up Project Workspace  | Installed Django and supporting Libraries, created a new blank Django project and app, set the project to use cloudinary and PostgreSQL and deploy new empty project to Heroku | Pass |          |
|2. Admin User - Complete final project deployment.  | Ensure that final commits are completed, debug changed to false and settings removed under config variables in Heroku. | Pass |          |
|3. Admin User - Be able to set up an account | Create a sign up page where i can enter my username, email and password in order to register and gain access to the blog.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3cbf6afb-0941-43eb-be15-47fda8f33b82) |          |
|4. Site User - Be able to set up an account. | sign up page where it requests the user to enter a username, email and password in order to register and to gain access to the blog.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3cbf6afb-0941-43eb-be15-47fda8f33b82) |    |
|5. Admin User - Be able to successfully login.  | Login page where it requests username and password provided.  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d0a9507c-cb5c-4dfc-a70b-1868574f7ec5) |          |
||          |          |          |
|6. Site User - Be able to successfully login. | Login page where it requests username and password.   | Pass![image](https://github.com/NBJIN/constructionblog/assets/106515976/d0a9507c-cb5c-4dfc-a70b-1868574f7ec5)  |          |
|7. Admin user - to be able to perform full crud | Provision of models, views, templates, forms and urls so that the admin user can have full crud functionality.  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/0f8d31df-0134-4891-b054-21914cd20205)|          |
|8. Site User - Be able to add a post. | forms providied to add a comment and a post for the user. | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/0f8d31df-0134-4891-b054-21914cd20205) |          |
|9. Site User - Be able to update a post.| Form provided to update a post for the user.     | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/0f8d31df-0134-4891-b054-21914cd20205) |          |
|10. Site User - Be able to like a post. | Button provided with each post that the user can click on to like the post.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/53dff80b-7014-4200-8393-87f567dd255f)|          |
|11 Site User - The user can see if an action is successfully completed.  | When the user signs in they can see successfully signed in at the top of the screen.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d4dcaec1-57df-4bd0-83ad-a2f1308b8186)
|          | 
|11 Site User - The user can see if an action is successfully completed.  | When the user signs in they can see successfully signed in at the top of the screen.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d4dcaec1-57df-4bd0-83ad-a2f1308b8186)
| 12 Admin - Complete Project Deployment          | Ensure that final commits are completed, Debug set False and variables set on Heroku  | Pass |          |
| 13 Admin - Manual Testing and Write Up          | Readme completed with all sections enclosed and full testing section.  | Pass |          |
| 14 Admin - Styling of Site   | Style of site is very appealing with the user of color, media and fonts.  | Pass |          |
| 15 Admin - Mobile First Design         | Responsive Across Laptop/Destop/ Mobile.  | Pass |          |
<br>

2. Code Validation - Will have to revert back

3. Accessibility
A lighthouse test report was carried out and the results are as follows 

![image](https://github.com/NBJIN/constructionblog/assets/106515976/aa9401b1-2cf0-4077-93ea-bb8c94a74ddf)



4. Features Testing

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Home Page - Signed In User |          |          |          |
|1. Logo | When the user clicks on the logo on top of each page it will always bring the user back to the home page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5b3425d9-0328-47c3-b965-1658607db66a) |          |
|2. Welcome Message | When the user logs in it will display the welcome message with their username letting the user know that they are logged in. | Pass |          |
|3. Navigational Link - Home | This is displayed at the top of every page when the user is logged in so when the user clicks on the home link it will bring them back to the home page | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)|          |
|4. Navigational Link - Logout  | This is displayed at the top of every page when the user is logged in so they can logout at any time.    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)|    |
|5. Navigational Link - Create Post | This is displayed at the top of every page when the user is logged in so that the user can create a post at any stage while visiting the site  | PassPass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)  |          |
|6. Header - List of Blogs Post  | This header advises the user that they are visiting the list of blog post page.  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/e627afd6-ccb9-43f1-af2d-dc57e85e36ab)  |          |
|7. Read More Link On Card   | When the read more link is clicked it brings the user to the detailed post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|8. Fontawesome Thumbs Up and Like Counter On Card  | When the thumbs up or the number of likes is clicked it will bring the user to the postdetail page where they can click the like button at the bottom of the page to like the post.  The number of likes on the lists of blog posts page provides the total number of likes for that post and clicking on the thumbs up as mentioned will bring the user to the postdetail where they will read the post in full and then if they wish to like the post they can click the button at the bottom of the postdetail page which automattically updates the counter on the list of blog posts page.    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|9. Pagination Next Button   | When the user clicks on the next button under the cards on the list of posts page it will bring them to the next page which has additional posts.     | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|10. Footer Social Media Link - Facebook   | When the user clicks on the fontawesome icon for facebook in the footer they will be brought to the facebook login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |
|11. Footer Social Media Link - Twitter   | When the user clicks on the fontawesome icon for Twitter in the footer they will be brought to the Twitter login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |
|12. Footer Social Media Link - Instagram   | When the user clicks on the fontawesome icon for Instagram in the footer they will be brought to the Instagram login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |

| Goals | Acceptance | Pass | Fail |
|:----------|:----------|:----------|:----------|
| Detailed Post Page Signed In User  |          |          |          |
|1 Detailed Post Page  | Contains all the header and footer items above for a logged in user and all features are working.  | Pass |          |
|2. Detailed Post Header | The header advises the user what page they are currently visiting.  |Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/f12e2f42-1da3-4d03-aa43-27da09d922ff) |          |
|3. Card Update Post | When the user clicks on the update post link at the bottom of the card it will bring the user to the update post page | Pass - Screen shot below |          |
|4. Card Delete Post | When the delete post link is clicked it will bring the user to the delete post page. | Pass - Screen shot below |          |
|5. Card Create Post | When the user clicks on create post it will navigate to the create post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d835e1ff-d553-4899-af99-b279a1f7673a) |          |
|6. Confirmation of Comments | If there is no comments it will advise the user of same and ask if they would like to add a comment  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cbc87569-bc4d-48ff-a1d0-a6ee671261a0) |          | 
|7. Add comment button | If the user clicks on the add comment button they will be brought to the add comment page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/378beb04-0ba6-4525-bdbd-a27f4a75e294) |          | 
|8. Delete comment button | A button had been added for Delete Comment but at present it is not functioning  | Fail ![image](https://github.com/NBJIN/constructionblog/assets/106515976/9e672d9c-d429-40d5-a00b-a94a82c2d360) |          | 
|9. Like button | The like button when clicked will increase the counter which inturn increments the no of likes on the list of posts page.  If the user likes the post by mistake they can press the button again and it will remove the like. | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/ec438296-b63b-4978-bf31-54a2b9a09e58) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Add Comment Page - Signed In User |          |          |          |
|1. Form and Submit Button | On the form the user will fill in the details of their comment on the form and when the submit button is clicked it will bring the user back to the postdetail page where they can see the comment displayed. | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/529f9253-bc4f-4e23-8514-e6be94f34e9a)

![image](https://github.com/NBJIN/constructionblog/assets/106515976/17b0b75d-b38c-4370-bdca-090e7d80b6f7)  |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|1. Sign Out Page |  |   |          | 
|1. Sign Out Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/ca3a7a4c-61fb-4544-bba4-050715a75f89) |          | 
|2. Sign Out Button | When the user clicks on the signout button it will bring them to the home page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/bef13f93-cd22-42e8-829a-9a748b689323) |          | 
|3. Sign Out Message | When the user is brought to the home page once they have clicked on the sign out button a message displays at the top of the homepage letting the user know they have successfully logged out.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/052fc651-1f0f-48ea-9d26-2b78ca87abb1) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Sign In Page |  |   |          | 
|1. Sign In Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/019174f7-13a7-4dad-9e03-4b1edcd6cf93) |          | 
|2. Sign Up Link | If the user does not have an account they can choose the sign up link which will bring them to the sign up page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/6a9728ff-75c1-42e0-9331-b60c93089d7f) |          | 
|3. Sign In Form  | The form allows the user to enter their username and password    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/f241a70f-8cf9-4f58-a938-c2d740b8a598) |          | 
|4. Sign In Error Message  | If the user inputs incorrect information it notifys the user    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3193e4ed-28f4-45d6-ad73-7a0e7462fefb) |          | 
|5. Sign In Button  | The sign in button when clicked will bring the user to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/8394ba66-637f-4420-bdd5-ea7bb66a5b61) |          | 
|5. Sign In Success Message | When the user signs in successfully a message will be displayed to the user in the home page under the logo of successfull sign in    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/04c7d453-d611-4204-99bd-f388f25f08cf) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Sign Up Page |  |   |          | 
|1. Sign Up Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3ba07683-c364-4e5e-aee3-9e4cfa4efea1) |          | 
|2. Sign In Link | If the user already has an account they can choose the sign in link which will bring them to the sign in page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/626c1cff-c03d-4f46-8280-7f5eb4e87d62) |          | 
|3. Sign Up Form  | The form allows the user to enter their username, email and password in order to register as a user.     |![image](https://github.com/NBJIN/constructionblog/assets/106515976/90fb2793-3f22-4a78-8ef8-a344767fae4a)|          | 
|4. Sign Up Error Messages  | If the user fails to input the correct information it notifys the user    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5f4f59c2-bee3-414d-bfc8-4975460f5acf) ![image](https://github.com/NBJIN/constructionblog/assets/106515976/8cb361de-9d12-45b1-bd50-e64e7ad890b2)|          | 
|5. Sign Up Button  | The sign up button when clicked will bring the user to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/565112f6-ed50-48d0-b18b-7134f766399a) |          | 
|5. Sign Up Success Message | When the user signs up successfully a message will be displayed to the user in the home page under the logo of successfull sign up   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/e15291e6-f708-401a-8151-dfd34b107100)|          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Home Page Not Logged In  |  |   |          | 
|1. Navigational Link Sign In | In the nav menu of home page where a user is not logged in they can chooose the sign in link which will bring them to the sign in page  | Pass - Screen Shot Below  |          | 
|2. Navigational Link Sign Up | When the user is not logged in and clicks on the sign up link on the nav bar it will bring them to the sign up page  | Pass - Screen Shot below |          | 
|3. Navigational Link Home  | When the user is not logged in and clicks on the home link it will bring them back to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/af3afe93-cc26-4d80-9c87-1c009f8e95f3)|          | 
|4. Card Message To Sign Up  | When the user is not signed in a message displays on the card to advise the user to sign in to like or comment on a post    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/065aac9c-dcfe-40df-b8ad-b82953502e36)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Detailed Post Page Not Logged In  |  |   |          | 
|1. Detailed Post Message To User Re Comment and Likes  | When the user is not logged in a message is displayed to the user to advise them to log in if they want to like or comment on a post.    | Pass - ![image](https://github.com/NBJIN/constructionblog/assets/106515976/fefafff0-83f6-4d02-8e81-8fe15fc764e5)  |          | 



| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Detailed Post Page Logged In User |  |   |          | 
|1. Detailed Post Header  | The Header advised the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Link To Update Post  | When the user clicks on the update post link they will be brought to the update post page  | Pass - Screen Shot below |          | 
|3. Link To Delete Post  | When the user clicks on the Delete Post they will be brought to the Delete Post Page    | Pass - Screen Shot Below |          | 
|4. Link to Create A Post   | When the user clicks on create post they will be brought to the create post page    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/0d2fb4ea-b409-4ad7-bdd0-44fb65466c2a)|          | 



| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Update Post Page Logged In User |  |   |          | 
|1. Update Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Update Post Form   | The form allows the user to enter details to update the post  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the list of post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5579625a-8cc5-4c32-91c9-a68087e7cd85) |          | 
|4. Error Message displayed back to user   | If the user submits the form without a date an error will display to the user   | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/df9d0ef0-6e32-4204-b420-ce6e93f0192e)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Delete Post Page Logged In User |  |   |          | 
|1. Delete Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Submit Button   | When the user clicks on the submit button the post will be deleted and the user will be brought back to the list of blog post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d3e07c35-2b64-4781-893e-b4eba0b6c798) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Create Post Page Logged In User |  |   |          | 
|1. Create Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Create Post Form   | The form allows the user to enter details to create the post  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the list of post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/a8135ffb-75c5-47e5-9d07-171b743268ca) |          | 
|4. Error Message displayed back to user   | If the user does not enter a date or a name the post will not submit and a message is displayed back to the user    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/9c1d694c-f3d6-4847-a798-785b4b309dc8)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Add Comment Page Logged In User |  |   |          | 
|1. Add Comment Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Create Post Form   | The form allows the user to enter details to add the comment  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the detailed post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/706a5bd2-861f-4ab1-8424-a961ca1c9d3d) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Delete Comment Page Logged In User | This page is currently not displaying  | Fail   |          | 


<br>