# ml-tutorial
Machine Learning tutorial

  * Install PyCharm Community
    * https://www.jetbrains.com/de-de/pycharm/download/#section=linux
  * Install Atom
    * https://www.ubuntuupdates.org/ppa/atom
  * Install VisualStudioCode
    * https://www.ubuntuupdates.org/ppa/vscode

## Cuda

Install Cuda
  * https://www.wikiwand.com/de/CUDA
  * https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux
  * https://medium.com/@stephengregory_69986/installing-cuda-10-1-on-ubuntu-20-04-e562a5e724a0
  * https://medium.com/analytics-vidhya/installing-tensorflow-with-cuda-cudnn-gpu-support-on-ubuntu-20-04-f6f67745750a


```
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt install cuda
#echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo '# CUDA' >> ~/.zshrc
echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.zshrc
```

Install libcudart

```
sudo apt install libcudart10.1
```

## Pyton virtualenv

Install python virtualenv

```
sudo apt update
sudo apt install python3-venv
```

move to the desired directory an initialize the virtual environment

```
cd ml-tutorial
python3 -m venv venv
```

This has generated a directory "venv" inside your working directory.

Start the environment

```
source venv/bin/activate
```

Stop the environment

```
deactivate
```

## tensorflkow Tutorial

  * https://codelabs.developers.google.com/codelabs/tensorflow-lab1-helloworld#2
