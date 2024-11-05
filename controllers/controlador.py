from flask import Blueprint, request, jsonify
from services.servicio import MutantService

mutant_blueprint = Blueprint("mutant", __name__)
service = MutantService()

@mutant_blueprint.route('/mutant/', methods=['POST'])
def is_mutant():
    data = request.get_json()
    dna = data.get("dna")
    
    if not dna:
        return jsonify({"error": "ADN no proporcionado"}), 400

    if service.check_dna(dna):
        return jsonify({"message": "Mutante detectado"}), 200
    else:
        return jsonify({"message": "No mutante"}), 403

@mutant_blueprint.route('/stats', methods=['GET'])
def stats():
    stats_data = service.get_statistics()
    return jsonify(stats_data), 200


@mutant_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200
