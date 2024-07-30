from Linked_list import LinkedList
from Node import Node 
def main():
    songs = LinkedList()
    user_choice = " "
    FINISHED = False
    while (not(FINISHED)):
        print("1. press 1 to add a song\n press 2 to display the list of songs")
        print("Press 3 to display the number of songs.\n press 4 to delete a song \n 9 to exit")
        user_choice = int(input("Enter a song choice: "))
        if user_choice == 1:
            song_title = input("Enter the title of the new song to add: ")
            new_song_object = Node(song_title)
            songs.insert(new_song_object)
        elif user_choice == 2:
            songs.display()
        elif user_choice == 3:
            print(songs.item_counts(), " songs in your album")
        elif user_choice == 4:
            title_of_song_to_delete = input("Enter the title of the song to delete: ")
            title_of_song_to_delete = title_of_song_to_delete.lower()
            songs.delete(title_of_song_to_delete)
        elif user_choice == 9:
            print("We are done!")
            FINISHED = True 
        else:
            print("not found")
