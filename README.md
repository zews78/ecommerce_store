# GameStore

## Table of contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Technology](#technology)
- [Features](#features)
- [Database Models](#database)
- [Run](#run)
- [License](#license)

## Introduction

• A virtual game store to buy your favourite games from all platforms. The website contains products, their details, prices etc.

• The platform is created with a clean UI to buy all your games without any hassle.

• Tech Used: Django, Bootstrap, HTML/CSS, JS. 

• Utilities Used: Pillow, Whitenoise, Auth Forms, Waitress.

## Demo

![orders](https://user-images.githubusercontent.com/56071565/123709244-5d757f80-d88a-11eb-99d6-39140e62aa6f.png)
![cart](https://user-images.githubusercontent.com/56071565/123709250-5f3f4300-d88a-11eb-8ccb-4ec701f29d36.png)
![search ](https://user-images.githubusercontent.com/56071565/123709253-5fd7d980-d88a-11eb-95fd-03818406bf28.png)
![playstation](https://user-images.githubusercontent.com/56071565/123709256-60707000-d88a-11eb-8278-96786a8cb08f.png)
![home](https://user-images.githubusercontent.com/56071565/123709259-623a3380-d88a-11eb-85ac-d69e29eb4455.png)

The application is deployed to Heroku and can be accessed through the following link:

[GameStore on Heroku](https://gamestoredj.herokuapp.com/)

The website resembles a real store and you can add products to your cart and buy them. The payment options have not been integrated yet.

In order to access the admin panel on "/admin" you need to provide the admin email and password.

## Technology

The application is built with:

- asgiref==3.3.4
- Django==3.2.2
- Pillow==8.2.0
- pytz==2021.1
- sqlparse==0.4.1
- waitress==2.0.0
- whitenoise==5.2.0

## Features

The application displays a virtual Game store that contains virtual products and contact information.

Users can do the following:

- Create an account, login or logout.
- Browse available products added by the admin or members having staff status.
- Add products to the shopping cart.
- Delete products from the shopping cart.
- View the shopping cart.
- To checkout, a user must be logged in.
- The profile contains all the informations about delivery address and user can add new address too.
- User can see their past orders and its status.
- Search bar allows user to search for games and related results will be displayed.
- Add reviews for a product.

Admins can do the following:

- Login or logout to the admin panel.
- View all the information stored in the database. They can view/add/edit/delete orders, users, products and categories. The cart model cannot be modified by an admin because a cart is either modified by the logged in user before the purchase or deleted after the purchase.

## Database

 - MySQL database is used to store products details.
 - One can see the product fields in model file.

 ### User Schema:

- username (String)
- email (String)
- password (String)

### Product Schema:

- ProductId(Number)
- name (String)
- image (String)
- description (String)
- price (Number)
- genre (ObjectId - a reference to the category schema)

### Cart Schema:

- items: an array of objects, each object contains: <br>
  ~ productId (ObjectId - a reference to the product schema) <br>
  ~ quantity (Number) <br>
  ~ price (Number) <br>
  ~ name (String) <br>
- totalCost (Number)
- user (ObjectId - a reference to the user schema)

### Order Schema:

- user (ObjectId - a reference to the user schema)
- product (ObjectId - refrence to product schema)
- address (String)
- OrderDate (Date)
- Status (array of possible status)

## Run

To run this application
- you need to install [Technology](#technology) items using pip install -r requirements.txt
- Set your SECRET_KEY
- Set your Database
- type <b>python manage.py runserver</b>

## License

[![License](https://img.shields.io/:License-MIT-blue.svg?style=flat-square)](http://badges.mit-license.org)

- MIT License
- Copyright 2021 © [Roneet Kumar Singh](https://github.com/roneetsingh)
