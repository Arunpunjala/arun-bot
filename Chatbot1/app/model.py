from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM, pipeline

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

sentiment = pipeline("sentiment-analysis")

def generate_response(user_input):

    sentiment_result = sentiment(user_input)[0]

    if sentiment_result["label"] == "NEGATIVE":
        prompt = f"The user feels sad. Reply empathetically: {user_input}"
    else:
        prompt = f"Reply normally: {user_input}"

    input_ids = tokenizer.encode(
        prompt,
        return_tensors="tf",
        truncation=True
    )

    output = model.generate(input_ids, max_length=150)

    return tokenizer.decode(output[0], skip_special_tokens=True)