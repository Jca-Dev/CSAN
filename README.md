<h1>CSAN E-Commerce Webiste</h1>
<hr>
    <p>CSAN is a fictional E-Commerece website for B2C, the purpose of the site is to sell blinds directly to consumers instead of paying third party so sell them.<br>
    This website is for educational purposes only and the credit card payment functionality is not set up to accept real payments. If testing interactively use card details below.<br>
    Visa = 4242424242424242 Expiration date = 4242 CVN = 424 ZIP = 42424<br>
    <a href="https://csan.herokuapp.com/">Click Here</a> to go to the live website.
</p>
<p>This website follows the mobile first approach and is responsive for mobile devices as well as desktop.</p>
<hr>

<h1>User Experience (UX)</h1>
<h2>Goals</h2>
<ul>
    <li>Users can easily find and purchase blinds online.</li>
    <li>Show a clean, clear, accessible and easily navigable website for the user.</li>
    <li>Users return to show/recommend service to others.</li>
    <li>Frequent users connect via the social media platforms for information and updates.</li>
    <li>Users give positive feedback in the form of reviews and testimonials.</li>
    <li>CRUD functionality for staff and superusers.</li>
</ul>
<hr>
<h1>Database Schema</h1>

![Database Schema](media/screenshots/database.png)
<hr>
<h1>Planning</h1>
<hr>
<h2>Storyboard used <a href="https://github.com/users/Jca-Dev/projects/4">Here</a></h2>

<h2>Desktop</h2>
<p>I used balsamiq wireframes to plan the look and layout of the project. however the final result is not exactly the same as the wireframes.</p>


![Landing Page Preview](media/screenshots/Landing.png)
<hr>

![Product Page Preview](media/screenshots/cassette.png)
<hr>

![Product Page Preview](media/screenshots/horizontal.png)
<hr>

![Product Page Preview](media/screenshots/roller.png)
<hr>

![Product Description Preview](media/screenshots/product-des.png)
<hr>

![Cart Page Preview](media/screenshots/cart.png)
<hr>

![Checkout Page Preview](media/screenshots/checkout.png)
<hr>

![Registration Page Preview](media/screenshots/register.png)
<hr>

![Login Page Preview](media/screenshots/login.png)
<hr>

![Logout Page Preview](media/screenshots/logout.png)
<hr>

![Profile Page Preview](media/screenshots/account.png)
<hr>

<h2>Mobile</h2>
<p>For the mobile design I used figma wireframes because my balsamiq trial had ended.
I also used blocks for forms and informaion to use the layout and reference the block info from the desktop view.</p>

![Nav Bar Mobile Preview](media/screenshots/nav-mob.png)
Above is the nav bar expanded and closed for mobile view.
<hr>

![Landing Page Mobile Preview](media/screenshots/home-mob.png)
<hr>

![Products Mobile Preview](media/screenshots/product-mob.png)
<hr>

![Product-description Mobile Preview](media/screenshots/product-des-mob.png)
<hr>

![Cart Mobile Preview](media/screenshots/cart-mob.png)
<hr>

![Checkout Mobile Preview](media/screenshots/checkout-mob.png)
<hr>

![Checkout Success Mobile Preview](media/screenshots/Checkout-s-mob.png)
<hr>

![Profile Page Mobile Preview](media/screenshots/profile-mob.png)
<hr>

<h1>Design And Features</h1>
<ul>
    <li>Customers can create an account and have their own profile to store their address details for checkout purposes, leave product reviews, testimonials and view their order history.</li>
    <li>Customers can log in with google Oauth for a fast user friendly registration experience.</li>
    <li>Staff accounts have CRUD functionality over products on the web page and can also log into the dJango admin pannel.</li>
    <li>There are links on the main page to relative information on blind cleaning and types of blinds.</li>
    <li>There are links on the product detail page to relative information on information required to order a blind.</li>
</ul>
<h2>Imagery</h2>
<ul>
    <li>The main background image is a bright picture of someone peering through a blind, I thought this would be relative as its a picture of a product sold in the store.</li>
</ul>
<h2>Site colors</h2>
<ul>
    <li>The color sheme is green, white and black. Green and white are the brand colors whereas black is the contrasting color for user interaction buttons to be easily seen.</li>
</ul>
<h2>Security</h2>
<ul>
    <li>Only staff users have access to CRUD functionality of products via links and URLs.</li>
    <li>Variables such as security keys are stored in the enviroment and not in the code.</li>
</ul>
<hr>
<h2>Font styles</h2>
<ul>
    <li>Raleway - is used for headings and the logo because it gives a clear crisp design.</li>
    <li>Open Sans - is used for the text body to align with the heading clear design.</li>
</ul>
<hr>
<h2>Navigation</h2>
<hr>
<p>The user navigates through the site with the buttons on screen and the navbar on the top which also has a search bar. <br>
The user will know where they are on the site as each page has a header displaying the page name. apart from the landing page.</p>

<h2>Future features</h2>
<ul>
    <li>Have duplicate products with different options in the same order.</li>
    <li>Impiment more options such as a selection between motorized and chain controls.</li>
    <li>Sales page one the products list grows.</li>
</ul>
<hr>

<h1>Marketing</h1>
<hr>
<p>I created a facebook marketing page for reaching potential and existing customers on a popular platform. However this has been taken down by facebook as it's not a genuine business. <br>
The footer has links to social media pages, if this was a real business then they would link to the social pages of the business.
<br> Mailchimp has a newsletter popup for new visitors to the site so they can subscribe their email for news letters and marketing campaigns.</p>

![Business Page Preview](media/screenshots/fb_page_1.png)
<hr>

![Business Post Preview](media/screenshots/fb_page_2.png)
<hr>

<h1>Legal Info</h1>
<hr>
<p>
The footer has links to the privacy policy and copyright notice. <br>
There is also a cookie consent popup that also links the privacy policy and controls cookies plus tracking to comply with GDPR.
</p>

![Cookies Popup Preview](media/screenshots/cookies.png)
<hr>

<h1>Technologies Used</h1>
<ul>
    <li>Python 3 - coding language.</li>
    <li>Django - coding framework.</li>
    <li>HTML & CSS - markup language.</li>
    <li>Bootstrap 5 - CSS framework and toolkit.</li>
    <li>JavaScript - coding language.</li>
    <li>jQuery - coding framework.</li>
    <li>Stripe - stripe payment and webhooks</li>
    <li>Git - version control by utilizing the Gitpod terminal to add, commit and Push to GitHub.</li>
    <li>Git Hub - stores the project code and hosts the website.</li>
    <li>Visual Code Studio - system used to write code via Git.</li>
    <li>Paint 3D - to create the logo and edit screenshots for the README.md</li>
    <li>Heroku - for hosting the python code and downloading requirements.</li>
    <li>Pep8 - testing code.</li>
    <li>Chrome Dev Tools - to action, review and test changes without having to commit and push to the website each time.</li>
    <li>Lighthouse - testing code.</li>
    <li>W3C Validation - testing code.</li>
    <li>AWS - amazon hosting service S3 hosts the required static files.</li>
    <li>Database - elephantSQL.</li>
    <li>Mailchimp - hosting user email address data for newsletters.</li>
    <li>Pytest - Automated testing.</li>
    <li>Coverage - Automated testing.</li>
    <li>Factory-boy - Automated testing.</li>
    <li>Balsamiq - wireframes for design.</li>
    <li>Figma - Wireframes for design.</li>
</ul>
<hr>
<h1>Deployment</h1>
<h2>Requirements:</h2>
<ul>   
    <li>AWS_ACCESS_KEY_ID - links AWS to heroku.</li>
    <li>AWS_SECRET_ACCESS_KEY - links AWS to heroku.</li>
    <li>DATABASE_URL - links database to heroku.</li>
    <li>SECRET_KEY - authorises heroku to use the app.</li>
    <li>USE_AWS - tells heroku to use AWS to serve static files.</li>
    <li>Procfile - declare the proccess type. e.g. web: gunicorn 'appname'.wsgi:application</li>
    <li>
        Requirments.txt - this file lists all the dependencies for the project. this project requires: 
        <br>asgiref==3.5.2
        <br>boto3==1.26.48
        <br>botocore==1.29.48
        <br>coverage==7.0.5
        <br>dj-database-url==0.5.0
        <br>Django==3.2
        <br>django-allauth==0.41.0
        <br>django-countries==7.2.1
        <br>django-crispy-forms==1.14.0
        <br>django-storages==1.13.2
        <br>exceptiongroup==1.1.0
        <br>factory-boy==3.2.1
        <br>Faker==16.5.0
        <br>gunicorn==20.1.0
        <br>inflection==0.5.1
        <br>iniconfig==2.0.0
        <br>jmespath==1.0.1
        <br>oauthlib==3.2.2
        <br>Pillow==9.3.0
        <br>pluggy==1.0.0
        <br>psycopg2==2.9.5
        <br>pytest==7.2.1
        <br>pytest-django==4.5.2
        <br>pytest-factoryboy==2.5.1
        <br>python3-openid==3.2.0
        <br>pytz==2022.6
        <br>requests-oauthlib==1.3.1
        <br>s3transfer==0.6.0
        <br>sqlparse==0.4.3
        <br>stripe==5.0.0
    </li>
</ul>
<h2>AWS</h2>
<ol>
    <li>Create an account at aws.amazon.com</li>
    <li>Open the S3 application and create an S3 bucket named csan-shop</li>
    <li>Select your nearest AWS Region.</li>
    <li>Uncheck the Block All Public access setting & acknowledge that the bucket will be public. It needs to be public in order to allow public access to static files.</li>
    <li>go to properties then to static website hosting and click edit.</li>
    <li>In properties turn on static website hosting and set the index.html and the error.html values, however for this app they aren't used.</li>
    <li>
    In the permissions section edit the CORS configuration and set it to the configuration below this list.</li>
    <li>Edit the bucket policy then generate and set the below configuration:</li>
    <li>Then go to the Access Control List and set the List objects permission for everyone under the Public Access section.</li>
    <li>Open the IAM application to control access to the bucket and set up a user group called</li>
    <li>Click on Policies, and Create Policy.</li>
    <li>Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess.</li>
    <li>Set the settings in the JSON tab below the list.</li>
    <li>Review policy, give it a name & description and then create policy.</li>
    <li>To attach the policy to the group go to Groups then permissions and under add permissions select attach policy.</li>
    <li>To create a user for the group click Add User and create one, ***make sure to download the CSV file which contains the user's access credentials.***</li>
    <li>Finally add the user to the group created.</li>
    !important the following AWS code in Settings.py. An environment variable called USE_AWS must be set to use these settings otherwise it will use local storage.
</ol>
CORS config

```
[
    {
    "AllowedHeaders": [
    "Authorization"
    ],
    "AllowedMethods": [
    "GET"
    ],
    "AllowedOrigins": [
    "*"
    ],
    "ExposeHeaders": []
    }
]

```
<br>

```
{
    "Version": "2012-10-17",
    "Id": "your generated id",
    "Statement": [
        {
            "Sid": "your generated id",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::csan-shop/*"
        }
    ]
}
```
<br>
<h2>Stripe</h2>
<ol>
    <li>Register for an account at stripe.com.</li>
    <li>Log in and go to the developers section.</li>
    <li>Then API keys.</li>
    <li>Copy publishable and secret keys.</li>
    <li>In your local environment(env.py):<br>
    os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')<br>
    os.environ.setdefault ('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</li> 
    <li>In heroku config vars, add STRIPE_PUBLIC_KEY with the publishable key you copied from stripe and STRIPE_SECRET_KEY with the secret key value from stripe.</li>
    <li>Back in the developers section of your stripe account go to webhooks.</li>
    <li>Create a webhook with the url of your website /checkout/wh/ e.g. https://csan.herokuapp.com/checkout/wh/</li>
    <li>Select the payment_intent.payment_failed and payment_intent.succeeded as events to send.</li>
    <li>Copy the key created for this webhook.</li>
    <li>In your local environment(env.py):<br>
    os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</li>
    <li>In heroku config vars, add STRIPE_WH_SECRET with the secret value.</li>
    <li>Test the webhook and note the success/fail attempts for troubleshooting, see events and logs for further testing.</li>
</ol>
<br>
<h2>Emails</h2>
Specifically for gmail.
<ol>
    <li>Create an email account at https://support.google.com/mail/answer/56256?hl=en. Login and go to account settings.</li>
    <li>Go to accounts and import and under Change account settings you will find other account settings.</li>
    <li>In security under signing into Google, turn on 2-step verification and follow the steps to enable.</li>
    <li>Once verified click on app passwords select other as the app and give the password a name for example Django-app.</li>
    <li>Finish by clicking create and then a 16 digit password will be generated copy this 16 digit password.</li>
    <li>In the env.py file:<br>
    os.environ["EMAIL_HOST_USER"] = "gmail email address".<br>
    os.environ["EMAIL_HOST_PASS"] = "the 16 digit password".</li>
    <li>You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in heroku as you did with stripe.</li>
</ol>
<br>
<h2>Database</h2>
<h3>Creation</h3>
<ol>
    <li>Log into to ElephantSQL.com to access your dashboard.</li>
    <li>Create New Instance.</li>
    <li>Set up your plan.</li>
    <li>Select Region e.g. "EU-West-1 (Ireland)".</li>
    <li>Review.</li>
    <li>Create instance.</li>
    <li>Return to the ElephantSQL dashboard and click on the database instance name for this project.</li>
</ol>
<br>
<h3>Migration</h3>
<ol>
    <li>Navigate to the Postgres Migration Tool repo on github.</li>
    <li>Click the Gitpod button to open a new workspace.</li>
    <li>Run: python3 reel2reel.py in the terminal.</li>
    <li>In a new browser tab go to your app in Heroku and go to Settings.</li>
    <li>Reveal Config Vars.</li>
    <li>In DATABASE_URL Config Var copy the value attained from step 3, It will start with postgres://</li>
    <li>Return to Gitpod and paste in the value attained from step 3 and hit enter.</li>
    <li>Get your ElephantSQL database URL from 'database creation' it will start with postgres://</li>
    <li>Return to Gitpod and paste in the URL where prompted.</li>
    <li>The data will now be downloaded from Heroku and uploaded to your ElephantSQL database.</li>
    <li>To test that your database has been moved successfully, return to ElephantSQL and select BROWSER.</li>
    <li>Open Table queries. If there are options in the dropdown, your tables have been created.</li>
    <li>Select a table name you recognise, and then click Execute.</li>
    <li>You should see your data displayed relating to the table you selected.</li>
</ol>

<h2>Heroku</h2>
After following the previous steps the project was deployed to Heroku via GitHub by:
<ol>
    <li>Log Into Heroku, create a new project, go to the settings page and add the required variables from 'requirements' above.</li>
    <li>Link the database (ElephantSQL) by pasting the database url in the DATABASE_URL Config Var.</li>
    <li>Link Static file host (AWS)</li>
    <li>Link Stripe (Payments)</li>
    <li>Go to deploy, select deployment method as GitHub and typing in the GitHub repository name into the required field and selecting this repository name.</li>
    <li>Finally select deploy branch to manually deploy or select automatic deployment which allows Heroku to rebuild the project after each push to GitHub.</li>
</ol>
!Important make sure to set Debug in the settings.py file to False. <br>
The page is now published and the link is in the settings section under Domains.


<br>

<h2>Making a Local Clone</h2>
<ol>
    <li>Log in to GitHub and locate the [GitHub Repository](https://github.com/)</li>
    <li>Under the repository name, click "Clone or download".</li>
    <li>To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.</li>
    <li>Open Git Bash</li>
    <li>Change the current working directory to the location where you want the cloned directory to be made.</li>
    <li>Type `git clone`, and then paste the URL you copied in Step 3.</li>
    <li>Press Enter. Your local clone will be created.</li>
    <li>Create a new Heroku app and follow the steps in Heroku deployment above or to use locally create an env.py file(do not commit this file to source control) in the root folder in your project with the following code:</li>
</ol>

```
    import os
    os.environ["SECRET_KEY"]= 'TO BE ADDED BY USER'
    os.environ["STRIPE_PUBLIC_KEY"]= 'TO BE ADDED BY USER'
    os.environ["STRIPE_SECRET_KEY"]= 'TO BE ADDED BY USER'
    os.environ["STRIPE_WH_SECRET"]= 'TO BE ADDED BY USER'
    os.environ["AWS_ACCESS_KEY_ID"]= 'TO BE ADDED BY USER'
    os.environ["AWS_SECRET_ACCESS_KEY"]= 'TO BE ADDED BY USER'
    os.environ["EMAIL_HOST_USER"]= 'TO BE ADDED BY USER'
    os.environ["EMAIL_HOST_PASS"]= 'TO BE ADDED BY USER'
    os.environ["USE_AWS"]= 'TO BE ADDED BY USER'
    os.environ["DATABASE_URL"]= 'TO BE ADDED BY USER'
    os.environ["DEVELOPMENT"] ='True'
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for retrieve pictures and more detailed explanations of the above process.
    
<hr>
<h1>Testing</h1>
<h2>User Stories</h2>
<ul>
    <li>
        <strong>Add to cart</strong><br>- test - add options for the product and click add to cart.<br><br>- expected result - a success message should be generated with the item and quantity, the product and option input should show on the cart page.<br><br>- result - success message was generated with the item and quantity, the product and option input showed on the cart page.
    </li>
    <br>
    <li>
        <strong>Creating an order</strong><br>
        - test - 
        <ol>
            <li>add options for the product and click add to cart.</li>
            <li>once the item is in the cart go to the checkout page.</li>
            <li>fill out the checkout form and payment options (card number & zip).</li>
        </ol><br>- expected result - redirected to the checkout success page with a success message "Order successfully processed! \ Your order number is {order_number}. A confirmation \ email will be sent to {order.email}." 
        with the order number, order details, product, quantity, options, and price should be displayed and finally an order line item should be displayed on the user profile page.<br><br>- result - redirected to the checkout success page with a success message "Order successfully processed! \ Your order number is {order_number}. A confirmation \ email will be sent to {order.email}." with the order number, order details, product, quantity, options, and price are displayed and finally an order line item was displayed on the user profile page.
    </li>
        <br>
    <li>
        <strong>Search function</strong><br>
        - test - search for one of the categories e.g. cassette.
        <br>- expected result - only products from the cassette category will desplay.<br><br>- result -only products from the cassette category were desplayed.
    </li>
    <br>
    <li>
        <strong>receiving email after Order creation</strong><br>- test - follow 'creating and order' test.<br><br>- expected result - an email should be generated and sent to the profile email address.<br><br>- result - an email was be generated and sent to the profile email address.
    </li>
    <br>
    <li>
        <strong>Leaving a review</strong><br>- test - write a review for a product on the product detail page and submit.<br><br>- expected result - the reiew will be submitted and displayed below the form.<br><br>- result -the reiew was submitted and displayed below the form.
    </li>
    <br>
    <li>
        <strong>Creating a testimonial</strong><br>- test - after placing an order, go to the profile page and fill out the testimonial form.<br><br>- expected result - a success message should display "You have successfully given your testimonial for our service. Thank you!" and the testimonial will be added to the landing page."<br><br>- result - success message was displayed "You have successfully given your testimonial for our service. Thank you!" and the testimonial was added to the landing page.
    </li>
    <br>
    <li>
        <strong>Account creation</strong><br>- test - go to the register page and fill out the form, open the email received and click the link to and on the page loaded in your browser click confirm than login.<br><br>- expected result - the account is created with access to the profile page.<br><br>- result - the account was created with access to the profile page.
    </li>
</ul>
<hr>
<h2>Manual test</h2>
<h3>Form testing</h3>
<ul>
    <li>
        <strong>Input fields</strong><br>- test - input incorrect data such as a char in an int field or empty required field.<br><br>- expected result - the form validation will throw an error and display "There was an error with your form. Please double check your information."<br><br>- result - error displayed "There was an error with your form. Please double check your information."
    </li>
    <br>
    <li>
        <strong>Duplicate form submission for single submision per user</strong><br>- test - submit a second form after one is bound to the user.<br><br>- expected result - an error will display saying "You have already given your testimonial for our service. Thank you!".<br><br>- result - error will display saying "You have already given your testimonial for our service. Thank you!".
    </li>
</ul>
<h3>Login & Registration Testing</h3>
<ul>
    <li>
        <strong>Duplicate Account</strong><br>- test - try registering with a username already in use.<br><br>- expected result - user wont be able to register and the page will refresh with an error message stating the username is taken.<br><br>- result - user cant register and the page refreshed however no error message is displayed.
    </li>
    <br>
    <li>
        <strong>Invalid Credentials</strong><br>- test - try logging in with a invalid credentials e.g. wrong password or non existant username.<br><br>- expected result - user wont be able to login and the page will refresh with an error message stating the password is wrong or the username doesn't exist.<br><br>- result - user cant login and the page refreshed however no error message is displayed.
    </li>
</ul>
<h3>Security Testing</h3>
<ul>
    <li>
        <strong>CRUD for products</strong><br>- test - open product page with anonymous (no logged in) and non staff user account and check to see if they can see the links.<br><br>- expected result - non staff users including anonymous cant see the edit or delete links when clicking on a product page.<br><br>- result - non staff users including anonymous cant see the edit or delete links when clicking on a product page.
    </li>
    <br>
    <li>
        <strong>CRUD for products via url</strong><br>- test - type in the url to edit or delete a product with anonymous (no logged in) and non staff user account. e.g. https://csan.herokuapp.com/products/delete/4/<br><br>- expected result - non staff users including anonymous get redirected to the login page.<br><br>- result - non staff users including anonymous get redirected to the login page.
    </li>
    <br>
    <li>
        <strong>Login to admin site</strong><br>- test - try to log into the admin site as a non staff user.<br><br>- expected result - login page refreshed with an error displaying "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."<br><br>- result - login page refreshed with an error displaying "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."
    </li>
    <br>
    <li>
        <strong>Testimonial</strong><br>- test - try to write a testimonial and submit in the profile page without having an order.<br><br>- expected result - the form will not show and text "You must have made a purchase to submit a Testimonial." is displayed instead.<br><br>- result - the form did not show and text "You must have made a purchase to submit a Testimonial." is displayed instead.
    </li>
</ul>
<h2>Browsers</h2>
<ul>
    <li>Google Chrome</li>
    <li>Microsoft Edge</li>
    <li>Mozilla Firefox</li>
</ul>
<h2>Devices</h2>
<ul>
    <li>Galaxy S8</li>
    <li>Galazy S21 Ultra</li>
    <li>Iphone SE</li>
    <li>Iphone 4</li>
    <li>Iphone 12 Pro</li>
    <li>Ipad Air</li>
    <li>Surface Pro 7</li>
    <li>Laptop</li>
    <li>Nest Hub max</li>
</ul>

<h2>Software Tests</h2>
<ul>
    <li><a href="https://search.google.com/test/mobile-friendly" target="_blank" rel="noopener">Google mobile friendly test Service</a></li>

![Google Mobile](media/screenshots/responsive.png)
    <li><a href="https://validator.w3.org/" target="_blank" rel="noopener">W3C Markup Validation Service</a></li>

![W3C HTML](media/screenshots/w3c-html.png)
    <li><a href="https://jigsaw.w3.org/css-validator/" target="_blank" rel="noopener">W3C CSS Validation Service</a></li>

![W3C CSS](media/screenshots/wc3-css.png)
    <li><a href="https://developers.google.com/web/tools/lighthouse" target="_blank" rel="noopener">Google Chrome Lighthouse</a></li>

![Lighthouse Test](media/screenshots/lighthouse.png)
    <li><a href="https://jshint.com/" target="_blank" rel="noopener">JSHint Javascript Validation Service tested javascript including third party.</a></li>
</ul>
<h2>Unit Tests</h2>
I used Coverage to Identify tests needed.

![Coverage view](media/screenshots/coverage_start.png)
<p>Automated testing showed me that I forgot to add webhook files and email templates and I changed my form validation on the phone number form field to be more user friendly by changing it to a charfield to take advantage of the max_value validator then I used RegexValidator to make sure the user inputs numbers.</p>

<h2>Bugs & Fixes</h2>
<ul>
   <li>The screen width on mobiles wasn't showing 100% so the nav bar and content was off the screen and you had to scroll across to see it. - fix - with setting up 100vw in body and html inside base.css.</li>
   <li>The monkeychimp modal for mobile was covered by the nav bar so users couldnt see it properly or exit it easily. - fix - reduced z-index of nav bar to 50 so it was below monkeychimp modal z-index.</li>
   <li>The testimonials were displaying too close together. - fix - add margin around each testimonial to keep them seperate.</li>
   <li>When an order is in the wishlist section of the profile page the options and picture are crushed and dificult to see. - fix - simplified the wishlist display by removing the form and description replacing add to cart with go to product.</li>
</ul>

<h2>Known Bugs</h2>
<ul>
    <li>The Error: Uncaught TypeError: Cannot read properties of null (reading 'appendChild') this is present in a third party script from mailchimp that I dont have access to.</li>
    <li>The checkout form validation doesn't show up on the fields apart from the stripe payment field. but it does validate.</li>
    <li>A user cannot add a duplicate product with different options to the cart list as its a dictionary.</li>
    <li>Allauth form validation doesn't display all errors required.</li>
</ul>
<hr>
<h2>Sources/Credits</h2>
<hr>
<ul>
    <li>My Mentor for her feedback</li>
    <li>Gathered information and troubleshooting from <a href="https://stackoverflow.com/" target="_blank" rel="noopener">Stackoverflow</li>
    <li>Code Institute's Boutique_ado walkthrough provided a very clear idea on how to create an E-commerce Website in Django.<a href="https://github.com/Jca-Dev/Love_sandwiches" target="_blank" rel="noopener">GitHub Link</a></li>
    <li>background image from <a href="https://www.pexels.com/" target="_blank" rel="noopener">Pexels</a></li>
    <li>Icons from <a href="https://fontawesome.com/search?o=r&m=free" target="_blank" rel="noopener">fontawesome</a></li>