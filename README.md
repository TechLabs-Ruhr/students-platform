# StudyMeet - A Platform for Study Groups

**Description:** StudyMeet is a platform that allows you to create, find and join study groups. 
Study groups are meant to be chatrooms with specific information: Group name, description, degree course, location/university and group type.
You can search for groups via a filter function. For the platform, an account is needed to join groups.

In this repository, you will find initial implementations of the landing page, the chat function and backend for log in. A database based on mostly MySQL is also included.

## Road Map
Our project followed mostly the design thinking process. 
Most of our work does only contain basic code since we only have reached the beginning of the implementation part in our project phase.
To look further into our results, feel free to look at our Figma file.

## Draft design
- [Figma main file](https://www.figma.com/file/fT4NbWfoZmmMpFSuUUv7R8/English-Version)

## Components
### Chat
Chat component based on a Microsoft Teams clone built with [Chat Engine](https://chatengine.io/). It was made with React, a dedicated [chat engine](https://www.npmjs.com/package/react-chat-engine) and some HTML code.
These models also provide interesting incentives to continue the project.
For successful implementation, some libaries have to be implemented in the React project. 
If necessary, look up the commands relevant to you in the documentation website.
For the fictitious profile names and profile pictures we recommend [Robohash](https://robohash.org/).

### Database
MySQL [Python](https://www.freecodecamp.org/news/connect-python-with-sql/) backend script. It contains basic functions for the user, group and membership relations.
[Fast API scripts](https://fastapi.tiangolo.com/de/tutorial/) for insert and select included.
Instructions can be found in the folder.

### Filter
Initial filter framework code based on Django.

### Log-In
Log-In Python backend scripts. One is based on Flask and made to work with SQLite3.
Also a [Django based version](https://www.ordinarycoders.com/blog/article/django-user-register-login-logout) included.

### Registration
Registration Python backend script based on [Django](https://django-registration.readthedocs.io/en/2.0/quickstart.html) and it's [authentification](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/).

## Contributors

- [@patrickblf](https://github.com/patrickblf)
- [@sara507](https://github.com/Sara507)
- [@dHoangBach](https://github.com/dHoangBach)
- [@SaskiaO96](https://github.com/SaskiaO96)

## Organization and Mentors
- [@NJannasch](https://github.com/NJannasch)
- [@mk406](https://github.com/mk406)
- [@TheMerphin](https://github.com/TheMerphin)
