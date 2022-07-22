from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.reciever_id = data['reciever_id']
        self.sender = data['sender']
        self.reciever = data['reciever']

    @classmethod
    def get_user_with_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as reciever, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON messages.reciever_id = users2.id WHERE users2.id = %(id)s; "
        results = connectToMySQL('friendships_schema').query_db(query, data)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages
    
    @classmethod
    def save(cls, data):
        query = " INSERT INTO messages (content, sender_id, reciever_id) VALUES (%(content)s, %(sender_id)s, %(reciever_id)s);"
        return connectToMySQL("friendships_schema").query_db(query, data)
        
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM messages WHERE id = %(id)s;"
        results = connectToMySQL("friendships_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        return connectToMySQL('friendships_schema').query_db(query, data)
