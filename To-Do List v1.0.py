import json, os


list_name = ""
list_date = ""
item_1 = ""

data = {
        "List name": list_name,
        "Date due to": list_date,
        "Shopping List": ["item1", "item2", "item3"]
            }



def dump():
    try:
        dump_search = input("Dump Filename: ")
        with open(dump_search + ".json", "r") as file:
            # Loads JSON data from the file
            current_data = json.load(file)
            json_string = json.dumps(current_data, indent=4)
            print(json_string)
            print()
    except FileNotFoundError:
        print(f"Couldn't find '{dump_search}', file not found. Please save data first.")
        print()
    except json.JSONDecodeError:
        print(f"Error: '{dump_search}' contains invalid JSON.")
        print()


print("""
This code has been written by: UH4X.
      Original Github Repository: https://github.com/UH4X/ToDo-List
""")

while True:
    try:
        command = input("Command: ").lower()
        print()



        if command == "help":
            print("""
                  
        Welcome to the help section!
                  
                  1. "help"
                  2. To exit write: "Breakk", "Exit", "Stop" or "Quit".
                  3. "Dump"

            """)
            


        elif command in ["break", "exit", "stop", "quit"]:
            exit()

        
        elif command == "edit":
            while True:
                try:
                    editor = input("Editor: ").lower()
                    print()

                    if editor == "help":
                        print("""
                  
Welcome to Editoring help section!
                  
                  1. "New" - Creates a new file.
                  2. "Name" - Changes the list name.
                  3. "Date" - Set what date your list is for.
                  4. "Item(number)" - An item you need.
                  5. "Dump" - Searches and dumps file info in terminal.
                  6. "Del" - Deletes a file.

""")


                    elif editor == "new":
                            print("Do not include the .json.")
                            create = input("New file(name): ")
                            with open(create + ".json", "w") as file:
                                json.dump(data, file, indent=4)

                    elif editor == "name":
                        print()
                        user_list = input("Choose list: ")

                        with open(user_list + ".json", "r") as file:
                            data = json.load(file)
                            print("File located")
                            print()

                            name = input("New list name: ")
                            data["List name"] = name
                            with open(user_list + ".json", "w") as file:
                                json.dump(data, file, indent=4)


                    elif editor == "date":
                        print()
                        user_list = input("Choose list: ")

                        with open(user_list + ".json", "r") as file:
                            data = json.load(file)
                            print("File located")
                            print()

                            date = input("Date Due To: ")
                            data["Date due to"] = date
                            with open(user_list + ".json", "w") as file:
                                json.dump(data, file, indent=4)


                    elif editor == "item":
                        print()
                        user_list = input("Choose list: ")

                        with open(user_list + ".json", "r") as file:
                            data = json.load(file)
                            print("File located")
                            print()

                            print("Item 1, 2 or 3?")
                            print("NUMBERS ONLY!!")
                            
                            
                            item_num = int(input("Item number: ")) -1
                            
                            print()

                            print("Your item you want added:")
                            new_item = input("New item: ")
                            data["Shopping List"][item_num] = new_item

                            

                            with open(user_list + ".json", "w") as file:
                                json.dump(data, file, indent=4)

                    elif editor == "dump":
                        dump()

                
                    elif editor == "del":
                         print()
                         user_list = input("Enter the name of the file to delete (without .json): ")

                         if os.path.exists(user_list + ".json"):
                            confirm = input(f"Are you sure you want to delete {user_list}.json? (yes/no): ").lower()
                            if confirm == "yes":
                                os.remove(user_list + ".json")
                                print(f"{user_list}.json has been deleted successfully!")
                            else:
                                print("File deletion aborted.")
                         else:
                            print(f"File {user_list}.json does not exist!")

                        
                           
                            


                        

                    

                except KeyboardInterrupt:
                    print("Keyboard has been interrrupted.")
                    exit()

                except FileNotFoundError:
                    print("File does not exist. Please try again...")
                    print()


    except ValueError:
        print("Error: ValueError")







