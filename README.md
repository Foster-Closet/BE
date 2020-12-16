
Formatting taken from: https://raw.githubusercontent.com/Team-Fourtress/brkly/main/README.md
(another project from Momentum Students)

# [FOSTER-CLOSET: API](https://foster-closet.herokuapp.com)

### FOSTER-CLOSET API is a REST API built with Django, built to serve the front-end FOSTER-CLOSET front-end app using React.


## Models
| Model | Notes |
| ----- | ----- |
| [User]
| [Registry]
| [Item]


## Endpoints: 
| HTTP Method | Endpoint | Result | Notes |
| ----------- | -------- | -------| ----- |
| POST | `/<basic model>/` | Creates a new model object |  |
| GET | `/<basic model>/` | Returns a list of all objects of that model |  |
| GET | `/<basic model>/<obj_pk>/` | Returns the detail view for `<obj_pk>` |  |
| PUT | `/<basic model>/<obj_pk>/` | Replaces `<obj_pk>` |  |
| PATCH | `/<basic model>/<obj_pk>/` | Modifies `<obj_pk>` |  |
| DELETE | `/<basic model>/<obj_pk>/` | Deletes `<obj_pk>` |  |




|      | Registry |          |          |
| -------- | -------- | -------- | -------- |
| POST | `/registry/` | Creates a `Registry` object for that user, and creates `Items` tied to that registry | Requires a foster-family login|
| PUT/PATCH/DELETE | `/registry/<pk>` | Replaces/Modifies/Deletes `Registry` | Requires login with associated user  |
| GET | `/registry/<pk>` | Returns a list of all of `self.request.user`'s, aka currenty logged-in user's `Registries` | Requires login with associated user  |
| POST | `/item/` | Returns a list of all `Items`| Requires a `Registry` that is associated with the logged-in user  |
| PUT/PATCH/DELETE | `/item/<pk>` | Replaces/Modifies/Deletes `Item` | Requires login with associated user  |
| GET | `/item/<pk>` | Returns a list of all `Items` |  |

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


# Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- A starting Django app named `core` is provided.
- There is a custom user model defined in `core.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is used to manage dependencies.
