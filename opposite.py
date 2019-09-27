msg = "This is a list of cities."
msg_list = msg.split(".")

for word in msg_list:
    print(word)

new_msg = " ".join(msg_list)
print(new_msg)