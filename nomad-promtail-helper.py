import nomad
import os
import time

n = nomad.Nomad()
node_name = os.environ['NOMAD_NODE_NAME']
alloc_dir = os.environ['ALLOC_DIR']
promtail_alloc_dir = os.environ['PROMTAIL_ALLOC_DIR']
refresh_period = int(os.environ['REFRESH_PERIOD'])
debug = eval(os.environ['DEBUG'])
namespace_label = os.environ['NAMESPACE_LABEL']
job_label = os.environ['JOB_LABEL']
node_label = os.environ['NODE_LABEL']

def sync_alloc_dir():
    namespaces = n.namespaces.get_namespaces()
    alloc_files = []
    for ns in namespaces:
        ns_name = ns["Name"]
        allocs = n.allocations.get_allocations(namespace=ns_name)
        for alloc in allocs:
            if alloc["NodeName"] == node_name:
                alloc_id = alloc["ID"]
                job_name = alloc["JobID"]
                filename = f"{alloc_id}.json"
                create_file_config(alloc_id, ns_name, job_name)
                alloc_files.append(filename)
    dir_files = os.listdir(alloc_dir)
    for dir_file in dir_files:
        if dir_file not in alloc_files:
            if debug:
                print(f"deleting file {alloc_dir}/{dir_file}")
            os.remove(f"{alloc_dir}/{dir_file}")

def create_file_config(id, namespace, job_name):
    if debug:
        print(f"creating file {alloc_dir}/{id}.json")
    with open(f"{alloc_dir}/{id}.json", 'w') as f:
        f.write(f'''
[
    {{
        "targets": [ "localhost" ],
        "labels": {{
            "__path__": "{promtail_alloc_dir}/{id}/alloc/logs/*",
            "__path_exclude__": "{promtail_alloc_dir}/{id}/alloc/logs/*fifo",
            "{namespace_label}": "{namespace}",
            "{job_label}": "{job_name}",
            "{node_label}": "{node_name}"
        }}
    }}
]
''')

if __name__ == "__main__":
    if not os.path.exists(alloc_dir):
        os.makedirs(alloc_dir)
    while True:
        sync_alloc_dir()
        time.sleep(refresh_period)