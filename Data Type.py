from unicodedata import name

Name = input("Your Name, Agent:")
gadget = input("Your Gadget, Agent:")

Agent_Number = 7
speed_rating = 9.5
mission_count = 5
height = 1.65
is_active = True

print("Name:", Name, "-> type:", type(Name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("Agent Number:", Agent_Number, "-> type:", type(Agent_Number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("Mission Count:", mission_count, "-> type:", type(mission_count))
print("Height:", height, "-> type:", type(height))
print("Is Active:", is_active, "-> type:", type(is_active))

Agent_Number_Text = str(Agent_Number)
Mission_Count_Text = str(mission_count)
Speed_Rating_Text = str(speed_rating)
status_text = str(is_active)

print("Agent Number as text:", Agent_Number_Text, "-> type:", type(Agent_Number_Text))
print("Mission Count as text:", Mission_Count_Text, "-> type:", type(Mission_Count_Text))
print("Speed Rating as text:", Speed_Rating_Text, "-> type:", type(Speed_Rating_Text))
print("Status as text:", status_text, "-> type:", type(status_text))

first_three = Name[0:3]
last_letter = Name[-1:]
code_name = first_three + last_letter

print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Code name:", code_name)

if is_active:
    print("Mission status: Active")
else:
    print("Mission status: Inactive")
