# PyRedirect

A lightweight Flask application that redirects all incoming requests to a specified external URL while preserving the original path structure.

## Features

- **Universal Redirect**: Redirects all requests to a configurable external URL
- **Path Preservation**: Maintains the original URL path in the redirect
- **Request Logging**: Optional logging of all incoming requests with timestamps
- **Docker Support**: Ready-to-deploy Docker container
- **Production Ready**: Configured with Gunicorn for production deployment

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/khaliduzzamantanoy/Pyredirect.git
   cd Pyredirect
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure redirect URL**
   
   Edit `app.py` and replace `https://your-redirect-url/` with your target URL:
   ```python
   return redirect(f'https://example.com/{path}', code=302)
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t pyredirect .
   ```

2. **Run the container**
   ```bash
   docker run -p 5002:5002 pyredirect
   ```

   The application will be available at `http://localhost:5002`

## Configuration

### Redirect URL

To change the redirect destination, modify the `catch_all` function in `app.py`:

```python
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(f'https://your-new-url.com/{path}', code=302)
```

### Logging

Request logging is enabled by default. To disable it, comment out or remove the `@app.before_request` decorator and `log_requests()` function.

### Port Configuration

- **Development**: The app runs on port 5000 by default
- **Docker**: The container exposes port 5002
- **Production**: Configured with Gunicorn on port 5002

## How It Works

1. **Catch-All Route**: The application uses Flask's catch-all route pattern to capture any incoming request
2. **Path Preservation**: The original path is extracted and appended to the redirect URL
3. **302 Redirect**: Returns a temporary redirect (HTTP 302) to the configured external URL
4. **Request Logging**: Optionally logs all incoming requests with timestamps

### Example

If your redirect URL is `https://example.com/` and someone visits:
- `http://yourapp.com/about` → redirects to `https://example.com/about`
- `http://yourapp.com/api/users` → redirects to `https://example.com/api/users`
- `http://yourapp.com/` → redirects to `https://example.com/`

## Project Structure

```
Pyredirect/
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- **Flask**: Web framework for handling HTTP requests
- **Gunicorn**: WSGI HTTP server for production deployment

## Production Deployment

The application is configured to run with Gunicorn in production. The Docker container automatically uses:

```bash
gunicorn --bind 0.0.0.0:5002 app:app
```

For manual production deployment:

1. Install Gunicorn: `pip install gunicorn`
2. Run: `gunicorn --bind 0.0.0.0:5002 app:app`

## Security Considerations

- The application runs as a non-root user in the Docker container
- Consider implementing rate limiting for production use
- Monitor redirect targets to prevent malicious redirects
- Use HTTPS in production environments

## Use Cases

- **Domain Migration**: Redirect traffic from old domain to new domain
- **Maintenance Pages**: Temporarily redirect all traffic during maintenance
- **Load Balancing**: Simple traffic redirection to different servers
- **URL Shortening**: Base for building URL shortening services
- **A/B Testing**: Redirect traffic for testing purposes

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/khaliduzzamantanoy/Pyredirect/issues).

---

**Note**: Remember to replace `https://your-redirect-url/` in the code with your actual target URL before deployment.
