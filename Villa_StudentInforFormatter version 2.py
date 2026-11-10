first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section:")
favorite_subject = input("Enter favorite subject: ")

full_name = first_name + " " + last_name
formatted_name = full_name.title()
uppercase_name = full_name.upper()
uppercase_section = section.upper()
formatted_subject = favorite_subject.title()
char_count = len(full_name)

print("\nFormatted Output:")
print("Name: " + formatted_name)
print("Name Code: " + uppercase_name)
print("Section: " + uppercase_section)
print("Favorite Subject: " + formatted_subject)
print("Character Count: " + str(char_count))