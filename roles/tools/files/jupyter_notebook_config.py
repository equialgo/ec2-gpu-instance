# Set options for certfile, ip, password, and toggle off browser auto-opening
c.NotebookApp.certfile = u'/home/ubuntu/.jupyter/mycert.pem'
c.NotebookApp.keyfile = u'/home/ubuntu/.jupyter/mykey.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha1:c3eacd915e69:65c80dc268c6dab2c28a885b9e9d50cbc9614a2c' #accelerator
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/home/ubuntu/'

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 9999