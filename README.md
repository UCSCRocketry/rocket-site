# rocket-site
Website for the UCSC Rocket Team

## Contributing
### Getting Started
To get started `git clone` the repo and ensure you have the [dependencies](#deps) installed. 
Create a python virtual environment with `python -m venv venv` then activate it with `source venv/bin/activate` and install pip dependencies with `pip install -r requirements.txt`.

### Tech Stack
This project uses MkDocs to build and format the site. Assuming you know how Markdown works, just edit the .md file for the page you are working on.

To build the site just run `mkdocs build` in the venv or you can start it on a local server using `mkdocs serve`.

### Dependencies {#deps}
This project uses
```
python3
cairosvg
```
