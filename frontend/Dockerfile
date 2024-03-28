# Use an official lightweight version of Nginx
FROM nginx:alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY . /usr/share/nginx/html

# Expose port 8000
EXPOSE 8000

# Start Nginx when the container has provisioned.
CMD ["python", "-m", "http.server"]
