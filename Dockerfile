FROM python:3.11-alpine
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
ENV NOMAD_ADDR=http://172.17.0.1:4646
ENV NOMAD_TOKEN=""
ENV NOMAD_NODE_NAME=""
ENV ALLOC_DIR=/allocs
ENV PROMTAIL_ALLOC_DIR=/nomad
ENV REFRESH_PERIOD=15
ENV NAMESPACE_LABEL=nomad_namespace
ENV JOB_LABEL=nomad_job
ENV DEBUG=False
COPY nomad-promtail-helper.py /nomad-promtail-helper.py
CMD python /nomad-promtail-helper.py
