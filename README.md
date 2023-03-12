<h3>Migrate Wisely</h3>

<a href="https://migratewisely.com/" target="_blank">See the ongoing site</a>

This is a project where the migration opportunities are categorized. 
I additionally created a forum. People can register and handle account settings such as editting profile pictures, changing passwords and so on. 

In this project, I used django framework in the backend. No frameworks are used in the frontend. Only HTML, CSS, JS and their libraries.

Some cool libraries I used are: 

+ django-htmx==1.12.1
- In the homepage, I created a search bar where the blogs are filtered instantly from the database.
- In the hot topics page, I created infinite scroll by using htmx.
- In the blog detail pages, I created mark button by using htmx that the specific blog can be specified as marked without refreshing the page.

+ django-encrypted-id==0.3.2
- I created a unique encrypted code for each user at the time when the profile is created. Honestly, I could not find some place to use it properly because the data user will keep are not so important. However, I used it in the url of the profile of the user.
- For changing email, I used a random encrypted code and sent it to the mailbox of the user and set it's expiration date to +24 h later so that if the user enters the code which is sent to mail after 24 hours it is sent, the function will not work.
