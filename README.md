[insert logo image here]

# Racehub


## [Deployed Project on Heroku](https://race-hub.herokuapp.com/)

[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

Racehub is race entry and results management system for amateur athletes and event organisers. It is written in python using the django framework and is the final project in the Code Institute Diploma in Software Development (Full Stack Web Development.)


## [Developer Aims](#developer-aims)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

* Use the django framework for writing a fully functioning web application
* Provide sufficient user interaction features to demonstrate that this project could be further developed into a viable commercial application
* Provide sufficient documentation in order that the project can be maintained and further developed in the future

## [UX](#ux)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [User Stories and Corresponding Features](#user-stories-and-features)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

| User Story ID | As a / an | I want to be able to... | ... so that I can | Existing Features | Suggested future features |
|---|---|---|---|---|---|
|  Viewing and Navigation  |
| 1a | Visitor | View a list of events | select one to enter | List view with search and filters, , Filter by distance, discipline, Sort by distance, date, price | Add filters to map view  |
| 1b |  | View race results | find performances | Find results by name, sort by date or name | Add further filtering controls |
| 1c |  | Quickly identify an event in my area and discipline | enter an event that suits my preferences | Map view | Add filters to map view |
| 1d |  | Add a whole series or championship to my cart at once.  |  |  | 
| 1e |  | Easily enter my friends who are / are not registered on this site.  | 'Family and Friends' can be added and entered for events. Registered users can be added as 'Racehub Friends' | Send a friends request to other site users, search athlete feature. | 
| Registration and User Accounts  | 
| 2a | Registered Athlete | Easily register for an account | Account creation automatically creates athlete profile | Popup 'tour' guides user through the process. | 
| 2b |  | Log in and out simply with social media account specifically facebook |  |  | 
| 2c |  | Recover my password | Authentication added |  | 
| 2e |  | Receive email confirmation after registering | Email confirmation added |  | 
| 2f |  | View a personalised user profile |  |  | 
| 2g |  | Cancel entry |  transfer my entry to another user |  swap my entry to another event from same organiser." | Entry can be transferred to other users by changing ID | Verification that all details especially the ID have genuinely been changed when a registration is transferred. Only allow transfer to FUTURE, live events. | 
|  |  | Sorting and Searching |  |  | 
| 3a |  | Sort the list of events | Easily identify events by date, discipline, distance |  | 
| 3b |  | Filter to find only events in a specific category | date, disciple |  | 
| 3c |  | Sort multiple properties of events simultaneously | Eg find a 10k road event or set of results in Yorkshire | After filtering by discipline, sorting features can can used find by distance | Add colours and icons to make different categories of events stand out |
| 3d |  | Search for results. | Search for results by athlete name, club or age category |  | 
| 3e |  | Easily enter an event |  |  | 
| 3f |  | Easily edit my own Athlete details | Athlete profile can be edited |  | 
| 3g |  | Enter multiple athletes for one event at the same time |  and pay for their entry all at once. | Self, friends or family can all be added to the same basket | In My Racehub, check if friend exists before adding the same Racehub Friend a second time. | 
| 3h |  |  |  |  | 
| 3i |  |  |  |  | 
| 3j |  | Add results for virtual races I am registered for | Result can be submitted as photo or hyperlink |  | 
|Admin and management  | 
| 4a | Club or organisation official | Manage teams | my club has it's own private page |  |  |
| 4b |  | Make my club events private  | they are not on the main listing pages |  |  | 
| 4c |  |  |  |  | 
| 4d | Event Organiser | Add events |  | Add a lat and long finder tool | 
| 4e |  | Add results by bulk upload | Add single results | Change add result form to pre populate with specific event id, Add bulk upload by csv. Add a 'Quick Add' feature to simply enter results by finding Bib number OR searching my athlete name and then entering the time only. The linked athlete field should be a select field or search field containing athlete names.| 
| 4f |  | Download results in bulk | Results can be exported to email account from Organiser Profile | Select one specific result set for download | 
| 4g |  | Add individual results 'live' at the finish line. | Single results can be added | Quick input form so that results are easier to add | 
| 4h | Manage England Athletics membership | Verify those eligible for discounts | EA membership can be made verified in the database, status is displayed in front end | Verify / Unverify EA memership in front end. Connect to EA api to verify memership status. Apply a discount in the checkout if EA membership is verified. | 



## [UI Structure](#ui-structure)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

The following UI layouts were considered essential for the implementation of user stories:

- Navigation menu
- Home Page
- User login form
- User registration form
- Log out button
- Event listing page
- Result listing page
- Cart page
- Checkout page
- User Dashboard page
- Organiser Dashboard page
- Add and manage Event page(s)
- Add and manage results page(s)

Bootstrap components used:
- [Grid](https://getbootstrap.com/docs/4.0/layout/grid/)
- [List Group](https://getbootstrap.com/docs/4.0/components/list-group/)
- [Dropdowns](https://getbootstrap.com/docs/4.0/components/dropdowns/)

Forms used on the site:
- Add Event
- Add Results
- Select which athlete to enter (Event entry process)
- Edit Athlete Profile - My Racehub profile page
- Edit User Profile - My Racehub profile page
- Racehub Friends form - to add another site user to your 'Racehub friends'
- Family and Friends form - to add a non racehub user to your My Racehub and allow facility to enter them in an event.
- Submit Virtual Result
- Transfer Entry form - to transfer event entry to another athlete.
- Manage Virtual Results (Organiser)

Javascript:
- Map View. Made use of Leaflet.js to display events as pins on a map.
- Search and filter functions (made reference to Boutique Ado project)


## [Visual Layout](#visual-layout)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

The visual layout was inspired by the Code Institute Boutique Ado project and also various reference sites.
- [Sports Shoes](https://www.sportsshoes.com/)
- [Yonda](https://yondasports.com/)
- [Findrace](https://findarace.com/)
- [Event Entry](https://findarace.com/)
- [Trail Events](https://findarace.com/)
- [SI Entries](https://www.sientries.co.uk/)
- [Entry Central](https://www.entrycentral.com/)
- [UKresults](https://findarace.com/)

Bootstrap was used to achieve a responsive grid layout and add UI components.
Logos were designed by the developer.

## [Technologies Used](#technologies-used)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

#### Languages:
* HTML for page structure and contents
* CSS for styling the content
* Javascript for DOM manipulation and stripe payment processing
* Python3 for application logic

#### Framework:
* Django (v3.1.1) for application backend, development database provision (SQLite3), routing and template manipulation;

#### Libraries:
* [Bootstrap](https://getbootstrap.com/) used for grid layout and front end ui components.
* [jQuery](https://jquery.com/) to easier DOM manipulation
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/) for icons
* [Leaflet](https://leafletjs.com/) for displaying markers on a map

#### Development:
* [Gitpod](https://www.gitpod.io/) Used for ide
* [Github](https://github.com/) Used for version control

#### Code Validation Tools:
* [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
* [JSHint](https://jshint.com/) was used to validate JavaScript code;
* [PEP8 online](http://pep8online.com/) to validate Python code;

#### Deployment:
* [Amazon Web Services](https://aws.amazon.com/free/) S3 used for image Hosting
* [Heroku](https://dashboard.heroku.com/apps) used for application online deployment and production database provision (PostgresSQL)

#### External (third party) services:
* [Gmail](https://www.google.com/intl/en_uk/gmail/about/) for sending email
* [Stripe](https://dashboard.stripe.com/) for credit card payment processing

#### Utilities:
* [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables)


## [Information Architecture](#information-architecture)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)


## Data Models

#### The User Model
The standard Django user model, `django.contrib.auth.models` was used for this project. NB This is not to be confused with the User and Athlete models used in the Profile app.

### Cart app

**Order Model:**
| Key in db | Field Type | Validation |
|---|---|---|
| order_number | CharField | max_length=32, null=False, editable=False | 
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True blank=True, related_name='orders' | 
| full_name | CharField | max_length=50, null=False, blank=False | 
| email | EmailField | max_length=254, null=False, blank=False | 
| phone_number | CharField | max_length=20, null=False, blank=False | 
| country = CountryField | blank_label='Country *', null=False, blank=False | 
| postcode | CharField | max_length=20, null=True, blank=True | 
| town_or_city | CharField | max_length=40, null=False, blank=False | 
| street_address1 | CharField | max_length=80, null=False, blank=False | 
| street_address2 | CharField | max_length=80, null=True, blank=True | 
| county | CharField | max_length=80, null=True, blank=True | 
| date | DateTimeField | auto_now_add=True | 
| delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 | 
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 | 
| grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 | 
| original_cart | TextField | null=False, blank=False, default='' | 
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' | 

**Order Line model:**
| Key in db | Field Type | Validation |
|---|---|---|
| order  | ForeignKey | Order, null=False, blank=False, | on_delete=models.CASCADE, related_name='lineitems' | 
| event  | ForeignKey | EventInstance, null=False, blank=False, |on_delete=models.CASCADE | 
| which_athlete  | CharField | max_length=2, null=True, blank=True | 
| quantity  | IntegerField | null=False, blank=False, default=0 | 
| lineitem_total  | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | 


### Checkout app

This app does not have any models.

### Clubs app

**Club model**

| Key in db | Field Type | Validation |
|---|---|---|

### Events app

**Discipline model**

Contains type of race eg Road, Fell, Trail, Cross Country. Behaves like 'categories' in the data structure.

| Key in db | Field Type | Validation |
|---|---|---|
| name  | CharField | max_length=254 | 
| friendly_name  | CharField | max_length=254, null=True, blank=True | 

**Distances model**

Contains type of race eg 10k, Half Marathonn Marathon. Behaves like 'categories' in the data structure.

| Key in db | Field Type | Validation |
|---|---|---|
| name  | CharField | max_length=254 | 
| friendly_name  | CharField | max_length=254, null=True, blank=True | 

**Format model**

Contains type of race eg Mass Start, Virtual. Behaves like 'categories' in the data structure.

| Key in db | Field Type | Validation |
|---|---|---|
| name  | CharField | max_length=254 | 
| friendly_name  | CharField | max_length=254, null=True, blank=True | 

**Organiser model**

| Key in db | Field Type | Validation |
|---|---|---|
| name  | CharField | max_length=254 | 
| friendly_name  | CharField | max_length=254, null=True, blank=True | 

**Event Instance model**

An event instance would be created each time an event happens. Eg. The CI Marathon 2019, The CI Marathon 2020. Event Instances are then added to the checkout process. Results are also linked to a specific Event Instance.

| Key in db | Field Type | Validation |
|---|---|---|
| name  | CharField | max_length=254 | 
| friendlyname  | CharField | max_length=254, null=True, blank=True | 
| eventdate  | DateField | null=True, blank=True | 
| price  | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True | 
| race_limit  | DecimalField | max_digits=4, decimal_places=0, null=True, blank=True | 
| sku  | CharField | max_length=254, null=True, blank=True | 
| isvirtual  | BooleanField | null=True, blank=True, default=False | 

**Event model**

Sometimes referred to in the user dashboard front end as the 'parent event.' This contains overall information about the event over time.

| Key in db | Field Type | Validation |
|---|---|---|
| discipline  | ForeignKey | 'Discipline', null=True, blank=True, on_delete=models.SET_NULL | 
| distance  | ForeignKey | 'Distance', null=True, blank=True, on_delete=models.SET_NULL | 
| exactdistancekm  | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True | 
| event_format  | ForeignKey | 'Format', null=True, blank=True, on_delete=models.SET_NULL | 
| organiser  | ForeignKey | 'Organiser', null=True, blank=True, on_delete=models.SET_NULL | 
| sku  | CharField | max_length=254, null=True, blank=True | 
| name  | CharField | max_length=254 | 
| event_instance  | OneToOneField | EventInstance, on_delete=models.CASCADE, null=True, blank=True | 
| entrycutoff  | DateField | null=True, blank=True | 
| keyinfo  | TextField |  | 
| description  | TextField |  | 
| location_post_code  | TextField | max_length=8 | 
| latitude  | DecimalField | max_digits=8, decimal_places=6, null=True, blank=True | 
| longitude  | DecimalField | max_digits=8, decimal_places=6, null=True, blank=True | 
| price  | DecimalField | max_digits=6, decimal_places=2 | 
| rating  | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True | 
| image_url  | URLField | max_length=1024, null=True, blank=True | 
| image  | ImageField | null=True, blank=True |

### Home app

This app contains no models.

### Profiles app

**User Profile model**

Used to store default delivery information. This is passed to Stripe.

| Key in db | Field Type | Validation |
|---|---|---|
| user  | OneToOneField | User, on_delete=models.CASCADE | 
| default_phone_number  | CharField | max_length=20, null=True, blank=True | 
| default_street_address1  | CharField | max_length=80, null=True, blank=True | 
| default_street_address2  | CharField | max_length=80, null=True, blank=True | 
| default_town_or_city  | CharField | max_length=40, null=True, blank=True | 
| default_county  | CharField | max_length=80, null=True, blank=True | 
| default_postcode  | CharField | max_length=20, null=True, blank=True | 
| default_country = CountryField | blank_label='Country', null=True, blank=True | 

**Athlete Profile model**

Used to store Athlete information. This is not passed to Stripe.

| Key in db | Field Type | Validation |
|---|---|---|
| athletefirstname  | CharField | max_length=60, null=True, blank=True | 
| athletesurname  | CharField | max_length=60, null=True, blank=True | 
| eanumber  | CharField | max_length=80, null=True, blank=True | 
| eaverified  | BooleanField | default=True | 
| club  | ForeignKey | Club, null=True, blank=True, on_delete=models.SET_NULL | 
| dateofbirth   | DateField |  null=True, blank=True  | 
| emergencycontactname  | CharField | max_length=60, null=True, blank=True | 
| emergencycontactphone  | CharField | max_length=20, null=True, blank=True | 
| gender  | CharField | max_length=2, choices=gender_choices, null=True, blank=True | 
| tshirtsize  | CharField | max_length=5, choices=tshirtsize_choices,  default=Medium | 
| user  | OneToOneField | User, on_delete=models.CASCADE | 
| userprofile  | OneToOneField | UserProfile, on_delete=models.CASCADE, null=True, blank=True | 

**Racehub Friends model**

Used to link one Athlete Profile to another Athlete profile.

| Key in db | Field Type | Validation |
|---|---|---|
| rfuserprofile  | ForeignKey | User, null=True, blank=True, on_delete=models.SET_NULL | 
| rfathleteprofile  | ForeignKey | AthleteProfile, null=True, blank=True, on_delete=models.SET_NULL | 
| myfriendsracehubid  | DecimalField | max_digits=10, decimal_places=0, null=True, blank=True | 

**Non Racehub Friends model**

Used to event athletes who are not registered on Racehub.

| Key in db | Field Type | Validation |
|---|---|---|
| parentprofile  | ForeignKey | AthleteProfile, on_delete=models.CASCADE | 
| athletefirstname  | CharField | max_length=60, null=True, blank=True | 
| athletesurname  | CharField | max_length=60, null=True, blank=True | 
| eanumber  | CharField | max_length=80, null=True, blank=True | 
| eaverified  | BooleanField | default=True | 
| club  | ForeignKey | Club, null=True, blank=True, on_delete=models.SET_NULL | 
| dateofbirth   | DateField |  null=True, blank=True  | 
| emergencycontactname  | CharField | max_length=60, null=True, blank=True | 
| emergencycontactphone  | CharField | max_length=20, null=True, blank=True | 
gender  | CharField | max_length=2, choices=gender_choices, null=True, blank=True | 
| tshirtsize | CharField | max_length=5, choices=tshirtsize_choices, default=Medium | 

#### Results app

**Result model**

| Key in db | Field Type | Validation |
|---|---|---|
| eventinstance  | ForeignKey | EventInstance, on_delete=models.SET_NULL, null=True, blank=True | 
| distance  | ForeignKey | Distance, null=True, blank=True, on_delete=models.SET_NULL | 
| discipline  | ForeignKey | Discipline, null=True, blank=True, on_delete=models.SET_NULL | 
| event_format  | ForeignKey | Format, null=True, blank=True, on_delete=models.SET_NULL | 
| athletefirstname  | CharField | max_length=40, null=True, blank=True | 
| athletesurname  | CharField | max_length=40, null=True, blank=True | 
| athlete  | CharField | max_length=125, null=True, blank=True | 
| dateofbirth  | DateField | null=True, blank=True | 
| gender  | CharField |  max_length=2, choices=gender_choices, null=True, blank=True | 
| bibnumber  | DecimalField | max_digits=6, decimal_places=0, null=True, blank=True | 
| agecat  | CharField |  max_length=6, choices=age_cat_choices, default=Senior, null=True, blank=True | 
| athlete_type  | CharField | max_length=18, choices=athlete_type_choices, default=Myself, null=True, blank=True | 
| club  | ForeignKey | Club, null=True, blank=True, on_delete=models.SET_NULL | 
| chiptime  | DurationField | null=True, blank=True | 
| guntime  | DurationField | null=True, blank=True | 
| isvirtual  | BooleanField | null=True, blank=True, default=False | 
| hyperlink  | CharField | max_length=240, null=True, blank=True | 
| imageupload  | ImageField | null=True, blank=True | 
| verifiedresultforvirtual  | BooleanField | null=True, blank=True, default=False | 
| linkedathlete  | DecimalField | max_digits=3, decimal_places=0, null=True, blank=True | 



## [Deployment](#deployment)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

* On Heroku Website https://dashboard.heroku.com/apps , New -> Create New App
* Choose App name and region.
* Use Resources - Addons - Heroku Postgres

* In gitpod:
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt

* In settings.py
- `import dj_database_url`

```
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': dj_database_url.parse('postgress-url-goes-here')
}
```
* NB Get url from Heroku App settings tab / reveal config vars.

* Run migrations again (different database)

* `python3 manage.py showmigrations` Will show none exist

* `python3 manage.py migrate`

* To import product data, use fixtures:
- `python3 manage.py loaddata categories`
- `python3 manage.py loaddata products`
- NB categories must be created first as products depend on them.

* Create superuser account in the new database
- `python3 manage.py createsuperuser`


NB DO NOT COMMIT DATABASE URL TO VERSION CONTROL.

* Update settings.py to connect to a different database depending on if this is deployed or production version:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* `pip3 install gunicorn`
* `pip3 freeze > requirements.txt`
* Create `Procfile` in root folder with the contents `web: gunicorn race_hub.wsgi:application`

* NB: Check folder for Procfile is correct

* In terminal:
- 'heroku login' or 'heroku login -i'
- `heroku config:set DISABLE_COLLECTSTATIC=1 --app race-hub`

* In settings.py `ALLOWED_HOSTS = ['race-hub.herokuapp.com', 'localhost']`
* NB must be wrapped in `` above.

* If the app was created on the heroku website, set the remote repo. `heroku git:remote -a race-hub-ado`

* to check: `git remote -v`

* The great moment! `git push heroku master`

* To deploy to github automatically:
- In Heroku web interface:
- Deploy -> Github
- Select repo and connect.
- Enable automatic deploys

* https://miniwebtool.com/django-secret-key-generator/ 
- Add this to Heroku -> Config Vars -> Add the secret_key
-  Update settings.py to contain it: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
- Set `DEBUG = 'DEVELOPMENT' in os.environ` in settings.py

### Creating an AWS Account

* Use AWS s3 to store static files.
- Create account at https://aws.amazon.com/
- Account type personal
- Go to AWS Management Console.
- Open s3
- Create new bucket
- In Set Permissions, uncheck Block All Public Access

* Bucket settings:
- Properties -> Static Website Hosting
- Use default values index.html and error.html
- Save
- Permissions:
- CORS Configuration:
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
- Bucket Policy -> Policy Generator
- Policy Type: s3 Bucket Policy
- Principal: *
- Action: GetObject
- Copy ARN from the other tab eg `arn:aws:s3:::race-hub-ado`
- Add statement
- Generate Policy
- Copy Policy into other tab 'Bucket Policy'
- BEFORE SAVING: add /* into the resource key `"Resource": "arn:aws:s3:::race-hub-ado/*",`
- Access Control list -> Public Access -> Tick 'List Objects' and save.

* Use AWS service 'IAM' to connect to the bucket
- Go to IAM
- Click Access Management -> Groups
- Create New Group 'manage-race-hub'
- Click next twice (no policy to attach yet)
- Create Group
- Policies -> Create Policy
- Create Policy
- json tab -> Import managed policy
- Search for s3 and import the s3 Full Access Policy.
- From Bucket Policy in s3, get the arn and edit the json accordingly.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::race-hub",
                "arn:aws:s3:::race-hub/*"
                ]
        }
    ]
}
```
- Review Policy
- Add name and description. 
- Create
- Go to Groups -> Select the group -> Permissions tab -> Attach policy -> search and attach.

* users
- Add user
- Include static files access.
- Next: Permisssions
- Add user to group.
- Create user
- ESSENTIAL: Download .csv file.

* Connecting django to Amazon s3.

- `pip3 install boto3`
- `pip3 install django-storages`
- `pip3 freeze > requirements.txt`
- Add 'storages' to installed apps in settings.py

- in settings.py:

```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'race-hub'
    AWS_S3_REGION_NAME = 'EU (London)'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Add these config vars in Heroku: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS.
- Delete Config Var for DISABLE_COLLECTSTATIC

- create custom_storages.py in main project folder. NB CHECK this location carefully. It should be at the same level as README.md
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
- update EU (London) to eu-west-2 in settings.py

* Add cache control:
```
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```

- Go to s3 and create a new folder called media. Upload all product images.
- Grant public permissions.

* Tidying up

- attempt to log in as admin (causes allauth to attempt to verify)
- in django admin panel, verify email address and make primary for the super user account.

* Stripe
- Add Stripe Keys to heroku config vars.
- Add new Stripe Webhook Endpoint. (Remember to tick viewing test data)
- Configure endpoint as follows:
- https://race-hub.herokuapp.com/checkout/wh/
- Select Receive all events.
- Add Endpoint.
- Add signing secret to Heroku Config Vars.
- Should now have: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET - all matched to what exists in settings.py
- send test webhook from Stripe to check.

### Email setup.

* In Gmail:
- Settings (cog)
- Accounts and import
- Other Google Account Settings
- Security
- 2 Step Verification
- Verify
- Turn On
- Under Signing in to Google heading, choose app passwords.
- Create app passwords: Type Mail / Other / enter django in the box.
- Copy the key and enter it in the Heroku app as a config var as EMAIL_HOST_PASS
- Create EMAIL_HOST_USER as the gmail account.

* In settings.py:
```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'hello@racehub.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

#### Further notes on deployment process



NB: Heroku login ipaddress mismatch error: Use `heroku login -i` to login from terminal rather than opening browser

NB: eu-west-2 for London in django settings.

During Deployment an error was found in the requirements.txt file due to a typo. This was fixed and the deployment process was then successful.

During Deployment a typo was found in Procfile. NB race_hub is the name of the application. race-hub is used in AWS and also as the project name in Heroku.

NB When logging in to deployed app for the first time, to verify email address... this may not appear. Try logging in to front end. This will cause allauth to create the email address in the back end. It can then be verified.

Bug found during deployment. Image urls were incorrectly coded and did not include {{ MEDIA_URL }} path.

## [Local Development](#local-development)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

### IDE selected:
- Gitpod installed with Python 3 and pip

- Gmail account with two-factor authentication enabled, and
- Stripe free account.

### How to replicate the project using Gitpod
- Navigate to the [project repository](https://github.com/jonburdon/race-hub)
- Click the green 'Gitpod' button
-  This will open the project in a new Gitpod IDE.
-  Open terminal
- Type `python3 manage.py runserver`
- This will run a new copy of the project in Gitpod local development environment

## [Testing](#testing)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

### Ongoing Testing

As with any project, the developer tested and checked components thoroughly during production. For example, during development, navigation elements from https://codepen.io/skywalkapps/pen/VeNzwG were found to be incompatible with Bootstrap 4. The current navigation was found to not allow any scrolling on mobile in the large dropdowns until a min-height was asigned to the containing div.

### Testing Credentials and Instructions:

* Card number for testing 4242 4242 4242 4242
* My Racehub profile id number for adding a Racehub Friend: User name has a racehub ID of 


### Automatic Testing

Automatic testing has not been implemented. Tests were created to test views in the Results app. It was the developers intention to explore this at only a basic level to allow more time for learning the logic of the web application itself. Time did not allow for further tests for models and views, or for other apps.

The following command is used in the command line to run the automatic tests:

`python manage.py test`

This will only one run test, which checks a url in the results app. The test passes.

### Manual Testing

Manual testing was performed in a three step approach:

- Testing as a Race Organiser took place first in the manual testing process. When the project was deployed to Heroku, as it started with a blank database, the developer tested the project by only adding content via the front end interface initially.
- When Deployed to Production, a blank database was used and the data added as if using the site as a site administrator. This helped identify issues with the front end Organiser Dashboard.
- Testing of User Stories. Testing of Features and Defensive Design
- Device testing.

#### Organiser Testing
- Organiser can create new event instance and then parent event.
- Organiser can change event instance connected to the parent event.
- Organiser can view all results
- Organiser can manage and approve virtual results

#### Registered User Testing
- User can create a new account
- User can enter self for an event
- User can add a new racehub friend
- User can enter a racehub friend for an event
- Racehub Friend subsequently appears in results list, and this result appears on their My Racehub profile page
- User can delete racehub friend
- User can add a new family or friend
- User can enter a racehub friend for an event
- Friend subsequently appears in entry list
- User can delete family or friend
- User can transfer an entry to someone else

#### Unregistered User Testing
- User cannot enter events without logging in


#### Issues Identified during testing:

**Issue #1** During testing it was found that some database fields were not required. These were changed to required in the model in order to provide a more defensive design approach to the database. Issue resolved.

**Issue #2** Some forms were displaying database field names rather than friendly alternatives.

**Issue #3** Date of Birth can be entered as any date. This should be changed to ensure it is always a date in the past, more than 18 years ago.

**Issue #4** Add Event and Add Results forms require additional helper text in the second column. A useful additional feature here would be to be able to look up a Racehub User using a select field.

**Issue 5** No datepicker was found in the Add results form and Entry Transfer forms. This was added.

**Issue 6** No back to list button was present on the Add results form page, Review Virtual Results page or Result detail pages. These were added as an additional feature to allow navigation between these pages.

**Issue 7** When entering a non virtual event as a user, no result is created by the webhook handler. Virtual results are created. This was as a result of the variable virtual not being defined in the webhook handler for non virtual results. `else: virtual = False` Issue resolved.

**Issue 8** Regular users did not have permission to transfer results as this was secured in the view. Issue resolved. This was as a result of an incorrect template link, with the user being directed the the edit result template. Issue resolved.

**Issue 9** No functionality had been added to remove / delete a Racehub Friend using the My Rachub dashboard. The same functionality was missing from add Family and Friends. This functionality was added.

**Issue 10** The Add Racehub Friend function was found not to be working when testing if athlete id numbers are valid. This error was idenfied - the view was using `RaceHubFriends.objects.all()` and was corrected to `AthleteProfile.objects.all()`. Issue resolved.

**Issue 11** It was found that the connection to Mapbox to longer worked therefore map tiles in 'Map View' no longer rendered. This was found to be the case in the reference code studied on Codepen as well as various similar examples meaning that the interaction between leafletjs and the mapbox api has changed. The js was updated to connect to openmap api rather than mapbox api.

**Issue 12** When creating a new account, it was found that it is possible to create an account and then enter yourself for an event whilst the Athlete Profile contains no information. An if statement was added to render the select field only if the Athlete First Name exists and otherwise add a warning button. This feature should be improved to make the form fields all required when editing the athlete form (whilst they are not actually required in the database, due to the fact that the athlete profile is created automatically during account creation.)

**Issue 13** When adding a new event, as organiser, there was no function to delete Event Instances. This was added.

**Issue 14** Map View - there are identical markers used for user's location and events. This is confusing, as the home marker has no popup. Also, events with an identical location overlap therefore one disappears.



## [Acknowledgements](#acknowledgements)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

- The developer made close reference to the Code Institute tutorials for core logic, base.css and some front end templates. Original code was written to handle multiple types of event entry, connect these with the athlete and results models via the webhook handler.
- Inspiration for Bootstrap cards taken from: https://codepen.io/aminulhchy/pen/RVeJMZ

Navigation:
- Used advice from https://stackoverflow.com/questions/29752882/cant-scroll-within-mobile-drop-down-nav/29753214 to make mobile mega dropdowns scroll on mobile devices
- Refactored code, based on: https://codepen.io/JakubHonisek/pen/xXaYqg
Code for mobile view buttons refactored from Code Institute tutorial
- Responsive Bootstrap Mega Menu: https://codepen.io/JakubHonisek/pen/xXaYqg
- Original Leaflet map view reference code when connecting to Mapbox api: https://codepen.io/bbrook154/pen/RRQQyG
- Map View Reference used for connecting to Open Maps https://harrywood.co.uk/maps/examples/leaflet/geolocate.view.html
- Footer: https://mdbootstrap.com/docs/jquery/navigation/footer/

#### Media:
- icons licensed and used from https://uxwing.com/
- logos created by the author using Boxy SVG for macos

Event Images used under lisence from:
- South Huddersfield Trail and Road Series (Photographer: Wil Valovin)
- Pixabay
- Free Images.com
- Stocksnap.io
- Unsplash.com


#### Useful Docmentation

https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html





