FROM python:3.11-alpine
RUN pip install python-nomad==1.5.0
ENV NOMAD_ADDR=http://172.17.0.1:4646
ENV NOMAD_TOKEN=""
ENV NOMAD_NODE_NAME=""
ENV ALLOC_DIR=/allocs
ENV PROMTAIL_ALLOC_DIR=/nomad
ENV REFRESH_PERIOD=5
ENV DEBUG=false
COPY nomad-promtail-helper.py /nomad-promtail-helper.py
CMD python /nomad-promtail-helper.py
