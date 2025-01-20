# Nitzagram

## Overview
**Nitzagram** is a Python-based project that simulates a social media platform. It uses the Pygame library to create a graphical interface where users can interact with posts, add likes, and leave comments. The project supports two types of posts: image posts and text posts.

---

## Project Structure
```
nitzagram
|
|-- main.py           # Entry point for the application
|-- constants.py      # Configuration file containing constants for UI and layout
|
|-- /classes
|   |-- post.py       # Base class for posts
|   |-- imagepost.py  # Subclass for image posts
|   |-- textpost.py   # Subclass for text posts
|
|-- /Images           # Directory for post images (e.g., 'ronaldo.jpg', 'noa_kirel.jpg')
|
|-- /helpers
    |-- helpers.py    # Utility functions for the project
```

---

## How to Run the Project
1. **Install Dependencies**
   Ensure you have Python installed along with the Pygame library:
   ```bash
   pip install pygame
   ```

2. **Prepare Assets**
   Place all required images in the `Images` directory. The filenames should match those specified in the code (e.g., `ronaldo.jpg`, `noa_kirel.jpg`).

3. **Run the Program**
   Execute the main script:
   ```bash
   python main.py
   ```

---

## Features
- **Dynamic Post Display**: Toggle between posts by interacting with the interface.
- **Like System**: Click the like button to add likes to posts.
- **Commenting System**: Add comments to posts dynamically.
- **Support for Multiple Post Types**: Display both image and text-based posts with unique styles.

---

## Code Components

### 1. `main.py`
Handles the main loop, user interaction, and rendering. It initializes the Pygame environment, sets up the background, and manages the event loop for user inputs.

### 2. `constants.py`
Defines constants for window dimensions, button positions, font sizes, and colors, ensuring a centralized configuration for the UI.

### 3. `/classes/post.py`
The base `Post` class implements shared functionality for all post types:
- Adding likes and comments.
- Displaying metadata (username, location, description).
- Rendering comments dynamically.

### 4. `/classes/imagepost.py`
Inherits from `Post` and adds functionality for displaying an image-based post. Images are loaded, scaled, and rendered on the screen.

### 5. `/classes/textpost.py`
Inherits from `Post` and adds functionality for text-based posts. Includes methods for rendering a styled background and the post's text.

### 6. `/helpers/helpers.py`
Contains utility functions such as button click detection and text alignment.

---

## User Interaction
- **Navigation**: Use the `Next Post` button to cycle through posts.
- **Likes**: Click the `Like` button to increment the like counter.
- **Comments**: Use the `Comment` button to add comments to the current post.

---

## Dependencies
- Python 3.8+
- Pygame 2.0+

---

## Future Improvements
- Add user authentication to personalize posts.
- Implement video post support.
- Enable persistent storage for likes and comments.
- Expand the interface with more interactive features (e.g., sharing, tagging).

---

## License
This project is open-source and available under the MIT License.
