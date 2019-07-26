from project.plant_list import add_new_plant
from project.plant_list import print_list
from project.plant_list import delete_from_list
import time


def choice(list_of_plants):
    while True:
        print_list(list_of_plants)
        answer = input("Would you like to add a new plant or delete some? (add/delete/exit): ")
        if answer == "add":
            add_new_plant(list_of_plants)
        elif answer == "delete":
            if not list_of_plants:
                print("You have no plants saved (nothing to delete).")
                time.sleep(1)
            else:
                delete_plant(list_of_plants)
        elif answer == "exit":
            print("Thank you for using Plantopedia")
            break
        else:
            print("Wrong input")
            continue


def delete_plant(list_of_plants):
    while True:
        if not list_of_plants:
            print("You have no plants saved (nothing to delete).")
            time.sleep(1)
            break
        else:
            answer = input("Enter the plant's common name or exit: ")
            if answer != "exit":
                result = delete_from_list(list_of_plants, answer)
                if result:
                    print("{to_delete} successfully deleted." .format(to_delete=answer))
                    print_list(list_of_plants)
                else:
                    print("{to_delete} not found in Plantopedia".format(to_delete=answer))
                time.sleep(2)
            else:
                break
