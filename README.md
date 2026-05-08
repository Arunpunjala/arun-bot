This project is a simple AI chatbot that generates responses based on user input, while also considering the sentiment of the message. It uses a transformer-based model to produce empathetic or normal replies.

🚀 Features
Uses FLAN-T5 (google/flan-t5-small) for text generation
Performs sentiment analysis on user input
Adjusts response tone:
Negative → empathetic reply
Neutral/Positive → normal reply
Built with Hugging Face Transformers
🧠 How It Works
User provides input
Sentiment is analyzed using a prebuilt pipeline
Based on sentiment:
Negative → prompt is modified to be empathetic
Otherwise → standard response
Input is tokenized and passed to the model
Model generates a response