FROM python:3.12

RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade pip

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
