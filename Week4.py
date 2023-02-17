usernames = ['Admin', 'Joshuakitts11', 'Joshuakitts2001', 'Akittsy', 'Gizmo']

for i in usernames:

    if i == "Admin":
        print ("Hello " + i + ", would you like to see a status report?\n")

    else:
        print ("Hello " + i + ", thank you for logging in again\n")


while usernames:
    username = usernames.pop()
    print(username)

print(usernames)

if len(usernames) != 0:
    print("Not Empty")

else:
    print("Empty List")
