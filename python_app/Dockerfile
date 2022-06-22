FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
CMD flask run -h 0.0.0.0 -p 5000