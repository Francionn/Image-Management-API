# Image-Management-API

## Description.

Getting started with the ORM (SQLalchemy) is a toolkit for greater independence from data base. exemplifying:

                 Interaction Managed by ORM
                --------------------------
                        * Classes -> SQL
                        * Standard Syntax

Code
 └─> Business Logic
         └─> ORM
                 └─> * Connection Management
                     * Connection Pool
                         └─> Database


Following the explanation, the connection between the database and the classes is established by ORM. 
This way, the PostRepository class can be used for CRUD operations, and the same approach can be applied to routes in the app.

## Installation.

To install the necessary dependencies, run the following commands:

```bash
pip install Flask
pip install SQLAlchemy
pip install Werkzeug
````

## Comments.

Import base64 - Convert the image to binary.

Using the concept for function "to_dict()" in class "Db_post", facilitating the passing of image and other date.

Observation: ('DB_CONNECTION_STRING', 'mysql+pymysql://root:password@localhost:3306/user') Enter your password if you use MySQL.
