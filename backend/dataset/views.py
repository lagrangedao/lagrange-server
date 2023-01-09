import os

from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend import db
from backend.obj_model.dataset import Dataset
from backend.obj_model.file import File
from backend.obj_model.user import get_user, User
from lagrange_server import app

dataset_bp = Blueprint(
    "dataset_bp", __name__, template_folder="templates", static_folder="static"
)


@app.route('/dataset', methods=['Get'])
@jwt_required()
def get_datasets():
    public_address = get_jwt_identity()
    user = get_user(public_address)
    datasets = Dataset.query.filter_by(user_id=user.id)
    data_list = []
    for dataset in datasets:
        data_list.append(dataset.to_dict())
    return jsonify(datasets=data_list), 200


@app.route('/dataset', methods=['POST'])
@jwt_required()
def create_dataset():
    public_address = get_jwt_identity()
    user: User = get_user(public_address)

    name = request.form.get("name")
    data_schema = request.form.get("data_schema")
    print(public_address)
    print(user.nonce)

    dataset = Dataset(name=name, data_schema=data_schema, user_id=user.id)
    db.session.add(dataset)
    db.session.commit()
    db.session.refresh(dataset)

    return jsonify(dataset=name), 200


@app.route('/dataset/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    files = File(uploaded_file.filename, os.path.abspath(path=uploaded_file.filename))
    return files.filename
