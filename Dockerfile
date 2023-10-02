FROM ubuntu:18.04

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
        software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip
RUN python3.7 -m pip install pip
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-setuptools
RUN python3.7 -m pip install pip --upgrade pip

RUN useradd -s /bin/bash user

RUN apt-get -y install tesseract-ocr

COPY requirements.txt ./

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN pip install -r requirements.txt

COPY checkpoints ./checkpoints
COPY core ./core
COPY data ./data
COPY detections ./detections
COPY templates ./templates
COPY detect.py ./
COPY main.py ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
