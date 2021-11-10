from flask import Blueprint, Response, request

from settings import Config

from .models import Dataset

blueprint = Blueprint("dataset", __name__)


@blueprint.route("/", methods=["GET"])
def get_dataset():
    kwargs = request.json
    data_schema = Dataset.get(kwargs["name"])
    return dict(data_schema)


@blueprint.route("/", methods=["POST"])
def update_dataset():
    kwargs = request.json
    name = kwargs.pop("name")
    dataset = Dataset(name)
    actions = []
    try:
        for key in kwargs:
            if kwargs[key]:
                actions.append(getattr(Dataset, key).set(kwargs[key]))
            else:
                actions.append(getattr(Dataset, key).remove())
    except Exception as err:
        return Response(str(err), status=400)
    response = dataset.update(actions=actions)

    return {"data": {"updateDataSet": response}}


@blueprint.route("/delete", methods=["POST"])
def delete_dataset():
    kwargs = request.json
    data_schema = Dataset.get(kwargs["name"])
    data_schema.delete()
    return {"data": {"deleteDataSet": "Delete successful"}}


@blueprint.route("/list", methods=["POST"])
def list_dataset():
    kwargs = request.json
    filter_condition = kwargs["filter"] if kwargs and "filter" in kwargs else None
    limit = (
        kwargs["limit"] if kwargs and "limit" in kwargs else Config.DATASET_MAX_LIMIT
    )
    last_evaluated_key = (
        kwargs["nextToken"] if kwargs and "nextToken" in kwargs else None
    )

    response = {"listDataSets": {"items": [], "nextToken": None}}
    scan = Dataset.scan(
        limit=limit,
        filter_condition=filter_condition,
        last_evaluated_key=last_evaluated_key,
    )
    for data_schema in scan:
        response["listDataSets"]["items"].append(dict(data_schema))
    response["listDataSets"]["nextToken"] = scan.last_evaluated_key
    return {"data": response}


@blueprint.route("/count", methods=["POST"])
def count_dataset():

    scan = Dataset.count()
    response = {"countDataSets": scan}

    return {"data": response}
