FROM python:3.11

WORKDIR /workspace
ADD src/requirements.txt src/.env src/main.py src/examples /workspace/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "/workspace/main.py"]
# CMD ["gradio", "/workspace/main.py"]