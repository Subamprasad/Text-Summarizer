from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    
    def predict(self,text):
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            model_path = self.config.model_path
        except Exception:
            # Fallback to base model if artifacts are missing
            tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
            model_path = "google/pegasus-cnn_dailymail"

        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output.replace("<n>", "\n")
