
Formatting taken from: https://raw.githubusercontent.com/Team-Fourtress/brkly/main/README.md
(another project from Momentum Students)

# [FOSTER-CLOSET: API](https://foster-closet.herokuapp.com/)

### FOSTER-CLOSET API is a REST API built with Django, built to serve the FOSTER-CLOSET front-end app that uses React.


## Models
| Model | Notes |
| ----- | ----- |
| [User]
| [Registry]
| [Item]

## Endpoints: 
| HTTP Method | Endpoint | Result | JSON Format |
| ----------- | -------- | -------| ----- |
| POST | `api/<basic model>/` | Creates a new model object |  |
| GET | `api/<basic model>/` | Returns a list of all objects of that model |  |
| GET | `api/<basic model>/<obj_pk>` | Returns the detail view for `<obj_pk>` |  |
| PUT | `api/<basic model>/<obj_pk>` | Replaces `<obj_pk>` |  |
| PATCH | `api/<basic model>/<obj_pk>` | Modifies `<obj_pk>` |  |
| DELETE | `api/<basic model>/<obj_pk>` | Deletes `<obj_pk>` |  |


|      | User |          |          |
| -------- | -------- | -------- | -------- |
| POST | `auth/token/login/` | Takes username and password-Logins and returns token|{"username":"<username>", "password":"<password>"}|
| POST | `auth/token/logout/` | Logout-destroys token|  |
| POST | `api/auth/users` | User registration|{"username":"<string>", "password":"<string>", "phone_number":"<string>"} |
| PUT/PATCH/DELETE | `api/user/<pk>/` | Replaces/Modifies/Deletes `User` | |
| GET | `api/user/<pk>/` | Returns a `User` object | |

|      | Registry |          |        |
| -------- | -------- | -------- | -------- |
| POST | `api/registry/` | Creates a `Registry` object for logged-in user, and creates `Item` objects tied to that registry | |
| POST | `api/registry/` | {"items": [{"description":"<description>"}, {"description":"<description>"}, .. ]} | |
| GET | `api/registry/` | Returns a list of all of currenty logged-in user's `Registries` | |
| GET | `api/registry/all/` | Returns a list of all of registries excluding current user| |    
| GET | `api/registry/<pk>` | Returns a specific`Registry` | |
| PUT/PATCH/DELETE | `api/registry/<pk>` | Replaces/Modifies/Deletes Registry

|      | Item |         |         |
| -------- | -------- | -------- | -------- |
| POST | `api/item/` | Creates an `Item`| {"registry": <registry_id>, "description":"<string>"} |
| GET | `api/item/<pk>` | Returns all of a user's `Item` objects |  |
| GET | `api/item/<pk>` | Returns an `Item` |  |
| PUT/PATCH/DELETE | `api/item/<pk>` | Replaces/Modifies/Deletes `Item` | Requires login with associated user  |
| GET | `api/item/status` | Returns  all of a user's `Item` objects sorted by status |  |

|      | Message |         |      |
| -------- | -------- | -------- | -------- |
| POST | `api/message/` | Creates and sends a `message`| {"reciever":<user_id>, "message":"<string>"}  |
| GET | `api/message/` | Returns logged-in user's `Messages` |  |



## Model Construction

### User
```
{
    "username": CharField - mandatory
    "password": CharField - mandatory
    all other defaults
    "first_name": CharField
    "last_name": CharField
    "is_foster": BooleanField
    "is_donor": BooleanField
    "zip_code": CharField
    
  
}
```

### Registry
```
{
    "user": ForeignKey(to=User) - auto adds `self.request.user` upon creation
    "time_made": DateTimeField  - tracks when registry is created
}
```

### Item
```
{
    "registry": ForeignKey(to=Registry) - mandatory
    "donor": ForeignKey(to=User) 
    "description": CharField - description of item
    "fulfilled": BooleanField - tracks if the requested item has been fulfilled
    "time_fulfilled": DateTimeField - updates whenever item is updated
}
```

### Messsage

```
    sender - logged-in user
    reciever - mandatory, id of user
    message - mandatory
    time_made 
    url - mandatory

```


# Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- A starting Django app named `core` is provided.
- There is a custom user model defined in `core.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is used to manage dependencies.
