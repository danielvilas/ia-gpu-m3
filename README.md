# ia-gpu-m3
Test of Python libs on M3 chips

from (https://medium.com/bluetuple-ai/how-to-enable-gpu-support-for-tensorflow-or-pytorch-on-macos-4aaaad057e74)

## Venv 
Do it in code or by...
```
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

## libs
```
python -m pip install tensorflow
python -m pip install tensorflow-metal
pip install --pre torch torchvision torchaudio \
 --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```
