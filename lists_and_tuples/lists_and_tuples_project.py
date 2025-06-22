playlist = [
    ("Bohemian Rhapsody", "Queen", 355),
    ("Stairway to Heaven", "Led Zeppelin", 482),
    ("Hotel California", "Eagles", 390)
]

while True:
    print("\n===== Playlist Manager =====")
    print("1. Add a song")
    print("2. Show playlist")
    print("3. Sort playlist")
    print("4. Show statistics")
    print("5. Exit")
    print("==========================")
    
    choice = input("Enter your choice (1-5): ")

    # --- 1. Add a song ---
    if choice == '1':
        print("\nAdding a new song...")
        try:
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            duration_str = input("Enter song duration in seconds: ")
            duration = int(duration_str)

            # A song is stored as a tuple
            song = (title, artist, duration)
            playlist.append(song)
            print(f"\nSuccessfully added '{title}' by {artist} to the playlist.")
        except ValueError:
            print("\nInvalid input. Duration must be a whole number. Please try again.")

    # --- 2. Show playlist ---
    elif choice == '2':
        print("\n--- Current Playlist ---")
        if not playlist:
            print("The playlist is currently empty.")
        else:
            for i, song in enumerate(playlist, 1):
                # Unpack the tuple for display
                title, artist, duration = song
                minutes = duration // 60
                seconds = duration % 60
                print(f"{i}. '{title}' by {artist} ({minutes:02d}:{seconds:02d})")
        print("------------------------")

    # --- 3. Sort playlist ---
    elif choice == '3':
        if not playlist:
            print("\nCannot sort an empty playlist.")
        else:
            print("\nSort playlist by:")
            print("1. Title")
            print("2. Artist")
            print("3. Duration")
            sort_choice = input("Enter your choice (1-3): ")

            if sort_choice == '1':
                # Sort by title (the first item in the tuple)
                playlist.sort(key=lambda s: s[0].lower())
                print("\nPlaylist sorted by title.")
            elif sort_choice == '2':
                # Sort by artist (the second item in the tuple)
                playlist.sort(key=lambda s: s[1].lower())
                print("\nPlaylist sorted by artist.")
            elif sort_choice == '3':
                # Sort by duration (the third item in the tuple)
                playlist.sort(key=lambda s: s[2])
                print("\nPlaylist sorted by duration.")
            else:
                print("\nInvalid choice.")
            
            # Show the playlist after sorting
            print("\n--- Sorted Playlist ---")
            for i, song in enumerate(playlist, 1):
                title, artist, duration = song
                minutes = duration // 60
                seconds = duration % 60
                print(f"{i}. '{title}' by {artist} ({minutes:02d}:{seconds:02d})")
            print("-----------------------")

    # --- 4. Show statistics ---
    elif choice == '4':
        if not playlist:
            print("\nNo statistics to show for an empty playlist.")
        else:
            total_songs = len(playlist)
            
            # Calculate total duration with a simple loop
            total_duration_seconds = 0
            for song in playlist:
                total_duration_seconds += song[2] # Add the duration

            # Format the total duration for display
            minutes, seconds = divmod(total_duration_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            print("\n--- Playlist Statistics ---")
            print(f"Total number of songs: {total_songs}")
            print(f"Total playlist duration: {hours}h {minutes}m {seconds}s")
            print("---------------------------")

    # --- 5. Exit ---
    elif choice == '5':
        print("Exiting playlist manager. Goodbye!")
        break

    # --- Handle invalid input ---
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")