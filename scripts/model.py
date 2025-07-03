import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Text2SQLGenerator:
    def __init__(self, model_name="XGenerationLab/XiYanSQL-QwenCoder-3B-2502"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = model_name
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        print(self.model.device)

    def generate_response(self, prompt, max_new_tokens=1024, temperature=0.1, top_p=0.8):
        # Crear el mensaje en el formato esperado
        message = [{'role': 'user', 'content': prompt}]
        text = self.tokenizer.apply_chat_template(
            message,
            tokenize=False,
            add_generation_prompt=True
        )
        # Preparar las entradas para el modelo
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        # Generar la respuesta
        generated_ids = self.model.generate(
            **model_inputs,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
        )
        # Extraer solo los tokens generados
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        # Decodificar la respuesta generada
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response