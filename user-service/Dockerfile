# Use the official Node.js image
FROM node:16

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json /app/

# Install the Node.js dependencies
RUN npm install

# Copy the rest of the source code
COPY . /app

# Expose the port that the app will run on (adjust based on your app's port)
EXPOSE 3001

# Command to run the app
CMD ["npm", "start"]
