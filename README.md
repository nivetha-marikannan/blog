# Django Blog Application

A full-featured blog web application built with **Django 5.1.4**, developed as my first hands-on Django project. This project covers the complete lifecycle of a web application — from data modeling and form handling to authentication, media uploads, and template rendering.

---

## Project Overview

This is a multi-user blog platform where registered users can create, edit, delete, and view blog posts. Each post supports a title, body text, an optional image upload, and is associated with a specific author. The application enforces authentication, meaning only logged-in users can manage posts, and only the post's author can edit or delete it.

The project name internally is **first_one** (Django project) with a core app named **calc** (the blog app).

---

## Features

- User Registration and Login/Logout using Django's built-in auth system
- Create, Read, Update, Delete (CRUD) operations for blog posts
- Image upload support per post (stored in `media/post_images/`)
- Author-based access control — users can only edit or delete their own posts
- Post listing sorted by most recent published date
- Responsive UI built with Bootstrap 5.3 and Google Fonts (Lobster)
- Gradient-styled frontend with card-based post layout
- Django Admin panel with Post model registered
- SQLite database for local development
- Static files served via `/static/`, media files via `/media/`
- CSRF protection, session management, and clickjacking protection middleware enabled

---

## Project Structure

```
blog/
├── first_one/           # Django project settings and root URL config
│   ├── settings.py      # App config, installed apps, DB, media, auth redirects
│   ├── urls.py          # Root URL routing (admin + calc app)
│   ├── wsgi.py
│   └── asgi.py
├── calc/                # Core blog app
│   ├── models.py        # Post model (title, text, image, author FK, published_date)
│   ├── views.py         # Function-based views for all CRUD + auth flows
│   ├── urls.py          # App-level URL patterns (namespaced as 'calc')
│   ├── forms.py         # ModelForm for Post creation/editing
│   ├── admin.py         # Post registered in Django admin
│   ├── serializers.py   # Prepared for future REST API integration
│   ├── migrations/      # 5 migration files tracking model evolution
│   ├── templates/calc/  # HTML templates (base, login, signup, post_list, post_detail, post_edit)
│   └── static/css/      # Custom CSS (blog.css)
├── media/post_images/   # Uploaded post images
├── staticfiles/         # Collected static files
├── db.sqlite3           # SQLite database
└── manage.py
```

---

## Data Model

```python
class Post(models.Model):
    title          = models.CharField(max_length=100)
    text           = models.TextField()
    image          = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
```

The model went through 5 migrations during development, reflecting iterative design decisions — starting from a basic form model, renaming it to Post, then adding the image field.

---

## URL Patterns

| URL | View | Description |
|-----|------|-------------|
| `/` | login_view | Default landing — login page |
| `/login/` | login_view | User login |
| `/signup/` | signup | User registration |
| `/posts/` | post_list | List all posts (login required) |
| `/blog/<id>/` | post_detail | View a single post |
| `/blog/new/` | post_new | Create a new post (login required) |
| `/blog/<id>/edit/` | post_edit | Edit a post (author only) |
| `/blog/<id>/delete/` | post_delete | Delete a post (author only) |
| `/logout/` | logout_view | Logout and redirect to login |
| `/admin/` | Django admin | Admin panel |

---

## Tech Stack

- **Backend:** Python 3, Django 5.1.4
- **Database:** SQLite via Django ORM
- **Frontend:** Django Templates, Bootstrap 5.3, Google Fonts (Lobster)
- **Authentication:** Django built-in auth (UserCreationForm, AuthenticationForm)
- **File Handling:** Django ImageField, Pillow
- **Static/Media:** Django staticfiles + media serving in development

---

## What I Learned

Building this project was my first real experience with Django, and it covered a wide range of backend and full-stack concepts.

**Django Fundamentals** — Understanding the MTV (Model-Template-View) architecture and how Django ties the database, business logic, and presentation layer together.

**ORM and Migrations** — Defining models in Python and letting Django generate the SQL. I went through 5 migrations iteratively as I refined the Post model, which taught me how schema changes work in a real project lifecycle.

**Function-Based Views** — Writing views manually (rather than class-based) to deeply understand the request/response cycle, form validation, redirect logic, and how context is passed to templates.

**Authentication System** — Integrating Django's built-in user registration, login, logout, and @login_required decorator without building auth from scratch. Understanding session-based authentication.

**Authorization vs Authentication** — Enforcing that only post authors can edit or delete their own posts using object-level permission checks (post.author != request.user returning HttpResponseForbidden).

**Forms and ModelForms** — Using ModelForm to auto-generate forms from the model and handling both GET (render empty form) and POST (validate + save) flows cleanly.

**File Uploads** — Handling ImageField with request.FILES, configuring MEDIA_URL and MEDIA_ROOT, and serving uploaded files during development.

**URL Namespacing** — Using app_name = 'calc' and {% url 'calc:post_list' %} to avoid URL name collisions across apps.

**Template Inheritance** — Using a base.html template with {% block %} tags so all pages share the same layout, navigation, and styles without duplication.

**Static Files** — Separating static assets (CSS) from templates and loading them with {% load static %}.

**Django Admin** — Registering models with admin.site.register() to get an instant admin interface for managing data.

**Settings Architecture** — Configuring INSTALLED_APPS, MIDDLEWARE, TEMPLATES, DATABASES, AUTH_PASSWORD_VALIDATORS, LOGIN_REDIRECT_URL, and media/static settings.

---

## Author

**Nivetha M** — Backend and Full Stack Developer | AI and DS @ KCT

[LinkedIn](https://www.linkedin.com/in/nivetha-m-b3849b290)
