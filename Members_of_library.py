    

member_list = []
checkbox_to_go_further = []
def register_names():   
    not_stop = True
    
    while not_stop:
        add_to_member_list = input("Type your name to become a member of the library.\n~").title()
        member_list.append(add_to_member_list)
        shall_continue = input("Want to register another student as a member? Type y/n ").lower()
        if shall_continue== 'y':
            pass
        elif shall_continue== 'n':
            not_stop= False
        else:
            print("**Input Error**")
            not_stop= False
    
    

class MembersCheck:
    def __init__(self,username):
        self.username = username
    
    
    def check(self):
        
            
            if len(member_list) ==1 :
                print(f"Welcome in the virtual library, {member_list[0]}!")
                

            else:
                print("The registered members are:")
                for names in member_list:
                    print(f"~{names}")
                greet = input("Which one of the following members is here to lend a book ?").title().strip()

                for item in member_list:
                
                    if item == greet:
                        print(f"Welcome in the virtual library, {item}!")
                        checkbox_to_go_further.append('y')
                        break
                    
                else:
                    print("Sorry but that name was not registered as a member in the virtual library.")
                    
                    

                        
                    
                
                
            
