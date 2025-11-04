name = input("Enter your name: ")

print(f"As entered: '{name}'")

stripped_name = name.strip()
print(f"After strip(): '{stripped_name}'")

lstripped_name = name.lstrip()
print(f"After lstrip(): '{lstripped_name}'")

rstripped_name = name.rstrip()
print(f"After rstrip(): '{rstripped_name}'")