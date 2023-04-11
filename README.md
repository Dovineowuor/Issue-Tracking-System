# Issue-Tracking-System
Tracking System (Trello-Of-Africa)

This is a project to build an issue tracking system.

# App Features Repository

This repository showcases all the respective features implemented on this app with redference to their files. Each fdirectory conteis respective app functionality.

## App Features

### Authentication
	This Feature supports User authentication and authentication state management. Its responsible for registration, Login, Logout and delete account functionalities. This feature is implemented using `Auth0 API` as a third party service. It aso Authorizes Users / Clients to access specified features.

### User Management
	This feature supports all registered users management. This app will handle user management tasks such as adding new users, updating user information, and deleting users. You can use Django's built-in user model or create a custom user model to store user information.

### State Management
	This app is responsible for the respective issue state management. The status of the issues *should* include :
		- `Open`
		- `In Progress`
		- `Resolved` and 
		- `Closed`

	This app will handle the different states an issue can be in. We created a model to store the different states and use Django's built-in admin interphase and custom interfaces to manage them.

### Issue Creation and Handling App
	This feature app handles the Issue creation and handling. We created a model to store the details of each issue and use Django's forms to validate user input. We also created views to handle different actions such as creating a new issue, updating an issue, and assigning an issue to a Client ... etc

### Issue Tracking and Resolution App
	This Feature helps in tracking the state and status of an Issue whether resolved, In Progress, Closed or Open. We create dviews to display a list of open issues, resolved issues, In progress issues and closed. We also created views to handle different actions like marking an issue as resolved 
(Resolve), In Progress (`In Progress`), Open,(`Open`), and closing an issue (`Close`).

### Issue Assignment App
	This app handles the assignment of issues to different users. We created a model to store the assignments and use views to handle the assignment of issues.

### Real-Time Notification System
	This feature handles the information and keeping up to date the information and mailing system of the app whe issue statuses change eg Clodes, New Issue(Open), ... etc. We used django channel to implement real-time notification and send notification to users via email or push notification.

### Files and Document Handling
	This feature app handles files and documents opening, editing, creating, deleting and updating uploading and downloading files and documents.

### Automatic Memo Creation 
	This feature app handles creation of automatic memos when an issue is raised, an issue status changes and an issue is resolved(`clodes`) and also will send the to respective appropriate users.

### Data Analytics
	This feature app will handle analytics of the issues related. We used a django builtin analytics tool intergrating additional analytic functionalities using third party appllications.

### Team Management
	This app handles team management tasks such as adding new team members, updating team information, and deleting team members. We created a model to store team information and use views to handle team management tasks.

## Third Party Apps
	1- Auth0;
This app handles authenyication and authentication states. It also handles app security features.

## Project Stracture

	issue_tracking_system/
	├── src/
	│   ├── accounts/
	│   │   ├── migrations/
	│   │   ├── templates/
	│   │   ├── __init__.py
	│   │   ├── admin.py
	│   │   ├── apps.py
	│   │   ├── models.py
	│   │   ├── urls.py
	│   │   └── views.py
	│   ├── analytics/
	│   │   ├── migrations/
	│   │   ├── templates/
	│   │   ├── __init__.py
	│   │   ├── admin.py
	│   │   ├── apps.py
	│   │   ├── models.py
	│   │   ├── urls.py
	│   │   └── views.py
	│   ├── documents/
	│   │   ├── migrations/
	│   │   ├── templates/
	│   │   ├── __init__.py
	│   │   ├── admin.py
	│   │   ├── apps.py
	│   │   ├── models.py
	│   │   ├── urls.py
	│   │   └── views.py
	│   ├── issues/
	│   │   ├── migrations/
	│   │   ├── templates/
	│   │   ├── __init__.py
	│   │   ├── admin.py
	│   │   ├── apps.py
	│   │   ├── models.py
	│   │   ├── urls.py
	│   │   └── views.py
	│   ├── teams/
	│   │   ├── migrations/
	│   │   ├── templates/
	│   │   ├── __init__.py
	│   │   ├── admin.py
	│   │   ├── apps.py
	│   │   ├── models.py
	│   │   ├── urls.py
	│   │   └── views.py
	|   ├── ...
	|   ├── Team Management/
	|   |
	│   ├── templates/
	│   │   ├── base.html
	│   │   ├── login.html
	│   │   ├── dashboard.html
	│   │   ├── create_issue.html
	│   │   ├── issue_detail.html
	│   │   ├── team_detail.html
	│   │   ├── create_team.html
	│   │   ├── update_team.html
	│   │   ├── analytics.html
	│   │   ├── document_list.html
	│   │   ├── upload_document.html
	│   │   ├── update_document.html
	│   │   └── notifications.html
	│   ├── static/
	│   │   ├── css/
	│   │   ├── js/
	│   │   ├── img/
	│   │   └── vendor/
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── requirements.txt
	└── manage.py

In the above directory structure, the src directory contains all the apps of the project, each responsible for a specific feature or functionality.

accounts app handles user authentication and management
analytics app handles data analytics
documents app handles document handling
issues app handles issue creation, handling, tracking, and resolution
teams app handles team management and administration
The templates directory contains all the HTML templates used in the project, and the static directory contains all the static files like CSS, JavaScript, and images.

The settings.py file in the root directory contains the project settings, and the urls.py file contains the project URLs.

