# 🌍 World War History Chat App

A modern AI-powered web application that provides detailed information about World War history using Google's Gemini AI. Built with Streamlit and designed for history enthusiasts, students, and researchers.

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-red.svg)
![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-orange.svg)

## ✨ Features

- 🤖 **AI-Powered Chat**: Interactive conversations about World War history
- 🎯 **Specialized Knowledge**: Focused on World War I & II, causes, and historical context
- ⚙️ **Customizable Parameters**: Adjust temperature, top-p, top-k, and token limits
- 🔒 **Secure API Key Management**: Environment-based configuration
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Modern UI**: Clean, intuitive interface with sidebar controls

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/world-war-chat-app.git
   cd world-war-chat-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

## 📸 Screenshots

### Main Interface
![Main Chat Interface](images/chat-interface.png)

### Sidebar Controls
![Sidebar Configuration](images/sidebar-config.png)

## 🛠️ Configuration

### Model Selection
- **Gemini 2.0 Flash**: Latest model with improved reasoning
- **Gemini 1.5 Flash**: Fast and efficient for quick responses

### Generation Parameters
- **Temperature** (0.0-2.0): Controls randomness in responses
- **Top P** (0.0-1.0): Nucleus sampling parameter
- **Top K** (1-100): Limits vocabulary selection
- **Max Output Tokens** (1-8000): Response length control

## 🏗️ Project Structure

```
world-war-chat-app/
├── app.py                 # Main Streamlit application
├── gemini_basic.ipynb     # Jupyter notebook for testing
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
└── images/               # Screenshots and assets
    ├── chat-interface.png
    └── sidebar-config.png
```

## 🔧 Technical Details

### Built With
- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **Language**: Python 3.13+
- **Environment Management**: python-dotenv
- **Image Processing**: Pillow

### Key Features
- Session state management for chat history
- Cached model initialization for performance
- Error handling and user feedback
- Responsive design with sidebar controls
- Real-time chat interface

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Usage Examples

### Basic Questions
- "What caused World War I?"
- "Explain the Battle of Stalingrad"
- "What was the role of women in World War II?"

### Advanced Queries
- "Compare the strategies of the Axis and Allied powers"
- "How did technology change warfare during WWII?"
- "What were the long-term effects of the Treaty of Versailles?"

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains a valid Gemini API key
   - Check that the key has proper permissions

2. **Import Errors**
   - Make sure you're using the virtual environment
   - Run `pip install -r requirements.txt` again

3. **Streamlit Not Starting**
   - Check if port 8501 is available
   - Try `streamlit run app.py --server.port 8502`

## 📄 Note

This project is for educational purposes and learning demonstration.

## 🙏 Acknowledgments

- Google for providing the Gemini AI API
- Streamlit team for the amazing web framework
- History enthusiasts who inspired this project

## 📞 Contact

Your Name - [@yourusername](https://twitter.com/yourusername) - your.email@example.com

Project Link: [https://github.com/yourusername/world-war-chat-app](https://github.com/yourusername/world-war-chat-app)

---

⭐ **Star this repository if you found it helpful!**
# world-war-chat-app
