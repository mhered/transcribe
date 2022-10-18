## Requisitos

Basado en este [Gist](https://gist.github.com/midudev/2bc13e6ef38ccc4716fba8b7258f1403) de Miguel Angel Durán

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
$ pip install pytube
```

Instala `ffmpeg`:

```bash
$ sudo apt update && sudo apt install ffmpeg
```

## Cómo usar la línea de comandos

Necesitas indicar la URL del vídeo de YouTube que quieres transcribir:

```sh
python3 transcript.py -h

python3 transcript.py --video "https://www.youtube.com/watch?v=x0YF9q1pJcYA"

# también puedes indicar el modelo de IA que usará Whisper
# cuanto más grande, más tardará en descargarlo la primera vez
python3 transcript.py --video "https://www.youtube.com/watch?v=x0YF9q1pJcYA" --model "large"
```

Probado con el vídeo de la [Presentación de Python Sevilla en la Pycon2020](https://www.youtube.com/watch?v=x0YF9q1pJcYA

```bash
$ python3 transcript.py --video https://www.youtube.com/watch?v=x0YF9q1pJcYA
```

Resultado:

Hola, muy buenas. Soy Cayetano, uno de los organizadores de Python Sevilla. En este vídeo nos gustaría presentaros nuestra comunidad. Hola, soy Alberto Fernández y soy uno de los organizadores de Python Sevilla. El grupo se crea hace ya bastantes años, allá por 2012, pero bueno, funcionando de forma un poco más continuada, llevamos unos 5 años desde 2015, **años** desde el cual pues empezamos ya a hacer **mitad** de forma más regular. Actualmente somos, aparte de Alberto y yo mismo, otros dos organizadores, Joséma y Ana. Bueno, algún organizador más que ha participado en el pasado, pero bueno, por motivos personales y de carga de trabajo pues han tenido que quedar un paso atrás. Hemos llegado a la cifra de 1.480 miembros en Meetup, lo cual está bastante bien para el tamaño que tiene la ciudad de Sevilla. Tenemos una comunidad también de miembros en Telegram de unos 190 personas, que también creo que bueno, pues no está nada mal. Además, estamos dentro actualmente de la Python Software Fundation Meetup Pro Network, lo cual nos da visibilidad más allá de lo que es la propia comunidad local. En nuestra cuenta de **GuiHA**, podéis encontrar algunas de las charlas que hemos dado en nuestros meetups. La temática **me variaba**, Data Science, Desarrollo Web, Seguridad Informática. Desde el año pasado formamos parte de **su web**. Una meta comunidad que aglutina a todas las comunidades tecnológicas de Sevilla. El objetivo es poder emprender actividades que junten a diferentes comunidades. Bueno, me despido, muchas gracias por escucharnos y ya sabéis que si pasáis por Sevilla, seréis recibidos con las manos abiertas en nuestra comunidad. Un saludo. Muchas gracias por vuestra atención. Nos vemos en la Python del año que viene.



## Descargar lista de videos del canal

Instrucciones aqui: https://www.youtube.com/watch?v=mXwKxtvhIJ4

Click derecho --> Inspect --> Console

* Pegar: 

  ```
  var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);
  ```

* Pegar:

  ```
  window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title"){console.log('\t'+v.title+'\t'+v.href+'\t')}});
  ```

  Click derecho --> Save all messages to file
