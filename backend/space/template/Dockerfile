# read the doc: https://docs.lagrangedao.org/lagrange-dao/getstarted/spaces/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "hello_world:app", "--host", "0.0.0.0", "--port", "7860"]
