# Contributing to This Site

## Clone repo

```bash
git clone https://github.com/UCSCRocketry/rocket-site.git
cd rocket-site/
```

## Create virtual environment

```bash
python3.13 -m venv venv
```

## Activate virtual environment

On Windows

```ps
myenv\Scripts\activate.bat
```

On Linux and Mac

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run local preview

```bash
mkdocs serve
```

## Create branch

```bash
git checkout -b <my_feature>
```

## Add and commit changes

```bash
git add docs/
git commit -m "Did stuff"
```

Commit with descriptive message

## Push

```bash
git push
```

Always preview site before pushing. Do not push directly to main.

Run `python -m pip check` and `mkdocs build --strict` before opening a PR.
Use Python 3.13 as pinned in `.python-version`, and install the Cairo system
library for social card generation (`libcairo2` on Ubuntu or `cairo` on macOS).

## Create PR

This happens on Github. Site maintainer must approve PRs, and the `Site build`
check must pass before merging.
