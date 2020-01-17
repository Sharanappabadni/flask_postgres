FROM python:3.8.0
WORKDIR /app
ENV FLASK_APP app
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
COPY . .
CMD ["flask", "run"]