# Nitzagram 📱

## Overview
**Nitzagram** is a Python-based project that simulates a social media platform. It uses the Pygame library to create a graphical interface where users can interact with posts, add likes, and leave comments. The project supports two types of posts: image posts and text posts. 🖼️ 💬

## Project Structure 📁
```
nitzagram
|
|-- main.py           # Entry point for the application
|-- constants.py      # Configuration file containing constants for UI and layout
|-- helpers.py        # Utility functions for the project
|
|-- /classes
|   |-- post.py       # Base class for posts
|   |-- imagepost.py  # Subclass for image posts
|   |-- textpost.py   # Subclass for text posts
|
|-- /Images           # Directory for post images (e.g., 'ronaldo.jpg', 'noa_kirel.jpg')
```

## Getting Started 🚀

### Prerequisites
- Python 3.8+
- Pygame 2.0+

### Installation Steps ⚙️
1. **Install Dependencies**
   ```bash
   pip install pygame
   ```

2. **Prepare Assets**
   Place all required images in the `Images` directory. The filenames should match those specified in the code (e.g., `ronaldo.jpg`, `noa_kirel.jpg`).

3. **Run the Program**
   ```bash
   python main.py
   ```

## Features ✨
- **Dynamic Post Display** 🔄: Toggle between posts by interacting with the interface
- **Like System** ❤️: Click the like button to add likes to posts
- **Commenting System** 💭: Add comments to posts dynamically
- **Support for Multiple Post Types** 🖼️: Display both image and text-based posts with unique styles

## Core Components 🛠️

### Main Components
- `main.py`: Application entry point and main loop handler
- `constants.py`: UI configuration and layout settings
- `/classes/post.py`: Base post functionality implementation
- `/classes/imagepost.py`: Image post handling and rendering
- `/classes/textpost.py`: Text post styling and display
- `helpers.py`: Utility functions for the application

### User Interaction Guide 🎮
- **Navigate**: Use the `Next Post` button to cycle through posts
- **Like**: Click the `Like` button to increment the like counter
- **Comment**: Use the `Comment` button to add comments to the current post

## Future Roadmap 🎯
- User authentication system 🔐
- Video post support 🎥
- Persistent storage for user interactions 💾
- Enhanced social features (sharing, tagging) 🤝

## Contributing 🤝
Contributions are welcome! Feel free to submit issues and pull requests.

## License 📄
This project is open-source and available under the MIT License.

---

## Support 💪
For support, please open an issue in the GitHub repository or contact the maintainers.

Made with ❤️ using Python and Pygame