FROM python:3.9-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
ENV TELEGRAM_ACCESS_TOKEN="7189373291:AAGT8N3ibcGZCxsbdCyOMl9IgkPFgiv3vxE"
ENV CHATGPT_BASICURL="https://chatgpt.hkbu.edu.hk/general/rest"
ENV CHATGPT_MODELNAME="gpt-35-turbo"
ENV CHATGPT_APIVERSION="2024-02-15-preview"
ENV CHATGPT_ACCESS_TOKEN="2a129f06-dc69-42c9-a1be-83a05ccdb0af"
ENV REDIS_HOST='TvshowsChatbot.redis.cache.windows.net'
ENV REDIS_PORT=6379
ENV REDIS_PASSWORD='UYe9jTpqIpZI1CGUNZUFcSQOE4Vs8Gh8HAzCaEKqR4o='

CMD ["python", "TvshowsChatbot.py"]
