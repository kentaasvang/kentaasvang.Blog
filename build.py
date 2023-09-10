#!./venv/bin/python
import os
import logging
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

from typing import Dict

if not load_dotenv():
    raise Exception("Could not load .env file")

def get_env_variable(var_name: str) -> str:
    value = os.getenv(var_name, False)
    if not value:
        raise Exception(f"Could not load environment variable '{var_name}'")
    return value

def load_env_variables(env_vars: Dict[str, str]) -> Dict[str, str]:
    for env_var in env_vars.keys():
        env_vars[env_var] = get_env_variable(env_var)
    return env_vars

DEVELOPMENT = get_env_variable("DEVELOPMENT") == "true"

if DEVELOPMENT:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

ENVIRONMENT_VARIABLES: Dict[str, str] = {
    "HTML_MINIBLOG_NAME": "", 
    "HTML_TEMPLATE_DIR": "", 
    "NGINX_TEMPLATE_DIR": "", 
    "NGINX_SITES_AVAILABLE": "", 
    "NGINX_SERVER_NAME": "", 
    "NGINX_LISTEN": "", 
    "NGINX_INDEX": "", 
    "NGINX_ROOT": ""}

# load environment variables
ENVIRONMENT_VARIABLES = load_env_variables(ENVIRONMENT_VARIABLES)

logging.info("Building Miniblog")

# *** Rebuild Nginx config files ***
logging.info("Cleaning up old nginx config files")
if not DEVELOPMENT:
    sites_available = ENVIRONMENT_VARIABLES["NGINX_SITES_AVAILABLE"]
else:
    sites_available = "dist/nginx"
for file in os.listdir(sites_available):
    logging.debug(f"Removing '{file}'")
    os.remove(os.path.join(sites_available, file))

logging.info("Creating new nginx config files")
nginx_template_dir = ENVIRONMENT_VARIABLES["NGINX_TEMPLATE_DIR"]
nginx_jinja_env = Environment(loader=FileSystemLoader(nginx_template_dir))
nginx_jinja_context = {
    "NGINX_SERVER_NAME": ENVIRONMENT_VARIABLES["NGINX_SERVER_NAME"],
    "NGINX_LISTEN": ENVIRONMENT_VARIABLES["NGINX_LISTEN"],
    "NGINX_INDEX": ENVIRONMENT_VARIABLES["NGINX_INDEX"],
    "NGINX_ROOT": ENVIRONMENT_VARIABLES["NGINX_ROOT"],
}

nginx_output = nginx_jinja_env.get_template("nginx.conf").render(nginx_jinja_context)

if not DEVELOPMENT:
    nginx_config_file = os.path.join(sites_available, ENVIRONMENT_VARIABLES["NGINX_SERVER_NAME"])
else:
    nginx_config_file = os.path.join("dist/nginx", ENVIRONMENT_VARIABLES["NGINX_SERVER_NAME"])

with open(nginx_config_file, "w") as nginx_file:
    logging.debug(f"Writing nginx config file to '{nginx_config_file}'")
    nginx_file.write(nginx_output)

# *** Rebuild HTML files ***
logging.info("Cleaning up old HTML files")
if not DEVELOPMENT:
    nginx_root = ENVIRONMENT_VARIABLES["NGINX_ROOT"]
else:
    nginx_root = "dist/html"

for file in os.listdir(nginx_root):
    if file.endswith(".html"):
        logging.debug(f"Removing '{file}'")
        os.remove(os.path.join(nginx_root, file))

logging.info("Building HTML files")
html_template_dir = ENVIRONMENT_VARIABLES["HTML_TEMPLATE_DIR"]
html_jinja_env = Environment(loader=FileSystemLoader(html_template_dir))
html_context = {
    "MINIBLOG_NAME": ENVIRONMENT_VARIABLES["HTML_MINIBLOG_NAME"],
}
html_output = html_jinja_env.get_template("index.html").render(html_context)
with open(os.path.join(nginx_root, "index.html"), "w") as index_file:
    logging.debug(f"Writing HTML file to '{os.path.join(nginx_root, 'index.html')}'")
    index_file.write(html_output)

# compress HTML files
#logging.info("Compressing HTML files")
#os.system("gzip -k -f -9 " + os.path.join("dist/html", "index.html"))
#os.remove(os.path.join("dist/html", "index.html"))

logging.info("Done building Miniblog")