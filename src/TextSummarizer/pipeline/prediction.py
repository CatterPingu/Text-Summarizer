from TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class Prediction:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()
    #Model evaluation config contains paths to the model and the tokenizer

    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={"length_penalty":0.8,"num_beams":8, "max_length": 128}
        #In the Hugging Face Transformers library, gen_kwargs 
        # is a dictionary of keyword arguments that are passed 
        # to the generate() method of a model. These arguments can 
        # be used to control the generation process, such as the 
        # maximum length of the output, the beam size, and the 
        # temperature.
        
        pipe=pipeline("summarization",model=self.config.model_path,tokenizer=tokenizer)

        print("Dialouge")
        print(text)

        output=pipe(text,**gen_kwargs)[0]["summary_text"]
        print("\n Model Summary")
        print(output)


        return output