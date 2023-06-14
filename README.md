# Nomad promtail helper

### Dockerhub
https://hub.docker.com/r/f4k3lol/nomad-promtail-helper

### Description
Creates json files for file_sd_configs

e.g. `6498fe7a-f237-bda5-5918-a1e710e2b108.json`
```
[
    {
        "targets": [ "localhost" ],
        "labels": {
            "__path__": "/nomad/6498fe7a-f237-bda5-5918-a1e710e2b108/alloc/logs/*",
            "__path_exclude__": "/nomad/6498fe7a-f237-bda5-5918-a1e710e2b108/alloc/logs/*fifo",
            "nomad_namespace": "ns1",
            "nomad_job": "promtail",
            "nomad_node": "node1"
        }
    }
]
```

### Environment Variables

| Name | Default value | Description |
| --- | --- | --- |
| NOMAD_ADDR | http://172.17.0.1:4646 | Nomad address. Used by nomad lib |
| NOMAD_TOKEN | "" | Nomad token. You must pass it to job (see job example) |
| NOMAD_NODE_NAME | "" | Nomad node name. Script uses this env to create files for allocations only on specific node he runs on. Passed by job (see job example) |
| ALLOC_DIR | /allocs | Dir where alloc files for file_sd_configs should be created |
| PROMTAIL_ALLOC_DIR | /nomad | Specifies where promtail should find nomad alloc files (Used in generating alloc files for file_sd_configs) |
| REFRESH_PERIOD | 15 | Timeout between generating alloc files for file_sd_configs |
| NAMESPACE_LABEL | nomad_namespace | Used in generating alloc files for file_sd_configs. Specifies label name for namespace, which should be added by promtail |
| NODE_LABEL | nomad_node | Used in generating alloc files for file_sd_configs. Specifies label name for node name, which should be added by promtail |
| JOB_LABEL | nomad_job | Used in generating alloc files for file_sd_configs. Specifies label name for job name, which should be added by promtail |
| DEBUG | False | Set this to "True" to enable debug |