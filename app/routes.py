from app.models import Feature
from app import db

from datetime import datetime
from flask import render_template, request

def load(app):
    def update_priority(new_feature):
        query = (
            Feature.query.filter_by(client=new_feature.client, client_priority=new_feature.client_priority)
                .order_by("client_priority")
                .all()
        )
        for feature in query:
            if (int(feature.id_feature) != int(new_feature.id_feature)):
                feature.client_priority = (int(feature.client_priority) + 1)
                db.session.add(feature)
                update_priority(feature)

    def update_feature(id_feature):
        new_feature = Feature(
            id_feature=request.form.get("id_feature"),
            title=request.form.get("title"),
            description=request.form.get("description"),
            client=request.form.get("client"),
            client_priority=request.form.get("client_priority"),
            target_date=datetime.strptime(request.form.get("target_date"), "%m/%d/%Y"),
            product_area=request.form.get("product_area"),
        )
        feature_update = Feature.query.filter_by(id_feature=id_feature).first()
        feature_update.title = new_feature.title
        feature_update.description = new_feature.description
        feature_update.client = new_feature.client
        feature_update.client_priority = new_feature.client_priority
        feature_update.target_date = new_feature.target_date
        feature_update.product_area = new_feature.product_area
        db.session.commit()
        # increment +1 with priority added is equal other priority with the same Client
        update_priority(new_feature)

    def create_feature():
        new_feature = Feature(
            title=request.form.get("title"),
            description=request.form.get("description"),
            client=request.form.get("client"),
            client_priority=request.form.get("client_priority"),
            target_date=datetime.strptime(
                request.form.get("target_date"), "%m/%d/%Y"
            ),
            product_area=request.form.get("product_area"),
        )
        db.session.add(new_feature)
        # increment +1 with priority added is equal other priority with the same Client
        update_priority(new_feature)
        db.session.commit()

    @app.route("/", methods=["GET", "POST"])
    def home():
        id_feature = request.form.get("id_feature")
        if id_feature:
            update_feature(id_feature)
        else:
            if request.form:
                create_feature()

        db.session.commit()
        features = Feature.query.filter().order_by("client_priority")
        return render_template("home.html", features=features)

    @app.route("/update/<int:id_feature>/")
    def update(id_feature):
        feature_update = Feature.query.filter_by(id_feature=id_feature).first()
        return render_template("/edit.html", feature=feature_update)

    @app.route("/delete/<int:id_feature>/")
    def delete(id_feature):
        feature_delete = Feature.query.filter_by(id_feature=id_feature).first()
        if feature_delete:
            db.session.delete(feature_delete)
            db.session.commit()
        features = Feature.query.filter().order_by("client_priority")
        return render_template("home.html", features=features, message=id_feature)

    @app.errorhandler(404)
    def page_not_found(error):
        features = Feature.query.filter().order_by("client_priority")
        return render_template("home.html", features=features), 404

    return app