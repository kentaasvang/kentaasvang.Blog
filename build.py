#!./venv/bin/python
import os
import logging
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

if not load_dotenv():
    raise Exception("Could not load .env file")

logging.basicConfig(level=logging.INFO)

logging.info("Building HTML Miniblog")
DEVELOPMENT=os.getenv("DEVELOPMENT").lower() == "true"

# *** HTML variables ***
HTML_MINIBLOG_NAME=os.getenv("HTML_MINIBLOG_NAME")
HTML_PATH=os.getenv("HTML_PATH")

# *** Nginx variables ***
NGINX_CONF_PATH=os.getenv("NGINX_CONF_PATH")
NGINX_SITES_AVAILABLE=os.getenv("NGINX_SITES_AVAILABLE")
NGINX_SERVER_NAME=os.getenv("NGINX_SERVER_NAME")
NGINX_LISTEN=os.getenv("NGINX_LISTEN")
NGINX_INDEX=os.getenv("NGINX_INDEX")
NGINX_ROOT=os.getenv("NGINX_ROOT")

logging.info("Cleaning up old nginx config files")
for file in os.listdir(NGINX_SITES_AVAILABLE):
    os.remove(os.path.join(NGINX_SITES_AVAILABLE, file))

logging.info("Creating new nginx config file")
with open(NGINX_CONF_PATH, "r") as nginx_template_file:
    nginx_template_content = nginx_template_file.read()
    nginx_template_content = nginx_template_content.replace("[NGINX_SERVER_NAME]", NGINX_SERVER_NAME)
    nginx_template_content = nginx_template_content.replace("[NGINX_LISTEN]", NGINX_LISTEN)
    nginx_template_content = nginx_template_content.replace("[NGINX_INDEX]", NGINX_INDEX)
    nginx_template_content = nginx_template_content.replace("[NGINX_ROOT]", NGINX_ROOT)

    new_nginx_conf_file = os.path.join(NGINX_SITES_AVAILABLE, NGINX_SERVER_NAME.lower())
    with open(new_nginx_conf_file, "w") as nginx_conf_file:
        nginx_conf_file.write(nginx_template_content)

logging.info("Cleaning up old HTML files")
for file in os.listdir(NGINX_ROOT):
    if file.endswith(".html"):
        os.remove(os.path.join(NGINX_ROOT, file))

logging.info("Building HTML files")
jinja_env = Environment(loader=FileSystemLoader(HTML_PATH))
data = {
    "MINIBLOG_NAME": HTML_MINIBLOG_NAME,
}

output = jinja_env.get_template("index.html").render(data)

with open(os.path.join(NGINX_ROOT, "index.html"), "w") as index_file:
    index_file.write(output)


logging.info("Done building HTML Miniblog")