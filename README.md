# `transcribe`: crear subtítulos para los videos de un canal YouTube

## Créditos

Inspirado en este [gist](https://gist.github.com/midudev/2bc13e6ef38ccc4716fba8b7258f1403) de Miguel Angel Durán y en este [video tutorial](https://www.youtube.com/watch?v=F30yC2jl5nA) de la herramienta `yt-whisper` de Miguel Piedrafita.

Desarrollado para añadir subtítulos a los vídeos del canal youtube de Python España a sugerencia de @astrojuanlu durante #Hacktoberfest22.

## Requisitos

* Python 3.9

* [PyTube](https://pytube.io/en/latest/):

```bash
$ pip install git+https://github.com/openai/whisper.git
```

* [Whisper](https://openai.com/blog/whisper/):

```bash
$ pip install pytube
```

* `ffmpeg`:

```bash
$ sudo apt update && sudo apt install ffmpeg
```

* `yt-whisper`:

```bash
$ pip install git+https://github.com/m1guelpf/yt-whisper.git
```

## `scan_channel.py`: escanear un canal YouTube

Herramienta de linea de comandos que recibe la URL de un canal de YouTube, lo escanea y genera un archivo JSON con detalles de todos los vídeos que contiene.

Uso de la herramienta:   

```sh
$ python3 scan_channel.py -h
usage: scan_channel.py [-h] [--channel CHANNEL] [--file FILE]

Scan a YouTube channel and create a JSON file with contents

optional arguments:
  -h, --help         show this help message and exit
  --channel CHANNEL  URL of the YouTube channel to scan
  --file FILE        Name of the output file (Optional, default is channel.json)

$ python3 scan_channel.py --channel https://www.youtube.com/channel/UCPnRCRhb-6gaPZuQWS7RVag --file my_channel.json
2022-10-25 21:18:41,325 [INFO] Scanning YouTube channel...
2022-10-25 21:18:42,574 [INFO] 6 videos found in the channel.
2022-10-25 21:18:42,575 [INFO] Building data structure...
2022-10-25 21:18:44,062 [INFO] 16.67% ...
2022-10-25 21:18:45,523 [INFO] 33.33% ...
2022-10-25 21:18:46,813 [INFO] 50.00% ...
2022-10-25 21:18:47,964 [INFO] 66.67% ...
2022-10-25 21:18:49,363 [INFO] 83.33% ...
2022-10-25 21:18:50,707 [INFO] 100.00% ...
2022-10-25 21:18:50,709 [INFO] Writing JSON...
```

La herramienta escanea el canal y genera un fichero JSON con detalles de los videos. El identificador único lo toma de la URL del video.

```json
{
    "z2Vivp0AbRg": {
        "url": "https://www.youtube.com/watch?v=z2Vivp0AbRg",
        "title": "Mini Pupper adventures - Part 6 - Legs Assembly",
        "published": "01/05/22",
        "views": 239,
        "transcript": ""
    },
    "PA9QOXW9rWs": {
        "url": "https://www.youtube.com/watch?v=PA9QOXW9rWs",
        "title": "Mini Pupper adventures - Part 5 - Software",
        "published": "14/04/22",
        "views": 242,
        "transcript": ""
    },
    "bmLP8sHBs2o": {
        "url": "https://www.youtube.com/watch?v=bmLP8sHBs2o",
        "title": "Mini Pupper adventures - Part 4 - Electronics",
        "published": "24/03/22",
        "views": 241,
        "transcript": ""
    },
    "shPb4SnDpC4": {
        "url": "https://www.youtube.com/watch?v=shPb4SnDpC4",
        "title": "Mini Pupper adventures - Part 1 -  Unboxing",
        "published": "03/03/22",
        "views": 315,
        "transcript": ""
    },
    "kHCIWT2SSXw": {
        "url": "https://www.youtube.com/watch?v=kHCIWT2SSXw",
        "title": "Mini Pupper adventures - Part 2 - Hip Assembly",
        "published": "03/03/22",
        "views": 266,
        "transcript": ""
    },
    "e0-bLMICy54": {
        "url": "https://www.youtube.com/watch?v=e0-bLMICy54",
        "title": "Mini Pupper adventures - Part 3 - Body Assembly",
        "published": "03/03/22",
        "views": 325,
        "transcript": ""
    }
}
```

## `process_channel.py`: Generar subtítulos

Herramienta de linea de comandos que lee un archivo JSON con el formato generado por `scan_channel.py` y genera subtítulos para cada uno de los vídeos.

El proceso de generar subtítulos es bastante lento (aproximadamente x3 la duración del vídeo usando un portátil modesto), por lo que la herramienta está pensada para reanudar la tarea si es interrumpida (el progreso parcial del video que se está analizando se pierde pero no empieza a escanear el canal desde el principio).

La herramienta lee el JSON y busca el video de mayor numero de visitas que tiene vacío el campo`transcript `(es decir, para el que aun no ha generado subtítulos). Cuando termina graba los subtítulos en formato SRT en el directorio `./captions/[video_id]/`, actualiza el campo `transcript` en el JSON y lo salva, y continua con el siguiente vídeo por numero de visitas.

Uso de la línea de comandos:   

```sh
$ python3 process_channel.py -h
usage: process_channel.py [-h] [--file FILE]

Resumes processing videos from a JSON file

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Name of the input file (Optional, default is channel.json)

$ python3 process_channel.py --file my_channel.json

```

## Issues conocidos

* Para interrumpir la ejecución hay que pulsar CTRL+C repetidas veces (#2)
