1. Nginx Config
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile      on;
    keepalive_timeout  65;

    # upstream django_upstream {
    #     server 127.0.0.1:8001;
    # }

    server {
        listen 80;
        server_name _;

        client_max_body_size 200M;

        proxy_connect_timeout 600;
        proxy_send_timeout 600;
        proxy_read_timeout 600;
        send_timeout 600;

        root C:/Users/neebal/AppData/Local/Microsoft/WinGet/Packages/nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe/nginx-1.29.4/html/vite-react;
        index index.html;

        location /upload-cloud {
            proxy_pass http://127.0.0.1:8000;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /invoice/ {
            proxy_pass http://127.0.0.1:8000;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /invoices {
            proxy_pass http://127.0.0.1:8000;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        # React frontend
        location / {
            try_files $uri $uri/ /index.html;
        }
    }

    server {
        listen 81;
        server_name _;

        client_max_body_size 200M;

        proxy_connect_timeout 600;
        proxy_send_timeout 600;
        proxy_read_timeout 600;
        send_timeout 600;

        root C:/Users/neebal/AppData/Local/Microsoft/WinGet/Packages/nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe/nginx-1.29.4/html/vite-react-2;
        index index.html;

        location /upload-cloud {
            proxy_pass http://127.0.0.1:8081;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /invoice/ {
            proxy_pass http://127.0.0.1:8081;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /invoices {
            proxy_pass http://127.0.0.1:8081;

            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        # React frontend
        location / {
            try_files $uri $uri/ /index.html;
        }
    }

    # server {
    #     listen 80;
    #     server_name 192.168.1.80;
    #
    #     # Allow office Wi-Fi users
    #     # allow 192.168.1.0/24;
    #
    #     # Allow office Wi-Fi (mobile) users
    #     # allow 192.168.10.0/24;
    #
    #
    #     # Allow server itself (optional)
    #     allow 127.0.0.1;
    #
    #
    #     # Block everyone else
    #     # deny all;
    #
    #     # STATIC (collected)
    #     location /static/ {
    #         alias C:/Users/neebal/Desktop/neebal-horilla-hrms/staticfiles/;
    #         expires 30d;
    #         add_header Cache-Control "public, max-age=2592000";
    #     }
    #
    #     # MEDIA (uploads)
    #     location /media/ {
    #         alias C:/Users/neebal/Desktop/neebal-horilla-hrms/media/;
    #         expires 7d;
    #     }
    #
    #     location / {
    #         proxy_pass http://django_upstream;
    #
    #         proxy_set_header Host $host;
    #         proxy_set_header X-Real-IP $remote_addr;
    #         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    #         proxy_set_header X-Forwarded-Proto $scheme;
    #
    #         client_max_body_size 50m;
    #         proxy_read_timeout 300;
    #         proxy_connect_timeout 60;
    #         proxy_send_timeout 300;
    #     }
    # }
    #
    # server {
    #     listen 80;
    #     server_name horilla.neebal.com;
    #
    #     # Allow office Wi-Fi users
    #     # allow 192.168.1.0/24;
    #
    #     # Allow office Wi-Fi (mobile) users
    #     # allow 192.168.10.0/24;
    #
    #
    #     # Allow server itself (optional)
    #     allow 127.0.0.1;
    #
    #
    #     # Block everyone else
    #     # deny all;
    #
    #     # STATIC (collected)
    #     location /static/ {
    #         alias C:/Users/neebal/Desktop/neebal-horilla-hrms/staticfiles/;
    #         expires 30d;
    #         add_header Cache-Control "public, max-age=2592000";
    #     }
    #
    #     # MEDIA (uploads)
    #     location /media/ {
    #         alias C:/Users/neebal/Desktop/neebal-horilla-hrms/media/;
    #         expires 7d;
    #     }
    #
    #     location / {
    #         proxy_pass http://django_upstream;
    #
    #         proxy_set_header Host $host;
    #         proxy_set_header X-Real-IP $remote_addr;
    #         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    #         proxy_set_header X-Forwarded-Proto $scheme;
    #
    #         client_max_body_size 50m;
    #         proxy_read_timeout 300;
    #         proxy_connect_timeout 60;
    #         proxy_send_timeout 300;
    #     }
    # }
}
2. Backend Terminal Commands and Output
PS C:\Users\neebal\Desktop\anchorAlliedDemo2> ls

    Directory: C:\Users\neebal\Desktop\anchorAlliedDemo2

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----           3/13/2026  9:15 AM                backend
d----           3/13/2026  9:04 AM                Datasets
d----           3/13/2026  9:04 AM                Docs
d----           3/13/2026  9:26 AM                frontend
d----           3/13/2026  9:04 AM                invoice_reading_and_processing
-a---           3/13/2026  9:04 AM             43 .gitignore
-a---           3/13/2026  9:04 AM            541 README.md

PS C:\Users\neebal\Desktop\anchorAlliedDemo2> ..\horillaenv\Scripts\Activate.ps1
(horillaenv) PS C:\Users\neebal\Desktop\anchorAlliedDemo2> deactivate
PS C:\Users\neebal\Desktop\anchorAlliedDemo2> ..\anchorAlliedDemo\.venv\Scripts\activate.ps1
(anchor-allied) PS C:\Users\neebal\Desktop\anchorAlliedDemo2> pip list
Package               Version
--------------------- ------------
annotated-doc         0.0.4
annotated-types       0.7.0
anyio                 4.12.1
certifi               2026.2.25
charset-normalizer    3.4.5
click                 8.3.1
colorama              0.4.6
distro                1.9.0
dnspython             2.8.0
et_xmlfile            2.0.0
exceptiongroup        1.3.1
fastapi               0.135.1
filelock              3.25.1
fsspec                2026.2.0
groq                  1.1.0
h11                   0.16.0
hf-xet                1.3.2
httpcore              1.0.9
httpx                 0.28.1
huggingface_hub       1.6.0
idna                  3.11
Jinja2                3.1.6
jiter                 0.13.0
joblib                1.5.3
lxml                  6.0.2
markdown-it-py        4.0.0
MarkupSafe            3.0.3
mdurl                 0.1.2
mpmath                1.3.0
networkx              3.4.2
numpy                 2.2.6
openai                2.26.0
openpyxl              3.1.5
packaging             26.0
pandas                2.3.3
pillow                12.1.1
pip                   26.0.1
pydantic              2.12.5
pydantic_core         2.41.5
Pygments              2.19.2
pymongo               4.16.0
PyMuPDF               1.27.1
python-dateutil       2.9.0.post0
python-docx           1.2.0
python-dotenv         1.2.2
python-multipart      0.0.22
pytz                  2026.1.post1
PyYAML                6.0.3
regex                 2026.2.28
requests              2.32.5
rich                  14.3.3
safetensors           0.7.0
scikit-learn          1.7.2
scipy                 1.15.3
sentence-transformers 5.2.3
setuptools            65.5.0
shellingham           1.5.4
six                   1.17.0
sniffio               1.3.1
starlette             0.52.1
sympy                 1.14.0
threadpoolctl         3.6.0
tokenizers            0.22.2
torch                 2.7.0
tqdm                  4.67.3
transformers          5.3.0
typer                 0.24.1
typing_extensions     4.15.0
typing-inspection     0.4.2
tzdata                2025.3
urllib3               2.6.3
uv                    0.10.9
uvicorn               0.41.0
(anchor-allied) PS C:\Users\neebal\Desktop\anchorAlliedDemo2> ls

    Directory: C:\Users\neebal\Desktop\anchorAlliedDemo2

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----           3/13/2026  9:15 AM                backend
d----           3/13/2026  9:04 AM                Datasets
d----           3/13/2026  9:04 AM                Docs
d----           3/13/2026  9:26 AM                frontend
d----           3/13/2026  9:04 AM                invoice_reading_and_processing
-a---           3/13/2026  9:04 AM             43 .gitignore
-a---           3/13/2026  9:04 AM            541 README.md

(anchor-allied) PS C:\Users\neebal\Desktop\anchorAlliedDemo2> cd .\backend(anchor-allied) PS C:\Users\neebal\Desktop\anchorAlliedDemo2\backend> ls

    Directory: C:\Users\neebal\Desktop\anchorAlliedDemo2\backend

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----           3/13/2026  9:14 AM                __pycache__
d----           3/13/2026  9:14 AM                constant
d----           3/13/2026  9:04 AM                data
d----           3/13/2026  9:14 AM                service
d----           3/13/2026 10:37 AM                utils
-a---           3/13/2026 10:37 AM            386 .env
-a---           3/13/2026  9:04 AM            137 .env.example
-a---           3/13/2026  9:04 AM             83 .gitignore
-a---           3/13/2026  9:04 AM              4 .python-version
-a---           3/13/2026  9:04 AM           6325 app.py
-a---           3/13/2026  9:04 AM            615 pyproject.toml
-a---           3/13/2026  9:04 AM           2192 requirements.txt
-a---           3/13/2026  9:04 AM         179695 uv.lock

(anchor-allied) PS C:\Users\neebal\Desktop\anchorAlliedDemo2\backend> uvicorn.exe app:app --reload --port 8081
INFO:     Will watch for changes in these directories: ['C:\\Users\\neebal\\Desktop\\anchorAlliedDemo2\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8081 (Press CTRL+C to quit)
INFO:     Started reloader process [808] using StatReload
WEBHOOK URL https://script.google.com/macros/s/AKfycbwWa5n37ReCM1sAB8jA4_GXzhEqhIu1_CRGQV1rtOoLstVV_SMJ00igiPs75vWP5a1pBg/exec
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|████████████████████████████████████████████████████| 103/103 [00:00<00:00, 149.93it/s]
BertModel LOAD REPORT from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  |
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  |

Notes:
- UNEXPECTED    :can be ignored when loading from different task/architecture; not ok if you expect identical arch.
INFO:     Started server process [4152]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:49970 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:49970 - "GET /openapi.json HTTP/1.1" 200 OK
ChatCompletion(id='chatcmpl-450963def22c4a178a3e8e3d3a827138', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='{"lpo_no": "02620", "date": "19/06/2023", "distributor_name": "GREEN CIRCLE TRADING CO. LLC", "each_product_prize": [{"product_name": "2\\" Pvc Wrapping Tape Black", "quantity": "3ctn", "unit_price": "94", "total_price": "282"}, {"product_name": "Spray Paint: Brown 26 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Black 02 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Chrome Silver 5cm", "quantity": "5ctn", "unit_price": "50", "total_price": "250"}, {"product_name": "Spray Paint: (aqua) Blue 18 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}, {"product_name": "Spray Paint: Matt Black 20 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}]}', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None))], created=1776144715, model='accounts/fireworks/models/qwen3-vl-30b-a3b-instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=302, prompt_tokens=2509, total_tokens=2811, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0)))
Raw response from qwen3:---------> {"lpo_no": "02620", "date": "19/06/2023", "distributor_name": "GREEN CIRCLE TRADING CO. LLC", "each_product_prize": [{"product_name": "2\" Pvc Wrapping Tape Black", "quantity": "3ctn", "unit_price": "94", "total_price": "282"}, {"product_name": "Spray Paint: Brown 26 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Black 02 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Chrome Silver 5cm", "quantity": "5ctn", "unit_price": "50", "total_price": "250"}, {"product_name": "Spray Paint: (aqua) Blue 18 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}, {"product_name": "Spray Paint: Matt Black 20 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}]}
Cleaned Result from qwen3:----------> {"lpo_no": "02620", "date": "19/06/2023", "distributor_name": "GREEN CIRCLE TRADING CO. LLC", "each_product_prize": [{"product_name": "2\" Pvc Wrapping Tape Black", "quantity": "3ctn", "unit_price": "94", "total_price": "282"}, {"product_name": "Spray Paint: Brown 26 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Black 02 5cm", "quantity": "5ctn", "unit_price": "33", "total_price": "165"}, {"product_name": "Spray Paint: Chrome Silver 5cm", "quantity": "5ctn", "unit_price": "50", "total_price": "250"}, {"product_name": "Spray Paint: (aqua) Blue 18 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}, {"product_name": "Spray Paint: Matt Black 20 3ctn", "quantity": "3ctn", "unit_price": "33", "total_price": "99"}]}
Best Match: PVC PIPE WRAP TAPE,ASMACO,72MM X 60 FEET,BLACK,48PCS
Best item code: PVAS7260FXX02GPP48
Similarity Score: 71.28 %
Best Match: SPRAY PAINT,G2100,BROWN,12PCS,400 ML,220GRAM
Best item code: SPG2XXXX2612220
Similarity Score: 69.36 %
Best Match: SPRAY PAINT,ASMACO,MEDIUM GRAY,12PCS,400 ML,280GRAM
Best item code: SPASXXXX2712280
Similarity Score: 70.94 %
Best Match: SPRAY PAINT,ASMACO,CHROME SILVER,12PCS,400 ML,280GRAM
Best item code: SPASXXXX2212280
Similarity Score: 70.33 %
Best Match: SPRAY PAINT,ASMACO,WATER BLUE,12PCS,400 ML,280GRAM
Best item code: SPASXXXX3812280
Similarity Score: 72.07 %
Best Match: SPRAY PAINT,G2100,MATT BLACK,12PCS,400 ML,220GRAM
Best item code: SPG2XXXX2012220
Similarity Score: 72.57 %
Json data going in DB: {'lpo_no': '02620', 'date': '19/06/2023', 'distributor_name': 'GREEN CIRCLE TRADING CO. LLC', 'each_product_prize': [{'product_name': 'PVC PIPE WRAP TAPE,ASMACO,72MM X 60 FEET,BLACK,48PCS', 'quantity': '3ctn', 'unit_price': '94', 'total_price': '282', 'item_code': 'PVAS7260FXX02GPP48'}, {'product_name': 'SPRAY PAINT,G2100,BROWN,12PCS,400 ML,220GRAM', 'quantity': '5ctn', 'unit_price': '33', 'total_price': '165', 'item_code': 'SPG2XXXX2612220'}, {'product_name': 'SPRAY PAINT,ASMACO,MEDIUM GRAY,12PCS,400 ML,280GRAM', 'quantity': '5ctn', 'unit_price': '33', 'total_price': '165', 'item_code': 'SPASXXXX2712280'}, {'product_name': 'SPRAY PAINT,ASMACO,CHROME SILVER,12PCS,400 ML,280GRAM', 'quantity': '5ctn', 'unit_price': '50', 'total_price': '250', 'item_code': 'SPASXXXX2212280'}, {'product_name': 'SPRAY PAINT,ASMACO,WATER BLUE,12PCS,400 ML,280GRAM', 'quantity': '3ctn', 'unit_price': '33', 'total_price': '99', 'item_code': 'SPASXXXX3812280'}, {'product_name': 'SPRAY PAINT,G2100,MATT BLACK,12PCS,400 ML,220GRAM', 'quantity': '3ctn', 'unit_price': '33', 'total_price': '99', 'item_code': 'SPG2XXXX2012220'}]}
Data sent to CSV: {'lpo_no': '02620', 'customer_name': 'GREEN CIRCLE TRADING CO. LLC', 'item_code': None, 'item_description': '[{"product_name": "PVC PIPE WRAP TAPE,ASMACO,72MM X 60 FEET,BLACK,48PCS", "quantity": "3ctn", "unit_price": "94", "total_price": "282", "item_code": "PVAS7260FXX02GPP48"}, {"product_name": "SPRAY PAINT,G2100,BROWN,12PCS,400 ML,220GRAM", "quantity": "5ctn", "unit_price": "33", "total_price": "165", "item_code": "SPG2XXXX2612220"}, {"product_name": "SPRAY PAINT,ASMACO,MEDIUM GRAY,12PCS,400 ML,280GRAM", "quantity": "5ctn", "unit_price": "33", "total_price": "165", "item_code": "SPASXXXX2712280"}, {"product_name": "SPRAY PAINT,ASMACO,CHROME SILVER,12PCS,400 ML,280GRAM", "quantity": "5ctn", "unit_price": "50", "total_price": "250", "item_code": "SPASXXXX2212280"}, {"product_name": "SPRAY PAINT,ASMACO,WATER BLUE,12PCS,400 ML,280GRAM", "quantity": "3ctn", "unit_price": "33", "total_price": "99", "item_code": "SPASXXXX3812280"}, {"product_name": "SPRAY PAINT,G2100,MATT BLACK,12PCS,400 ML,220GRAM", "quantity": "3ctn", "unit_price": "33", "total_price": "99", "item_code": "SPG2XXXX2012220"}]', 'date': '19/06/2023'}
Sent to Google Sheets: Data added to 14-04-2026-Final and 14-04-2026-Preview
INFO:     192.168.1.1:0 - "POST /upload-cloud HTTP/1.1" 200 OK
3. Nginx Terminal Commands and Output: TO START
PS C:\Users\neebal\AppData\Local\Microsoft\WinGet\Packages\nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe\nginx-1.29.4> nginx -t
nginx: the configuration file C:\Users\neebal\AppData\Local\Microsoft\WinGet\Packages\nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe\nginx-1.29.4/conf/nginx.conf syntax is ok
nginx: configuration file C:\Users\neebal\AppData\Local\Microsoft\WinGet\Packages\nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe\nginx-1.29.4/conf/nginx.conf test is successful
PS C:\Users\neebal\AppData\Local\Microsoft\WinGet\Packages\nginxinc.nginx_Microsoft.Winget.Source_8wekyb3d8bbwe\nginx-1.29.4> .\nginx.exe
4. Nginx Terminal Commands and Output: TO SET UP FOR WINDOWS
cd Desktop/anchorAliedDemo2/frontend
winget install Node.js
npm i
npm run build
winget install nginxinc.nginx
Then open file explorer, in frontend directory
Open dist dictory
Copy the contents
Go to nginx installation dir, to the html directory
Create directory vite-react
Paste the contants
Modify nginx.conf viz. in nginx installation dir
Link is something like this: http://103.19.133.94:81/home, with port 81
