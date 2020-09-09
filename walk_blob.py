from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient



def walk_container(client, container, verbose = False):
    container_client = client.get_container_client(container)
    if verbose:
        print('C: {}'.format(container))
    depth = 1
    separator = '   '
    project_folders=[]
    def walk_blob_hierarchy(prefix="", f_name=""):
        

        nonlocal depth
        for item in container_client.walk_blobs(name_starts_with=prefix):
            short_name = item.name[len(prefix):]
            if isinstance(item, BlobPrefix):
                if verbose:
                    print('F: ' + separator * depth + short_name)
                depth += 1
                walk_blob_hierarchy(prefix=item.name, f_name=short_name)
                depth -= 1
            else:
                message = 'B: ' + separator * depth + short_name
                results = list(container_client.list_blobs(name_starts_with=item.name, include=['snapshots']))
                num_snapshots = len(results) - 1
                if num_snapshots:
                    message += " ({} snapshots)".format(num_snapshots)
                if short_name == 'index.html':
                    project_folders.append(f_name)
                if verbose:
                    print(message)
   
        
    walk_blob_hierarchy()
    print(project_folders)
