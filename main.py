file_path = "/etc/gdm/custom.conf"

def select_file_path(file_path):
    print("Default file path is:", file_path)
    print("[1] - Use default file path")
    print("[2] - Change file path")
    choice = int(input("> "))
    if(choice == 2):
        return input("new file path: ")
    return file_path
    

print("Select your option:")
print("[1] - Nvidia")
print("[2] - Integrated")
print("[0] - Leave")

choice = int(input("> "))

file_path = select_file_path(file_path)

lines = []


with open(file_path, 'r') as file:
    lines = file.readlines()

if choice == 0:
    exit()

choice_string =  "nvidia" if choice == 1 else "integrated"

for i, line in enumerate(lines):
    if "WaylandEnable=false" in line:
        if choice == 1:
            lines[i] = "WaylandEnable=false\n"
        elif choice == 2:
            lines[i] = "#WaylandEnable=false\n"

with open(file_path, 'w') as file:
    file.writelines(lines)

print("Changed config settings")
print("Use command sudo systemctl restart gdm")
print("Use command optimus-manager --switch", choice_string)
if choice == 2:
    print("Reboot")

