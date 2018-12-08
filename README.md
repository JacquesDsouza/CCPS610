# Flask Form Content With work Flow

The project uses the Python Flask Frame work to create a Blog type website with a Simple workflow.

- **Name**: Jacques D'souza
- **Online Demo**: https://peaceful-castle-77000.herokuapp.com/home
- **Project Title**: Content Workflow
- **Course**:  CCPS530
- **Instructor**: Ghassem Tofighi


Repository structure:
```
  |__CCPS610 
  |__run.py 
     |__README.md 
     |__Procfile
     |__requirements.txt
     |__ccps610     
        ├── errors
        │   └── __init__.py
        │   └── handlers.py
        ├── main
        │   └── __init__.py
        │   └── routes.py
        ├── posts
        │   └── __init__.py
        │   └── forms.py
        │   └── routes.py
        ├── static
        ├── templates
            ├── errors
            │   └── 403.html
            │   └── 404.html
            │   └── 405.html
        │   └── about.html
        │   └── account.html
        │   └── browse.html
        │   └── browse_moderate.html
        │   └── browse_my_posts.html
        │   └── create_post.html
        │   └── home.html
        │   └── layout.html
        │   └── login.html
        │   └── post.html
        │   └── register.html
        │   └── reset_request.html
        │   └── reset_token.html
        │   └── user_list.html
        │   └── user_posts.html
        │   └── signup.html
        ├── users
        │   └── __init__.py
        │   └── forms.py
        │   └── routes.py
        │   └── utils.py
        └── __init__.py
        └── config.py
        └── models.py
```

## Features:
Workflow: (in Development)
1. Draft - New posts are not visible for anyone other than Admin/Moderators to view and initially approve.
2. Pending Approval - Posts are now visible to users. In order to move to the next state in the work flow, the post requires 50 Likes.
3. Discussion - Post become discussion forums where other members of the community can participate. 
4. Execution - Post is locked until further notice and only owner/Mod/admins can updated. 
5. Closed - Post is archived. 

Users Can modify their own Posts.
Admin and Moderators can modify all posts and delete where needed. 

User Panel - To modify personal settings
User Admin Panel - Change Roles and settings of all users

## Pulling the repository and Setting up the environment 


### Create a Test folder to setup and run the application

Type the following into the console and traverse into the directory

```bash
mkdir NewFolder; cd NewFolder
```

### Git Hub Commands
Initialize Git
Add the current Git Repository to you configurations
Pull the contents from the online repository

```bash
git init
git remote add origin https://github.com/JacquesDsouza/CCPS610.git
git pull -q origin master
```

### Virtual Environment 
Spin up a virtual environment to test out the build.

```bash
virtualenv venv
source venv/Scripts/activate
```

### Download the extensions
Download the required extension using the requirements.txt file.

```bash
pip install -r ./requirements.txt
```

### Setting up the Database
The application currently requires two tables within a database. Users and Posts


```SQL
CREATE TABLE users ( 
id serial PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(120) NOT NULL UNIQUE,
image_file VARCHAR(120) NOT NULL DEFAULT 'default.png',
password VARCHAR(100),
usertype VARCHAR(20) NOT NULL DEFAULT 'User' ,
usertype_id INTEGER DEFAULT 1,
moderator_flag  BOOLEAN NOT NULL DEFAULT FALSE,
admin_flag  BOOLEAN NOT NULL DEFAULT FALSE
);
```



```SQL

CREATE TABLE posts (
id serial PRIMARY KEY,
title VARCHAR(100) not null,
post_category VARCHAR(20) not null DEFAULT 'Not Applicable',
post_category_id INTEGER DEFAULT 0,
post_type VARCHAR(20) not null DEFAULT 'Not Applicable',
post_type_id INTEGER DEFAULT 0,
status VARCHAR(20) not null DEFAULT 'Draft',
status_id INTEGER DEFAULT 0,
date_posted date not null,
content VARCHAR(300) not null,
support_count INTEGER DEFAULT 0,
user_id INTEGER REFERENCES users (id)
);

ALTER TABLE posts
    ADD CONSTRAINT fk_posts_users FOREIGN KEY (user_id) REFERENCES users (id);

```


### Update the System environment variables 
The following variables need to be declared:
Database URI
gmail to send emails from & password
```
DATABASE_URL
EMAIL_PASS
EMAIL_USER
```

### Run the Python program to boot up the application.
Download the required extension using the requirements.txt file.

```bash
python run.py
```
