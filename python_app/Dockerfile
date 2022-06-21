FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r ./python_app/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "hello.py" ]