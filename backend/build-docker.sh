#!/bin/bash

# Tommy Timecrunch Backend - Docker Build & Run Script

echo "🏗️  Building Tommy Timecrunch Backend Docker Container..."

# Build the Docker image
docker build -t tommy-timecrunch-backend .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo ""
    echo "🚀 You can now run the container with:"
    echo ""
    echo "   # Run with Docker:"
    echo "   docker run -p 5000:5000 tommy-timecrunch-backend"
    echo ""
    echo "   # Or run with Docker Compose:"
    echo "   docker-compose up"
    echo ""
    echo "   # Run in background:"
    echo "   docker-compose up -d"
    echo ""
    echo "   # With Nginx reverse proxy:"
    echo "   docker-compose --profile production up"
    echo ""
    echo "📋 The API will be available at:"
    echo "   - http://localhost:5000 (direct)"
    echo "   - http://localhost:80 (with nginx)"
    echo ""
    echo "🧪 Test the API with:"
    echo "   curl http://localhost:5000/"
else
    echo "❌ Docker build failed!"
    exit 1
fi
