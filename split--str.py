# splitting strings
msg = "It is a good day!"
msg_list = msg.split()

for word in msg_list:
    print(word)

# Split with delimiter
msg = """This is an example of using a period. There are three sentences here. The entire sentence will be one item in the list."""
msg_list = msg.split(".")

for sentence in msg_list:
    print(sentence)