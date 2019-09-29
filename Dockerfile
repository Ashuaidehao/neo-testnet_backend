FROM ashuaidehao/neowish-deps:latest  AS Final

WORKDIR /app
COPY . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# ENV FLASK_APP=neo-testnet-faucet.py

ENTRYPOINT [ "python","neo-testnet-faucet.py" ] 
