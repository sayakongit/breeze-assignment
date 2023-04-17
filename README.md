---
title: Breeze Assignment
description: An endpoint with Python to reverse a string
tags:
  - fastapi
  - python
---

# FastAPI Example

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/-NvLj4?referralCode=milo)
## ✨ Features

- FastAPI
- Python 3

## 💁‍♀️ How to use

- Deploy using the button 👆
- Clone locally and install packages with Pip using `pip install -r requirements.txt` or Poetry using `poetry install`
- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`

## :rocket: Endpoints

- '/': The root endpoint which shows a welcome message!
- '/reverse': The POST endpoint where users can enter a string and get the reversed string in response.
- '/docs': Opens the Swagger Interactive UI to try out the APIs.

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/).
- FastAPI provides automatic documentation to call and test your API directly from the browser. You can access it at `/docs` with [Swagger](https://github.com/swagger-api/swagger-ui) or at `/redoc` with [Redoc](https://github.com/Rebilly/ReDoc).
