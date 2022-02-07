import argparse
import logging
import os

import flask
import waitress

from flask import jsonify, Flask, request
from logging.config import dictConfig

logger = logging.getLogger()
def setup_logging():
    #dictConfig({
    #})    
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', 
        level=logging.DEBUG)

def jsonify_from_dict(d):
    #res = convert_object_for_json_dict(d)
    return jsonify(d)

def handle_calc_square():
    logger.info("handle_calc_square, starting")
    x = float(request.args.get('x', default="0"))
    res = {
        "x"       : x,
        "result"  : x,
    }
    if x > 10.0:
        os._exit(1)
    logger.info("handle_calc_square, finished")
    return jsonify_from_dict(res)

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.add_url_rule("/api/v1/calc_square", view_func=handle_calc_square, methods=["GET"])    

    return app

def run_server_fn(app, host: str, port: int):
    waitress.serve(app, host=host, port=port)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)

    return parser.parse_args()

def main():
    setup_logging()

    args = parse_args()
    app = create_app()
    run_server_fn(app, args.host, args.port)


if __name__ == "__main__":
    main()