from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_apispec import MethodResource

from decorator.catch_exception import catch_exception
from decorator.log_request import log_request
from decorator.verify_admin_access import verify_admin_access
from decorator.verify_payload import verify_payload
from exception.object_not_found import ObjectNotFound


class DeleteDataControl(MethodResource, Resource):

    db = None

    def __init__(self, db):
        self.db = db

    @log_request
    @verify_payload([
        {'field': 'id', 'type': int}
    ])
    @jwt_required
    @verify_admin_access
    @catch_exception
    def post(self):
        input_data = request.get_json()

        data_control = self.db.get(self.db.tables["DataControl"], {"id": input_data["id"]})

        if len(data_control) > 0:
            self.db.delete(self.db.tables["DataControl"], {"id": input_data["id"]})
        else:
            raise ObjectNotFound

        return "", "200 "
