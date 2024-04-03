try:
    #Create the file
    with open("my_file.txt", 'w') as file:
        file.write("My name is Ben.\n")
        file.write("I am a 23 year old.\n")
        file.write("I am hoping to be good at Python, someday.\n")

    #reading and displaying the file
    print("Contents of my file:")
    with open("my_file.txt", 'r') as file:
        for line in file:
            print(line.strip())

    # Appending
    with open("my_file.txt", 'a') as file:
        file.write("I am currently at PLP.\n")
        file.write("The experience so far is good. \n")
        file.write("Looking forward to learn so much! \n")

    print("Contents of appended file:")
    with open("my_file.txt", 'r') as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("Execution completed.")
