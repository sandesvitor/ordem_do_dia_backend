from flask_restful import Resource, reqparse


users = [
    {
        'user_id': '100',
        'nome': 'Vitor Sandes',
        'email': 'vitor@ordemdodia.com.br',
        'password': '123456789'
    },
    {
        'user_id': '101',
        'nome': 'Pedro Fountora',
        'email': 'pedro@ordemdodia.com.br',
        'password': '123456790'
    },
    {
        'user_id': '103',
        'nome': 'Guilherme Pim',
        'email': 'pim@ordemdodia.com.br',
        'password': '123456791'
    }
]

class UserModel:
    def __init__(self, user_id, nome, email, password):
        self.user_id = user_id
        self.nome = nome
        self.email = email
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id,
            'nome': self.nome,
            'email': self.email,
            'password': self.password,
        }


class Users(Resource):
    def get(self):
        return {'users': users}


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('password')

    def find_user(self, user_id):
        for user in users:
            if user['user_id'] == user:
                return user
        return None
    
    def get(self, user_id):
        user = self.find_user(user_id)
        if user:
            return user
        return {'message': 'User not found.'}, 404

    def post(self, user_id):
        dados = User.argumentos.parse_args()
        user_objeto = UserModel(user_id, **dados) 
        novo_user = user_objeto.json() 
        
        users.append(novo_user)
        return novo_user, 200 

    def put(self, user_id):

        dados = User.argumentos.parse_args()
        user_objeto = UserModel(user_id, **dados) 
        novo_user = user_objeto.json()

        user = self.find_user(user_id)

        if user:
            user.update(novo_user)
            return novo_user, 200
        users.append(novo_user)
        return novo_user, 201

    #def delete(self, user_id):
    #    global users 
    #    users = [user for user in users if users['user_id'] != user_id] 
    #    return {'message': 'User deleted'}