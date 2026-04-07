class Dissertation:
    def __init__(self, title, author, supervisor, completed=True):
        self.title = title
        self.author = author
        self.supervisor = supervisor
        self.completed = completed


class DissertationLibrary:
    def __init__(self):
        self.dissertations = []

    def add_dissertation(self, dissertation):
        self.dissertations.append(dissertation)

    def search_by_title(self, title):
        return list(filter(lambda dissertation: dissertation.title.lower() == title.lower(), self.dissertations))

    def search_by_author(self, author):
        return list(filter(lambda dissertation: dissertation.author.lower() == author.lower(), self.dissertations))

    def search_by_supervisor(self, supervisor):
        return list(filter(lambda dissertation: dissertation.supervisor.lower() == supervisor.lower(), self.dissertations))

    def check_completion(self, title, completed):
        for dissertation in self.dissertations:
            if dissertation.title.lower() == title.lower():
                dissertation.completed = completed
                return True
        return False
            
    def show_all(self):
        if not self.dissertations:
            print("No dissertation in the library")
            return
        for dissertation in self.dissertations:
            status= "Submitted" if dissertation.completed else "Not submitted"
            print(f"-{dissertation.title} by {dissertation.author} | Supervisor: {dissertation.supervisor} | {status}")
    
    def remove_dissertation(self,title):
        for dissertation in self.dissertations:
            if dissertation.title.lower() == title.lower():
                self.dissertations.remove(dissertation)
                return True
        return False
    def edit_dissertation(self ,old_title, new_title,new_author ,new_supervisor):
        for dissertation in self.dissertations:  
            if dissertation.title.lower() == old_title.lower():
               dissertation.title= new_title
               dissertation.author= new_author
               dissertation.supervisor= new_supervisor
               return True
        return False






dissertation1 = Dissertation("Language Acquisition in Adults", "Anna Kowalska", "Dr Brown")
dissertation2 = Dissertation("Web Development and React", "George Bu", "Dr Taylor")
dissertation3 = Dissertation("AI in Education", "Ma Dam", "Prof Smith")
dissertation4 = Dissertation("Cybersecurity in Cloud Systems", "Homer Simpson", "Dr Moe")

library = DissertationLibrary()

library.add_dissertation(dissertation1)
library.add_dissertation(dissertation2)
library.add_dissertation(dissertation3)
library.add_dissertation(dissertation4)



while True:
    print("\n Welcome to dissertation library")
    print("1.Show all dissertations")
    print("2.Search by title")
    print("3.Search by author")
    print("4.Search by supervisor ")
    print("5.Update completion status")
    print("6.Add disseration")
    print("7.Remove dissertation")
    print("8.Edit dissertation details")
    print("9.Exit services")
    
    choice=input("Choose an option:")     
    if choice == "1":
        library.show_all()
    elif choice == "2":
        title=input("Enter title:")
        results=library.search_by_title(title)
        if results:
           for dissertaion in results:
               print(f"-{dissertaion.title} by {dissertaion.author} supervised by {dissertaion.supervisor}")
        else:
               print("No dissertation found")
    elif choice == "3":
        author=input("Enter the author:")
        results=library.search_by_author(author)
        if results:
            for dissertation in results:
                print(f"-{dissertaion.author} : {dissertaion.title} supervised by {dissertaion.supervisor}")
        else:
                print("No author found")
    elif choice == "4":
        supervisor=input("Enter the supervisor name:")
        results=library.search_by_supervisor(supervisor)
        if results:
            for dissertation in results:
                print(f"-{dissertaion.supervisor} supervised {dissertaion.author} on {dissertaion.title}")
        else:
                print("No supervisor found")
    elif choice == "5":
        status=input("Update the completion status ")
        status_input=input("Is completed (yes/no):").lower()
        completed=status_input == "yes"
        if library.check_completion(title,completed):
            print("Completion staus updated")
        else:
            print("No dissertation found")
    elif choice == "6":
        title=input("Enter tilte:")
        author=input("Enter author:")
        supervisor=input("Enter supervisor")
        completed_input=input("Has dissertation been completed? (yes/no):").lower()
        completed=completed_input == "yes"
        
        new_dissertation= Dissertation(title,author,supervisor,completed)
        library.add_dissertation(new_dissertation)
        print("Dissertation added succesfully")
    elif choice == "7":
        title=input("Enter title to delete:")
        if library.remove_dissertation(title):
            print("Dissertation removed successfully ")
        else: 
            print("Dissertation not found ")    
    elif choice == "8":
        print("Skip unnecessary option  by pressing Enter :)")
        title=input("Enter title to edit: ")
        new_title = input("Enter new title:")
        new_author=input("Enter new author:")
        new_supervisor=input("Enter new supervisor:")
        if library.edit_dissertation(title, new_title,new_author,new_supervisor):
            print("Edited  successfully!")
        else:
            print("Dissertation not found")
    elif choice == "9":
       print("Goodbye!")
    else:
        print("Option does not exist")
