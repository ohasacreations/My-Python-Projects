import datetime
members = []

n = int(input("Enter number of members: "))

# Input details

for i in range(n):
    print(f"\nEnter details for member {i+1}:")
    name = input("Name: ")
    member_id = input("Member ID: ")
    projects = int(input("Completed Projects: "))
    score = float(input("Total Score: "))

    member = {
        "name": name,
        "id": member_id,
        "projects": projects,
        "score": score
    }

    members.append(member)

# Menu Loop 
while True:
    print("\n===== Student Management System =====")
    print("1. Display all members")
    print("2. Search a member by ID")
    print("3. Display the member with the highest score")
    print("4. Sort members by total score (descending)")
    print('''5. Save all data to a file named "members.txt" ''')
    print("6. Exit")


    user_input=int(input("Select What you want: "))


# Display All
    if(user_input==1):
        for m in members:
            print(f"ID: {m['id']}, Name:{m['name']}, Projects{m['projects']},Score{m['score']}")

# Search by ID
    elif(user_input==2):
        search_id = input("Enter Member ID to search: ")
        found = False
        for m in members:
            if m["id"] == search_id:
                print(f"Found → Name: {m['name']}, Projects: {m['projects']}, Score: {m['score']}")
                found = True
                break
        if not found:
            print("No member found with that ID")

# Highest score
    elif(user_input==3):
        top=max(members,key= lambda m:m["score"])
        print(f"\nHighest Scorer → {top['name']} ({top['id']}) - {top['score']}")

#Sort by score
    elif (user_input==4):
        members.sort(key=lambda m: m["score"], reverse=True)
        print("\nMembers sorted by total score (highest first).")

# Save to file
    elif (user_input==5):
        file=open("members.txt","w")
        for m in members:
            file.write("=====================================\n")
            file.write((f"ID: {m['id']}, Name: {m['name']}, Projects: {m['projects']}, Score: {m['score']}\n"))
            file.write("=====================================\n")

        print(" Data saved to members.txt successfully!")
# Exit
    elif(user_input==6):
        print("Exiting program... Bye bye")
        break
    else:
        print("Please enter a valid number")

