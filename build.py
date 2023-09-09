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
NGINX_PATH=os.getenv("NGINX_PATH")
NGINX_SITES_AVAILABLE=os.getenv("NGINX_SITES_AVAILABLE")
NGINX_SERVER_NAME=os.getenv("NGINX_SERVER_NAME")
NGINX_LISTEN=os.getenv("NGINX_LISTEN")
NGINX_INDEX=os.getenv("NGINX_INDEX")
NGINX_ROOT=os.getenv("NGINX_ROOT")

logging.info("Cleaning up old nginx config files")
for file in os.listdir(NGINX_SITES_AVAILABLE):
    os.remove(os.path.join(NGINX_SITES_AVAILABLE, file))

logging.info("Creating new nginx config file")
nginx_jinja_env = Environment(loader=FileSystemLoader(NGINX_PATH))
nginx_context = {
    "NGINX_SERVER_NAME": NGINX_SERVER_NAME,
    "NGINX_LISTEN": NGINX_LISTEN,
    "NGINX_INDEX": NGINX_INDEX,
    "NGINX_ROOT": NGINX_ROOT,
}

nginx_output = nginx_jinja_env.get_template("nginx.conf").render(nginx_context)

with open(os.path.join(NGINX_SITES_AVAILABLE, NGINX_SERVER_NAME), "w") as nginx_file:
    nginx_file.write(nginx_output)

logging.info("Cleaning up old HTML files")
for file in os.listdir(NGINX_ROOT):
    if file.endswith(".html"):
        os.remove(os.path.join(NGINX_ROOT, file))

logging.info("Building HTML files")
html_jinja_env = Environment(loader=FileSystemLoader(HTML_PATH))

html_context = {
    "MINIBLOG_NAME": HTML_MINIBLOG_NAME,
}

html_output = html_jinja_env.get_template("index.html").render(html_context)

with open(os.path.join(NGINX_ROOT, "index.html"), "w") as index_file:
    index_file.write(html_output)


logging.info("Done building HTML Miniblog")
