# FROM python:3.11-slim
#
# WORKDIR /app
#
# COPY ./requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# COPY ./tests ./tets
# EXPOSE 5000

# CMD ["flask","--app", "MainScores.py" ,"--debug","run","--host=0.0.0.0", "--port=5000" ]
FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask
COPY . /srv
ENV FLASK_APP=app
CMD ["python","MainScores.py"]