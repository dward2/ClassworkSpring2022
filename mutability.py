def work_with_strings():
    print("******* Strings *******")

    words = ["hello", "bye", "tomorrow"]
    print("Initial words: {}".format(words))
    print("The second entry has an id of {}\n".format(id(words[1])))
    
    mod_word = words[1]
    print("Word to mod is {}".format(mod_word))
    print("It has an id of {}\n".format(id(mod_word)))
    
    mod_word = "good" + mod_word
    print("Modified word is {}".format(mod_word))
    print("It has an id of {}\n".format(id(mod_word)))
    
    
    print("Word list is now: {}".format(words))
    print("The second entry has an id of {}\n".format(id(words[1])))
    
    
def work_with_lists():
    print("******* Lists *******")
    lists = [["hello"], ["bye"], ["tomorrow"]]
    print("Initial lists: {}".format(lists))
    print("The second entry has an id of {}\n".format(id(lists[1])))
    
    mod_list = lists[1]
    print("Word to mod is {}".format(mod_list))
    print("It has an id of {}\n".format(id(mod_list)))
    
    mod_list[0] = "good" + mod_list[0]
    print("Modified word is {}".format(mod_list))
    print("It has an id of {}\n".format(id(mod_list)))
    
    
    print("Word list is now: {}".format(lists))
    print("The second entry has an id of {}\n".format(id(lists[1])))


def update_number(a):
    a = a + 2
    
    
def work_numbers():
    b = 5
    update_number(b)
    print(b)


def update_list(a):
    a[0] = a[0] + 2
    a.append("more data")
    
   
def work_lists():
    b = [5]
    update_list(b)
    print(b)

    
if __name__ == "__main__":
    work_with_strings()
    work_with_lists()
    work_numbers()
    work_lists()

    
