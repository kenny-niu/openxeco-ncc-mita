from flask_restful import Resource
from flask_apispec import MethodResource
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.db import DB
from decorator.catch_exception import catch_exception
from decorator.log_request import log_request
from sqlalchemy.orm.exc import NoResultFound
from flask_apispec import doc


class GetMyCompanyCollaborators(MethodResource, Resource):

    def __init__(self, db: DB):
        self.db = db

    @log_request
    @doc(tags=['private'],
         description='Get the list of collaborators of the specified company',
         responses={
             "200": {},
             "422": {"description": "Object not found or you don't have the required access to it"},
         })
    @jwt_required
    @catch_exception
    def get(self, id_):

        try:
            self.db.session \
                .query(self.db.tables["UserCompanyAssignment"]) \
                .with_entities(self.db.tables["UserCompanyAssignment"].company_id) \
                .filter(self.db.tables["UserCompanyAssignment"].user_id == get_jwt_identity()) \
                .filter(self.db.tables["UserCompanyAssignment"].company_id == int(id_)) \
                .one()
        except NoResultFound:
            return "", "422 Object not found or you don't have the required access to it"

        subquery = self.db.session \
            .query(self.db.tables["UserCompanyAssignment"]) \
            .with_entities(self.db.tables["UserCompanyAssignment"].user_id) \
            .filter(self.db.tables["UserCompanyAssignment"].company_id == int(id_)) \
            .subquery()

        data = [r._asdict() for r in self.db.session
                .query(self.db.tables["User"])
                .with_entities(self.db.tables["User"].id,
                               self.db.tables["User"].email,
                               self.db.tables["User"].first_name,
                               self.db.tables["User"].last_name)
                .filter(self.db.tables["User"].id.in_(subquery))
                .all()]

        return data, "200 "
