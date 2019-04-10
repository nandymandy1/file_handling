# Open File

# File Objects
"""
To Open a file
"""
# f = open('text.txt', 'r')

'''
To Write to a file
'''
# f = open('text.txt', 'w')

'''
To Append to a file
f = open('text.txt', 'a')
To Read and Write to a file
f = open('text.txt', 'r+')
'''

# To get the name of the file
# print(f.name)
# print(f.mode)
# f.close()

# USING CONTEXT MANAGER
with open('text.txt', 'r') as f:
    # f_contents = f.read()
    # print(f_contents)
    # f_contents = f.readlines()
    # print(f_contents)
    # f_content = f.readline()
    # print(f_content, end="")
    # f_content = f.readline()
    # print(f_content, end="")
    # f_content = f.readline()
    # print(f_content, end="")
    # f_content = f.readline()
    # print(f_content, end="")

    # for line in f:
    #     print(line, end="")

    # f_contents = f.read(100)
    # print(f_contents)
    # f_contents = f.read(100)
    # print(f_contents)
    # size_to_read = 100
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end="")
    #     f_contents = f.read(size_to_read)
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)
