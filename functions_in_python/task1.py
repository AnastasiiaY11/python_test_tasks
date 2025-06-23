def format_name(name, title="Mr./Ms."):
    # Find first space in the name
    space_index = name.find(" ")
    # If space found, take substring up to space, otherwise use whole name
    first_name = name[:space_index] if space_index != -1 else name
    return f"Title: {title}, Name: {first_name}"


print(format_name("Alice"))
print(format_name("John Smith", "Dr."))
print(format_name("Alice Johnson"))