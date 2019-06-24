#1
female = []

#2
male = []

#3
user1 = {'username': 'kevin',
         'status': True,
         'first_name': 'kevin',
         'last_name': 'wick',
         'gender': 'male',
         'member': 'FuchiCorp'}

#4
user2 = {'username': 'cutiebun',
         'status': False,
         'first_name': 'Emma',
         'last_name': 'Gipson',
         'gender': 'female',
         'member': 'Apple'}

#5
for m in user1['member'], user2['member']:
    if m == 'FuchiCorp':
        email_list = [user1['first_name'] + '.' + user1['last_name'] + '@member.com']
        user1.update(email = email_list[0])
        print (user1)
    elif m == 'Apple':
        email_list.append(user2['first_name'] + '.' + user2['last_name'] + '@member.com')
        user2.update(email = email_list[1])
        print (user2)
    else:
        print (f'User is not part of {m}')

#6
if 'female' in user1.values():
    female = user1
elif 'female' in user2.values():
    female = user2
else:
    ('Value not in the lists of users')
print (female)


if 'male' in user1.values():
    male = user1
elif 'male' in user2.values():
    male = user2
else:
    ('Value not in the lists of users')
print (male)
