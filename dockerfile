# keyword argument
# Simple 1 stage dockerfile 
# deploy python code
# cache dependencies using requirements.txt
# deploy app.py file 
# expose port 5000

FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
