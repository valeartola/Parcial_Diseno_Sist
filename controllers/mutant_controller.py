# controllers/mutant_controller.py
from flask import Flask, request, jsonify
from services.dna_service import is_mutant
from repositories.dna_repository import count_dna_records

app = Flask(__name__)

@app.route('/mutant/', methods=['POST'])
def mutant_endpoint():
    data = request.get_json()
    dna = data.get("dna")
    if not dna:
        return jsonify({"error": "DNA data missing"}), 400
    
    if is_mutant(dna):
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403

@app.route('/stats', methods=['GET'])
def stats_endpoint():
    mutant_count, human_count = count_dna_records()
    ratio = mutant_count / human_count if human_count > 0 else 0
    return jsonify({
        "count_mutant_dna": mutant_count,
        "count_human_dna": human_count,
        "ratio": ratio
    })
