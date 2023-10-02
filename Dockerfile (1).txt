FROM generic_ocr

WORKDIR /workspace

COPY checkpoints ./checkpoints
COPY core ./core
COPY data ./data
COPY detections ./detections
COPY templates ./templates
COPY detect.py ./
COPY main.py ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
