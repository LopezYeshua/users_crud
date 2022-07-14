# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database

DATABASE = "users"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
    # Now we use class methods to query our database
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( User(user) )
        return users

    # ! CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name, last_name, email) VALUES ( %(fname)s, %(lname)s, %(email)s );"
        return connectToMySQL(DATABASE).query_db( query, data)
    
    # ! READ/RETRIEVE TWO
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # Iterate over the db results and create instances of users with cls.
        user = User(results[0])
        return user

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)