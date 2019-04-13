import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Model


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "features.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)


class Feature(db.Model):
    id_feature = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(80), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )
    product_area = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "Title: {}".format(self.title)


@app.route("/", methods=["GET", "POST"])
def home():
    id_feature = request.form.get("id_feature")
    if id_feature:
        update_feature = Feature(
            id_feature=request.form.get("id_feature"),
            title=request.form.get("title"),
            description=request.form.get("description"),
            client=request.form.get("client"),
            client_priority=request.form.get("client_priority"),
            target_date=datetime.strptime(request.form.get("target_date"), "%m/%d/%Y"),
            # target_date=request.form.get("target_date"),
            product_area=request.form.get("product_area"),
        )
        feature_new = Feature.query.filter_by(id_feature=id_feature).first()
        feature_new.title = update_feature.title
        feature_new.description = update_feature.description
        feature_new.client = update_feature.client
        feature_new.client_priority = update_feature.client_priority
        feature_new.target_date = update_feature.target_date
        feature_new.product_area = update_feature.product_area
        db.session.add(feature_new)

        # increment +1 with priority added is equal other priority with the same Client
        query = Feature.query.filter_by(client=feature_new.client).all()
        for priority in query:
            if priority.id_feature != feature_new.id_feature and int(
                priority.client_priority
            ) >= int(feature_new.client_priority):
                priority.client_priority = int(priority.client_priority) + 1
                db.session.add(priority)

    else:
        if request.form:
            feature = Feature(
                title=request.form.get("title"),
                description=request.form.get("description"),
                client=request.form.get("client"),
                client_priority=request.form.get("client_priority"),
                target_date=datetime.strptime(
                    request.form.get("target_date"), "%m/%d/%Y"
                ),
                # target_date=request.form.get("target_date"),
                product_area=request.form.get("product_area"),
            )
            db.session.add(feature)

            # increment +1 with priority added is equal other priority with the same Client
            query = Feature.query.filter_by(client=feature.client).all()
            for priority in query:
                if priority.id_feature != feature.id_feature and int(
                    priority.client_priority
                ) >= int(feature.client_priority):
                    priority.client_priority = int(priority.client_priority) + 1
                    db.session.add(priority)

    db.session.commit()
    features = Feature.query.filter().order_by("client_priority")
    return render_template("home.html", features=features)


@app.route("/update/<int:id_feature>/")
def update(id_feature):
    feature_update = Feature.query.filter_by(id_feature=id_feature).first()
    # db.session.add(feature)
    # db.session.commit()
    return render_template("/edit.html", feature=feature_update)


@app.route("/delete/<int:id_feature>/")
def delete(id_feature):
    feature_delete = Feature.query.filter_by(id_feature=id_feature).first()
    if feature_delete:
        # db.session.add(feature)
        db.session.delete(feature_delete)
        db.session.commit()
    features = Feature.query.filter().order_by("client_priority")
    return render_template("home.html", features=features, message=id_feature)


@app.errorhandler(404)
def page_not_found(error):
    features = Feature.query.filter().order_by("client_priority")
    return render_template("home.html", features=features), 404


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
