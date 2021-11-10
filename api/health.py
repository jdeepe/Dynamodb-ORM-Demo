from flask import Blueprint

blueprint = Blueprint("health", __name__)


@blueprint.route("/", methods=["GET"])
def health():
    return "ok"
