# rocket-site
Website for the UCSC Rocket Team

## Contributing
### Getting Started
To get started `git clone` the repo and ensure you have the [dependencies](#dependencies) installed. 
Use Python 3.13 (pinned in `.python-version`). Create a virtual environment with `python3.13 -m venv venv`, then activate it with `source venv/bin/activate` and install dependencies with `python -m pip install -r requirements.txt`.

### Tech Stack
This project uses MkDocs to build and format the site. Assuming you know how Markdown works, just edit the .md file for the page you are working on.

To build the site just run `mkdocs build` in the venv or you can start it on a local server using `mkdocs serve`.

Before opening a pull request, run `python -m pip check` and `mkdocs build --strict`. CI runs these checks on every pull request and merge queue entry, including a fresh dependency installation. The `Site build` check must pass before merging into `main`. Deployment publishes the build artifact only after checks pass on `main`.

Keep Python upgrades explicit in `.python-version` and test them with the pinned dependencies. CI requires binary wheels so an unsupported Python/dependency combination fails immediately instead of attempting native compilation.

### Dependencies
This project uses
```
Python 3.13
Cairo system library (libcairo2 on Ubuntu, cairo on macOS)
```
