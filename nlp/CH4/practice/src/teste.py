import requests

resposta = requests.get("https://huggingface.co/api/datasets/squad_v2", timeout=5)
print(resposta.status_code)