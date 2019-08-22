FROM python:3.6-alpine  AS Final

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add --update build-base libffi-dev postgresql-dev 

WORKDIR /app
COPY . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# ENV FLASK_APP=neo-testnet-faucet.py

ENTRYPOINT [ "python","neo-testnet-faucet.py" ] 
