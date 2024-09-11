from flask import Flask, jsonify
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

app = Flask(__name__)

# Initialize feature flag client and setup target
api_key = '8430c8fb-711f-4215-92b9-0f4c738a9899'
#client = CfClient(api_key)
#client.wait_for_initialization()

beta_testers = Target(identifier="test1", name="test1", attributes={"org": "blue"})

@app.route('/feature_flag_status', methods=['GET'])
def get_feature_flag_status():
    try:
        client = CfClient(api_key)
        client.wait_for_initialization()
      #  result = client.bool_variation("ChaosFeatureDemo", beta_testers)
        if client.is_initialized() is False:
            return jsonify({"status": "Failed to Initialise"}), 500
        return jsonify({"status": "Initialised"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989)
