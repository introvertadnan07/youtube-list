import json

DATA_FILE = 'youtube.txt'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []  # Ensure it's always a list
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_data(videos):
    with open(DATA_FILE, 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    if not videos:
        print("No videos available.")
        return
    print("\nList of YouTube Videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")

def add_video(videos):
    if videos is None:  # Safety check
        videos = []
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("Video added successfully.")

def update_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            videos[index]['name'] = input("Enter new video name: ") or videos[index]['name']
            videos[index]['time'] = input("Enter new video time: ") or videos[index]['time']  
            save_data(videos)
            print("Video updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter video number to delete: ")) - 1
        
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data(videos)
            print(f"Deleted: {deleted_video['name']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting YouTube Manager.")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()