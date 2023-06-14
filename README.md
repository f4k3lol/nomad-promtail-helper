# Nomad promtail helper

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

### Dockerhub
https://hub.docker.com/r/f4k3lol/nomad-promtail-helper