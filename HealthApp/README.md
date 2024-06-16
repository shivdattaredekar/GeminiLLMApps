# Google Gemini Health App

Google Gemini Health App is a Streamlit application that allows users to interact with images of meals by uploading photos and receiving detailed calorie information for the meals. The application leverages Google's Gemini Pro Vision model for image processing and calorie estimation.

https://github.com/shivdattaredekar/GeminiLLMApps/assets/46707992/acb0cab3-79f4-4b98-99c8-be2da4b6e20d

## Features

- **Upload Meal Images**: Users can upload images of their meals.
- **Calorie Estimation**: The app estimates the total calorie content and provides a breakdown of calories for individual items in the meal.
- **Responsive Design**: User-friendly interface that works well on both mobile and desktop.

## Installation

### Prerequisites

- Python 3.10
- Streamlit
- Google Generative AI package
- Pillow (PIL) for image processing

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/gemini-health-app.git
    cd gemini-health-app
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Interact with the app:
    - **Upload Image**: Upload images of your meals.
    - **Get Calorie Information**: Click the "Get the information about the Meal" button to process the image and receive calorie details.

## Code Overview

### `app.py`

- **Main script**: Sets up the Streamlit interface and handles user interactions.

### `get_response(input, image, prompt)`

- **Function to get response**: Sends input and image data to the Gemini Pro Vision model and returns the response.

### `input_image_setup(uploaded_file)`

- **Image processing**: Converts uploaded images to bytes for model processing.

### Dependencies

- Python 3.7+
- Streamlit
- Google Generative AI
- Pillow (PIL)
- dotenv

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Google**: For providing the Generative AI services
- **Streamlit**: For the web application framework

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

If you have any questions or feedback, feel free to reach out to me at [shivdattaredekar@gmail.com].
