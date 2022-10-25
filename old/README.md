## Créditos

Inspirado en este [gist](https://gist.github.com/midudev/2bc13e6ef38ccc4716fba8b7258f1403) de Miguel Angel Durán

## Requisitos

* Python 3.9

Para poder tener varias versiones de python usamos `pyenv`  ([How to install and run multiple pythons with virtualenv and vscode](https://k0nze.dev/posts/install-pyenv-venv-vscode/)):

```bash
$ # prerequisites
$ sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git
$ # pyenv
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ # environment
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
$ source ~/.bashrc
```

Instala Python 3.9 con pyenv, que gestionará también los paquetes que instales luego con pip:

```bash
$ pyenv install 3.9.15
$ cd transcribe
$ pyenv local 3.9.15
$ pyenv version
3.9.15 (set by ~/transcribe/.python-version)
$ # note pyenv "channels" pip so youll need to install packages for each python version
$ which pip
/home/mhered/.pyenv/shims/pip
```

Crea y activa el venv en el directorio:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$
```

Instala las dependencias: [Whisper](https://openai.com/blog/whisper/) y [PyTube](https://pytube.io/en/latest/):

```bash
$ pip install git+https://github.com/openai/whisper.git
```

Instala `ffmpeg`:

```bash
$ sudo apt update && sudo apt install ffmpeg
```
