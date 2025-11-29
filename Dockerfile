FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN chmod +x start.sh || true
ENV PORT=8000
EXPOSE 8000
CMD ["sh","start.sh"]
