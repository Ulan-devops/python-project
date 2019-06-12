#1
github_users = []

#2
user_emma = {'username': 'emma-11', 'firstname': 'Emma', 'lastname': 'Lopes', 'password' : 'redhat' }
print (user_emma)
#3
user_smith = dict.fromkeys(user_emma)
user_smith.update(username = 'frank', firstname = 'Frank', lastname = 'Smith', password = 'frank2019')
print (user_smith)

#4
github_users.append(user_emma)
github_users.append(user_smith)
print(github_users)
 
