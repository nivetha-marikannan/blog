# Blog Application

A full-featured blog web application built with **Django 5.1.4**, developed as my first hands-on Django project. This project covers the complete lifecycle of a web application — from data modeling and form handling to authentication, media uploads, and template rendering.

---

## Project Overview

This is a multi-user blog platform where registered users can create, edit, delete, and view blog posts. Each post supports a title, body text, an optional image upload, and is associated with a specific author. The application enforces authentication, meaning only logged-in users can manage posts, and only the post's author can edit or delete it.

---

## Features

- User Registration and Login/Logout using Django's built-in auth system
- Create, Read, Update, Delete (CRUD) operations for blog posts
- Image upload support per post (stored in `media/post_images/`)
- Author-based access control — users can only edit or delete their own posts
- Post listing sorted by most recent published date

---

## What I Learned

Building this project was my first real experience with Django, and it covered a wide range of backend and full-stack concepts.

**Django Fundamentals** — Understanding the MVT (Model-View-Template) architecture and how Django ties the database, business logic, and presentation layer together.

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
