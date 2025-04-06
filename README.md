Here’s a well-structured `README.md` file for your Morse Code application. It includes all the necessary sections to provide a comprehensive overview of the project.

---

# Morse Code Translator 

A Python-based Morse Code translator and player built using the `customtkinter` library for the GUI and `pygame` for audio playback. This application allows users to convert text between English and Morse Code, play Morse Code as audio, and clear/reset inputs with ease.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **Bidirectional Translation**: Convert text from English to Morse Code and vice versa.
- **Audio Playback**: Play Morse Code translations as audio using `.mp3` files for dots (`dot.mp3`) and dashes (`dash.mp3`).
- **Interactive GUI**: A user-friendly interface built with `customtkinter` that includes:
  - Input and output text areas.
  - Radio buttons to toggle between translation modes (English → Morse / Morse → English).
  - Buttons for conversion, playback, clearing, and quitting.
- **Morse Code Guide**: View a visual guide for Morse Code symbols via a pop-up window.

---

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Poyamohamadi/morse_code.git
   cd morse_code
   ```

2. Install the required dependencies:
   ```bash
   pip install customtkinter pygame pillow
   ```

3. Place the required audio and image files in the project directory:
   - `dot.mp3`: Sound for a dot (short beep).
   - `dash.mp3`: Sound for a dash (long beep).
   - `morse.png`: Image file for the Morse Code guide.

4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the application by running the script.
2. Enter text in the input box:
   - For **English → Morse Code**, select the corresponding radio button.
   - For **Morse Code → English**, select the other radio button.
3. Click the "Convert" button to translate the text.
4. Use the "Play Morse" button to hear the Morse Code translation as audio.
5. Clear the input/output fields using the "Clear" button.
6. Exit the application by clicking the "Quit" button.

**Note**: Ensure that the `dot.mp3`, `dash.mp3`, and `morse.png` files are present in the working directory for proper functionality.

---

## Structure

The project is organized into a single Python script (`main.py`) with a modular structure. Below is a detailed breakdown of the code and its components:

###  **Imports**
   - **`customtkinter`**: A modern GUI library built on top of Tkinter, used for creating the application's user interface.
   - **`pygame.mixer`**: Handles audio playback for Morse Code sounds (dots and dashes).
   - **`PIL.Image`**: Used to load and display the Morse Code guide image.
   - **`os`**: Provides utilities for interacting with the file system (e.g., loading audio and image files).

### **Class Definition: `MyApp(CTk)`**
   The main application class inherits from `CTk`, which is the base class for `customtkinter` applications. It encapsulates all the functionality of the Morse Code translator.

   #### Key Components:
   - **Initialization (`__init__`)**:
     - Sets up the application window and calls the `run()` method to initialize the GUI.

   - **`run()` Method**:
     - Configures the main application window (title, size, resizability).
     - Defines dictionaries for English-to-Morse and Morse-to-English translations.
     - Creates the layout using frames, textboxes, radio buttons, and buttons for user interaction.

   - **GUI Layout**:
     - **Input Frame**:
       - Contains a `CTkTextbox` for user input.
       - Includes radio buttons to toggle between "English → Morse" and "Morse → English" modes.
       - A "Guide" button opens a pop-up window displaying the Morse Code guide.
     - **Output Frame**:
       - Contains a `CTkTextbox` to display the translated output.
       - Buttons for converting text, playing Morse Code as audio, clearing fields, and quitting the application.

   - **Helper Methods**:
     - **`show_guide()`**:
       - Opens a new window (`CTkToplevel`) displaying the Morse Code guide image (`morse.png`).
     - **`get_morse()`**:
       - Converts English text to Morse Code using the predefined dictionary.
       - Filters out invalid characters and formats the output with spaces and separators (`|`).
     - **`get_english()`**:
       - Converts Morse Code back to English using the reverse dictionary.
       - Handles spaces and separators to reconstruct words.
     - **`convert()`**:
       - Determines the translation direction based on the selected radio button and calls the appropriate conversion method.
     - **`play()`**:
       - Plays the Morse Code translation as audio using `pygame.mixer`.
       - Uses `dot.mp3` for dots and `dash.mp3` for dashes, with pauses for spaces and word separators.
     - **`clear()`**:
       - Clears both the input and output textboxes.

### **Main Execution Block**
   - The script checks if it is being run directly (`if __name__ == "__main__":`) and initializes the `MyApp` class to start the application.

The project is organized as follows:

```
morse_code/
├── main.py               # Main application script
├── README.md             # Project documentation
├── dot.mp3               # Audio file for dots
├── dash.mp3              # Audio file for dashes
├── demo.gif              # Gif documention
└── morse.png             # Morse Code guide image
```

---

## Dependencies

This project relies on the following Python libraries:

- `customtkinter`: Modern GUI toolkit based on Tkinter.
- `pygame`: Used for playing audio files.
- `Pillow`: Handles image loading and display.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request detailing your changes.

Please ensure your code adheres to the existing style and includes appropriate documentation.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Poyamohamadi/Morse_Code/blob/main/LICENSE.md) file for details.

---

## Acknowledgments

- **CustomTkinter Library**: Thanks to the developers of `customtkinter` for creating a modern and customizable GUI toolkit.

- **Python Community**: Special thanks to the Python community for their support and resources.

---

## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: [Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using **Morse Code Translator**! 😊
