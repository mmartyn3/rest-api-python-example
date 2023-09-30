# rest-api-python-example
Example Flask app demonstrating setting up Python-based REST API and how to interact with it using Postman.

## Table of Contents

- [Prerequisites](#prerequisites)
- [GET: Retrieve All Blog Posts](#get-retrieve-all-blog-posts)
- [POST: Create a New Blog Post](#post)
- [DELETE: Remove a Blog Post](#delete)
- [PUT: Update a Blog Post](#put)
- [License](#license)

## Prerequisites

Make sure you have installed Postman.

Make sure you set up the virtual environment (`python3 -m venv venv` then `source venv/bin/activate` then `pip install -r requirements.txt`)

Your Flask Blog API should be running (activate the virtual environment by `source venv/bin/activate` then `python api.py`)

## Geting Postman set up

You can either try to manually enter the API endpoint details into Postman (see details for each endpoint below), or you can import the API into Postman by dragging and dropping Simple_Flask_REST-API_example.postman_collection.json into the Postman app to automatically create all of the endpoints.

## GET: Retrieve All Blog Posts

- Open Postman.
- Create a new request.
- Select the request type as GET.
- Enter your API URL (e.g., http://127.0.0.1:5000/api/v1/blogs).
- Click Send.

You should receive a 200 OK status and a list of all blog posts in the response body.

## POST: Create a New Blog Post

- Create a new request.
- Select the request type as POST.
- Enter your API URL (e.g., http://127.0.0.1:5000/api/v1/blogs).
- In the Body tab, select x-www-form-urlencoded.
- Add the title and content key-value pairs to represent the title and content of the new blog post.
- Click Send.
- You should receive a 201 Created status and a success message with the ID of the newly created post.

## DELETE: Remove a Blog Post

- Create a new request.
- Select the request type as DELETE.
- Enter your API URL (e.g., http://127.0.0.1:5000/api/v1/blogs).
- In the Params tab, add a new parameter with the key id and the value of the post you want to delete.
- Click Send.
- You should receive a 200 OK status and a success message indicating that the post was deleted.

## PUT: Update a Blog Post

- Create a new request.
- Select the request type as PUT.
- Enter your API URL (e.g., http://127.0.0.1:5000/api/v1/blogs).
- In the Params tab, add a new parameter with the key id and the value of the post you want to update.
- In the Body tab, select x-www-form-urlencoded.
- Optionally add the title and/or content key-value pairs to update.
- Click Send.
- You should receive a 200 OK status and a success message indicating that the post was updated.

## License

[MIT License](LICENSE)
