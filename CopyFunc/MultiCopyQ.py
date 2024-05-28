
#V2
import keyboard
import clipboard
import time
import os

# Path to save the text file
file_path = 'copied_text.txt'

def main():
    # Clear the content of the text file at the start of the script
    with open(file_path, 'w') as file:
        file.write('')  # Clear the file

    print("Instructions:")
    print("1. Manually select and copy text to the clipboard (Ctrl+C).")
    print("2. Press 'c' to append the copied text to the file.")
    print("3. Repeat as necessary.")
    print("4. Press 'q' to copy the contents of the file to the clipboard.")

    while True:
        # Block until 'c' or 'q' is pressed
        event = keyboard.read_event()

        if event.name == 'c' and event.event_type == 'down':
            # Read text from clipboard
            time.sleep(0.2)  # Delay to ensure clipboard content is ready
            text = clipboard.paste()

            # Append the text to the file
            with open(file_path, 'a') as file:
                file.write(text + '\n')
            
            print("Text copied! Continue or press 'q' to finish.")
        
        elif event.name == 'q' and event.event_type == 'down':
            # If 'q' is pressed, copy the contents of the text file to the clipboard
            with open(file_path, 'r') as file:
                file_content = file.read()
            clipboard.copy(file_content)
            print("Contents of the file have been copied to the clipboard.")
            break
    
    # Optionally, you could also open the clipboard data in an editor, if needed
    # os.startfile(file_path)  # This line is no longer needed if you just want to copy to clipboard

if __name__ == "__main__":
    main()