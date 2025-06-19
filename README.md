## Emoji Only Website – Backend

This is the backend service for the Emoji Only Website.
It is a FastAPI-based project that collects browser information sent from the frontend.
The information includes IP address, OS, platform, and other browser-level details.

## how to run
to run this repository, you will need `uv` which you can install from internet using
official documentation.

1. Clone the GitHub repository.
2. Enter the root directory where you will see the `src/` folder and `pyproject.toml` file.
3. Run the application using:

```bash
uv run uvicorn src.main:app
```

## project details

* The backend exposes one POST endpoint.
* The endpoint receives browser information in JSON format.
* Data is not stored persistently. It is processed immediately or logged depending on your configuration.
* Use Nginx or similar reverse proxy to forward real client IP addresses.

## related resources

* Frontend repository: `abdurahimovf18/emoji-only-website`
* Uses a public emoji API for rendering emojis in the frontend

## note

This is a one-time educational project. No persistent backend database is used. The public emoji API may become unavailable in the future.

## license

MIT
