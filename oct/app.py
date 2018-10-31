# -*- coding: utf-8 -*-

from flask import Flask

def create_app(config=None):
    config = config or {}
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.update(config)

    @app.route('/')
    def index():
        return 'This is app start index'

    return app


__all__ = ['create_app']
