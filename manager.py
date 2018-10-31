# -*- coding: utf-8 -*-

from oct.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(
        host=app.config.get('SERVICE_HOST', 'localhost'),
        port=app.config.get('SERVICE_PORT', 5000))
