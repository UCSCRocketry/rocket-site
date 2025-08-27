# Contributing to This Site

## Clone repo

```bash
git clone https://github.com/UCSCRocketry/rocket-site.git
cd rocket-site/
```

## Create virtual enviroment

```bash
python -m venv venv
```

## Activate virtual enviroment

On Windows

```ps
myenv\Scripts\activate.bat
```

On Linux and Mac

```bash
source venv/bin/activate
```

## Install dependancies

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

Commit with descriptime message

## Push

```bash
git push
```

Always preview site before pushing. Do not push directly to main.

## Create PR

This happens on Github. Site maintainer must approve PRs.
