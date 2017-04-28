# ec2-gpu-instance
Ansible provision scripts for configuration of an Amazon EC2 GPU P2 instance.

## Amazon instance and AMI

These provision scripts should be applied to an EC2 P2 GPU instance configured with an *Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-47a23a30* machine image.

## Installed software

The following software is installed on the instance:
- **common**; regular packages like java8, git, curl, make, etc.
- **cuda**; Nvidia drivers, CUDA 8.0, CUDNN 5.1
- **tools**; Anaconda (python 3), Theano, TensorFlow, Keras, MXNet

## Running the ansible-playbook

To allow the installation of the NVIDIA® cuDNN – GPU Accelerated Deep Learning libraries, please download the binaries from https://developer.nvidia.com/cudnn.

Perform the following steps to successfully install the instance using the ansible playbook:

1. Make sure ansible is installed (preferably in python 2 environment, if not install using `pip install ansible`).
2. Add the cudnn-8.0-linux-x64-v5.1.tgz file to the **roles/gpu/files/**-folder.
3. Add the public ip or dns of the instance to the hosts file.
4. Add the path of the pem key file to the ansible.cfg file.
5. Run the playbook from the root of this repository by executing: `ansible-playbook gpu-instance.yml`.

## Accessing Jupyter notebook

Jupyter notebook is by default installed and started during bootup of the instance:
1. Make sure you setup the security group such that port 9999 is exposed to you local ip.
2. Open your browser and got to the following url **https://public_ip:9999**
3. Ignore the ssl certificate warning and login with the default password `accelerator`
