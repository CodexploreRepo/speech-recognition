# speech-recognition

## Environment

- You can create your own virtual environment and install the `requirements.txt` file
- Note: torch should be installed based on your CUDA version.

```bash
cd speech-recognition

conda create -n asr
conda activate asr
conda install pip
# pytorch
conda install pytorch::pytorch torchaudio -c pytorch
# pyaudio
brew install portaudio
pip install pyaudio
# conda install remaining packages
conda install --file requirements.txt
```

- Setup the project

```bash
pip install -e .
```

- Also, you need to install **ctcdecode**:

```bash
git clone --recursive https://github.com/parlance/ctcdecode.git
cd ctcdecode && pip install . && cd ..
```

## References

- [Vietnamese Speech Recognition](https://github.com/manhph2211/Vietnamese-Speech-Recognition)
