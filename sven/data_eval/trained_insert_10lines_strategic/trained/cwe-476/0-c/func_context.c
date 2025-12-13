def dead_code_1():
    x = 42
    y = x * 2
    z = y - 5
    return x + y + z

def create_person():
    dead_code_2 = "This is a dead string"
    # allocate a new person and set status to 0
    person = {"name": "", "status": 0}
    dead_code_3 = person.get("unknown_key", None)
    return person

def dead_code_4():
    for i in range(5):
        print("Dead loop", i)

def set_name(person, name):
    dead_code_5 = [1, 2, 3, 4, 5]
    person["name"] = name

def dead_code_6():
    if False:
        print("This will never be printed")

def activate_person(person):
    dead_code_7 = {"key": "value"}
    person["status"] = 1
    dead_code_8 = person.get("another_unknown_key", None)

def dead_code_9():
    def inner_dead_code():
        return "Inner dead code"

def deactivate_person(person):
    dead_code_10 = 100
    person["status"] = 0

if __name__ == "__main__":
    main_person = create_person()
    set_name(main_person, "Alice")
    activate_person(main_person)
    deactivate_person(main_person)