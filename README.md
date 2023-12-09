<p align="center">
<img src="https://raw.githubusercontent.com/surbhitt/qaahl/main/assets/qaahl.webp" width=25% height=25%>
</p>

# Objective

To develop an application capable of scrapping data from webpages and to provide visuals to assist the process through a GUI. Implementing a light weight multithreaded interactive application.

# Introduction

Qaahl serves as a minimalist webcrawler providing the basic functionality of a scrapper. A lightweight graphical interface built using pygames.

<p align="center">
<img src="https://raw.githubusercontent.com/surbhitt/qaahl/main/assets/qaahl_screen.png">
</p>

# Libraries utilised

- Pygame
- Requests
- Beautiful Soup (Bs4)

# Run

```console
        pip install -r requirements.txt
        python3 main.py $URL $flags
```

| `$URL`   | with the link as the base url                   |
| -------- | ----------------------------------------------- |
| `$flags` | with flags e.g. -d 3 performs depth=3 traversal |
