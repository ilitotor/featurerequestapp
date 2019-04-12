from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from models import Feature
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        feature = Feature(
            title=request.form.get("title"),
            description=request.form.get("description"),
            client=request.form.get("client"),
            client_priority=request.form.get("client_priority"),
            target_date = datetime.strptime(request.form.get("target_date"), '%m/%d/%Y'),
            # target_date=request.form.get("target_date"),
            product_area=request.form.get("product_area"),
        )
        db.session.add(feature)
        db.session.commit()
    features = Feature.query.all()
    return render_template("home.html", features=features)


@app.route("/update", methods=["POST"])
def update():
    update_feature = Feature(
        id_feature=request.form.get("id_feature"),
        title=request.form.get("title"),
        description=request.form.get("description"),
        client=request.form.get("client"),
        client_priority=request.form.get("client_priority"),
        target_date = datetime.strptime(request.form.get("target_date"), '%m/%d/%Y'),
        # target_date=request.form.get("target_date"),
        product_area=request.form.get("product_area"),
    )
    feature = Feature.query.filter_by(id_feature=update_feature.id_feature).first()
    feature.title = update_feature.title
    feature.description = update_feature.description
    feature.client = update_feature.client
    feature.client_priority = update_feature.client_priority
    feature.target_date = update_feature.target_date
    feature.product_area = update_feature.product_area
    # db.session.add(feature)
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    delete_feature = Feature(
        id_feature=request.form.get("id_feature"),
    )
    feature_delete = Feature.query.filter_by(id_feature=delete_feature.id_feature).first()
    # db.session.add(feature)
    db.session.delete(feature_delete)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
