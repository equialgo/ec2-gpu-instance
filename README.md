# ec2-gpu-instance
Ansible provision scripts for configuration of an Amazon EC2 GPU instance

## Amazon instance and AMI

These provision scripts should be applied to an EC2 GPU instance configured with an *Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-47a23a30* machine image.

## Installed software

The following software is installed on the instance:
- *common*; regular packages like java8, git, curl, make, etc.
- *cuda*; Nvidia drivers, CUDA, CUDNN
- *tools*; Anaconda, Theano, Caffe
