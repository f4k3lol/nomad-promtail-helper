# Nomad promtail helper

Creates json files for file_sd_configs

e.g. `396fd2f1-a7b7-c3ce-1b59-33170a29584d.json`
```
[
    {
        "targets": [ "localhost" ],
        "labels": {
            "__path__": "/nomad/396fd2f1-a7b7-c3ce-1b59-33170a29584d/alloc/logs/*std*.{?,??}",
            "nomad_namespace": "ns1",
            "nomad_job": "prometheus"
        }
    }
]
```