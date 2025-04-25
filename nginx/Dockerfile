# Use official nginx image
FROM nginx:alpine

# Remove default config (optional but clean)
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx.conf into container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
