class User:
    def __init__(self, user_id, user_name) -> None:
        print("Inicialize called")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1 # o usuario que esta sendo passado, quando um follower. Estou modificando o atributo do objeto que esta sendo passado
        self.following += 1 # eu estou seguindo mais um. Estou modificando o meu objeto, por isso self. Ou seja, modificando o objeto que chamou o metodo

user_1 = User('001', 'Noberto')
user_2 = User('002', 'Jorge')

user_1.follow(user_2)
print()