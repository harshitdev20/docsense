FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install \
    --index-url=https://pypi.org/simple \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --default-timeout=1000 \
    --retries=10 \
    --no-cache-dir \
    -r requirements.txt

COPY . .

CMD ["python", "app/mcp_server.py"]