from flask import Blueprint, Response, request

from settings import Config

from .models import DataSchema

blueprint = Blueprint("dataschema", __name__)


@blueprint.route("/", methods=["GET"])
def get_dataschema():
    kwargs = request.json
    data_schema = DataSchema.get(kwargs["name"])
    return dict(data_schema)


@blueprint.route("/", methods=["POST"])
def update_dataschema():
    kwargs = request.json
    name = kwargs.pop("name")
    data_schema = DataSchema(name)
    actions = []
    try:
        for key in kwargs:
            if kwargs[key]:
                actions.append(getattr(DataSchema, key).set(kwargs[key]))
            else:
                actions.append(getattr(DataSchema, key).remove())
    except Exception as err:
        return Response(str(err), status=400)
    response = data_schema.update(actions=actions)

    return {"data": {"updateDataSchema": response}}


@blueprint.route("/delete", methods=["POST"])
def delete_dataschema():
    kwargs = request.json
    data_schema = DataSchema.get(kwargs["name"])
    data_schema.delete()
    return {"data": {"deleteDataSchema": "Delete successful"}}


@blueprint.route("/list", methods=["POST"])
def list_dataschema():
    kwargs = request.json
    filter_condition = kwargs["filter"] if "filter" in kwargs else None
    limit = kwargs["limit"] if "limit" in kwargs else Config.DATASET_MAX_LIMIT
    last_evaluated_key = kwargs["nextToken"] if "nextToken" in kwargs else None

    response = {"listDataSchemas": {"items": [], "nextToken": None}}
    scan = DataSchema.scan(
        limit=limit,
        filter_condition=filter_condition,
        last_evaluated_key=last_evaluated_key,
    )
    for data_schema in scan:
        response["listDataSchemas"]["items"].append(dict(data_schema))
    response["listDataSchemas"]["nextToken"] = scan.last_evaluated_key
    return {"data": response}


@blueprint.route("/count", methods=["POST"])
def count_dataschema():

    scan = DataSchema.count()
    response = {"countDataSchema": scan}
    return {"data": response}
