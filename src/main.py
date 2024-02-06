import gradio as gr
import os
from archivematica_tools.task import Task
from dotenv import load_dotenv
import uuid

def test(file, transfer_name):
    file_path = file.name

    if not file_path:
        return "Please upload a file."
    
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

    aws_bucket_name = os.environ.get("AWS_BUCKET_NAME")

    transfer_type = os.environ.get("TRANSFER_TYPE")
    location_uuid = os.environ.get("LOCATION_UUID")
    processing_config = os.environ.get("PROCESSING_CONFIG")
    
    transfer_source_prefix = os.environ.get("TRANSFER_SOURCE_PREFIX")
    
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
        task_id,
        transfer_type,
        transfer_name,
        file_path,
        location_uuid,
        processing_config,
        aws_bucket_name,
        transfer_source_prefix
    )

    return f"# Result\n[Download the AIP file here]({url})"

title = "Archivematica Gradio Demo"
description = "A simple demonstration of Archivematica and Gradio."
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