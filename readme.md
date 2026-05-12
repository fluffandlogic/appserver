Steps
---

# Create a users table
id
first name
last name
email
active

# user_logins table
id
user_id
datetime
is_successful
foreign key (user_id) references users(id)# appserver
