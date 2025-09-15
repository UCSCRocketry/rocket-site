import yaml
import os


def define_env(env):
    path = os.path.join(env.project_dir, "docs", "leadership", "leads.yml")
    with open(path, "r", encoding="utf-8") as f:
        leads_data = yaml.safe_load(f)
    env.variables["leads"] = leads_data
