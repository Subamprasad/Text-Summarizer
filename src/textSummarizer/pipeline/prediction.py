from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            self.model_path = self.config.model_path
        except Exception:
            # Fallback to base model if artifacts are missing
            self.tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
            self.model_path = "google/pegasus-cnn_dailymail"

    
    def predict(self,text):
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.model_path,tokenizer=self.tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output.replace("<n>", "\n")
