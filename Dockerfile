# Use the official Nginx image as the base image
FROM nginx:1.18.0

# Copy your static files to the Nginx container
# COPY ./path/to/your/static/files /usr/share/nginx/html

# Expose port 80 to be accessible from the host
EXPOSE 80