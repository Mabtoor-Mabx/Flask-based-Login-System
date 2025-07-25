# Flask-based Login System

## 📌 Introduction

This project demonstrates a **Flask-based Login System** with session management. It provides a simple and secure way to authenticate users by validating credentials and managing sessions using **Flask**. The application ensures that only authenticated users can access the homepage, while unauthorized users are redirected to the login page.

This is a basic yet practical implementation for beginners who want to learn about Flask, sessions, and template inheritance in Python web development.

---

## ✅ Features

* **User Authentication**: Validates username and password.
* **Session Management**: Stores user session data to maintain login state.
* **Login & Logout**: Simple and user-friendly login and logout functionality.
* **Template Inheritance**: HTML templates using Jinja2 with `base.html` and child templates.
* **Error Handling**: Displays error message for invalid credentials.
* **Minimal & Clean UI**: Simple and responsive interface for easy understanding.

---

## 🛠 Workflow

1. **Home Page**:

   * Checks if the user is logged in.
   * Displays a welcome message if authenticated, otherwise redirects to the login page.
2. **Login Page**:

   * Accepts username and password through a form.
   * Verifies credentials and creates a session for the user.
   * Shows error message for invalid input.
3. **Logout**:

   * Ends the user session and redirects to the login page.
4. **Templates**:

   * `base.html`: Main template structure with styles.
   * `login.html`: Login form and error message handling.
   * `home.html`: Welcome screen for authenticated users.

---

## 📦 Libraries Used

* **Flask**

  * Web framework for creating the application.
  * Handles routes, sessions, and rendering templates.
* **Jinja2**

  * Template engine used with Flask for dynamic HTML content.

---

## 🔑 Key Concepts

* Flask Routing (`@app.route`)
* HTTP Methods: `GET` and `POST`
* Session Management (`session`)
* Template Inheritance (`extends`, `block`)
* Form Handling (`request.form`)
* URL Handling (`url_for`)
* Redirect and Response Handling

