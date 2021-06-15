from flask_restful import Resource
from flask_apispec import MethodResource
from db.db import DB
from exception.object_not_found import ObjectNotFound
from decorator.catch_exception import catch_exception


class GetPublicCompany(MethodResource, Resource):

    def __init__(self, db: DB):
        self.db = db

    @catch_exception
    def get(self, id_):

        c = self.db.tables["Company"]
        entities = c.id, c.name, c.is_startup, c.is_cybersecurity_core_business, c.rscl_number, c.creation_date, \
            c.description, c.website, c.image
        data = [o._asdict() for o in self.db.get(c, {"id": id_}, entities)]

        if len(data) < 1:
            raise ObjectNotFound

        data = data[0]
        data["creation_date"] = None if data["creation_date"] is None else str(data["creation_date"])

        data["taxonomy_assignment"] = [v[0] for v in self.db.get(
            self.db.tables["TaxonomyAssignment"],
            {"company": data['id']},
            [self.db.tables["TaxonomyAssignment"].taxonomy_value],
        )]

        return data, "200 "
