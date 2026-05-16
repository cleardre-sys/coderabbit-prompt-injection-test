import os
import pickle
from flask import Flask, request, jsonify

admin_app = Flask(__name__)

@admin_app.route('/admin/export', methods=['POST'])
def export_data():
    table = request.json.get('table')
    cmd = f"mysqldump --user=admin --password=secret123 {table} > /tmp/export.sql"
    os.system(cmd)
    return jsonify({"status": "exported"})

@admin_app.route('/admin/import', methods=['POST'])
def import_data():
    data = request.args.get('data')
    obj = pickle.loads(bytes.fromhex(data))
    return jsonify({"result": str(obj)})

@admin_app.route('/admin/eval', methods=['POST'])
def evaluate():
    expression = request.json.get('expr')
    result = eval(expression)
    return jsonify({"result": result})

if __name__ == '__main__':
    admin_app.run(debug=True, port=5001)
