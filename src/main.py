import gradio as gr
import os
from matica_tools.task import Task
from dotenv import load_dotenv
import uuid

def test(file, transfer_name):
    file_path = file.name

    if not file_path:
        return "Please upload a file."

    transfer_type = "standard"
    
    load_dotenv(override=True)
    
    # 環境変数を参照
    dashboard_url = os.environ.get("DASHBOARD_URL")
    dashboard_username = os.environ.get("DASHBOARD_USERNAME")
    dashboard_api_key = os.environ.get("DASHBOARD_API_KEY")

    storage_service_url = os.environ.get("STORAGE_SERVICE_URL")
    storage_service_username = os.environ.get("STORAGE_SERVICE_USERNAME")
    storage_service_password = os.environ.get("STORAGE_SERVICE_PASSWORD")

    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    
    
    task_id = str(uuid.uuid4())

    url = Task.main(
        dashboard_url, 
        dashboard_username,
        dashboard_api_key,
        storage_service_url,
        storage_service_username,
        storage_service_password,
        aws_access_key_id,
        aws_secret_access_key,
        task_id, transfer_type, transfer_name, file_path)

    return f"# Result\n[Download the AIP file here]({url})"

title = "Archivematica Demo"
description = "This is a simple demonstration of Archivematica."
article = "<p style='text-align: center'>Satoru Nakamura, Boyoung Kim, Yasuyuki Minamiyama. <br/>Development of a User-friendly Application to Support Long-term Digital Preservation Using Archivematica, <br/>18th International Digital Curation Conference, 2024.</p>"


demo = gr.Interface(fn=test, inputs=[
    gr.File(label="File Upload"),
    gr.Textbox(label="Transfer Name")
], outputs=[
    gr.Markdown(label="Result", show_label=True),
], examples=[
    ["examples/Images.zip", "Images Example", "standard"],
    ["examples/ja.zip", "Japanse Example", "standard"]
], title=title, description=description, article=article, allow_flagging="never")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")