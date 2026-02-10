from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_filtered_characters():
    base_url = "https://rickandmortyapi.com/api/character"
    results = []
    # פילטר ראשוני דרך ה-API (חוסך זמן ורוחב פס)
    params = {
        "species": "human",
        "status": "alive"
    }
    
    url = base_url
    while url:
        response = requests.get(url, params=params if url == base_url else None)
        if response.status_code != 200:
            break
            
        data = response.json()
        
        for char in data.get('results', []):
            # סינון נוסף לפי המקור (Origin) שיהיה מכדור הארץ
            if "Earth" in char['origin']['name']:
                results.append({
                    "Name": char['name'],
                    "Location": char['location']['name'],
                    "Image": char['image']
                })
        
        # מעבר לעמוד הבא במידה וקיים
        url = data.get('info', {}).get('next')
        
    return results

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    # דרישת חובה לפי סעיף 27 בבונוס
    return jsonify({"status": "healthy"}), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    # החזרת הנתונים בפורמט JSON לפי סעיף 26 בבונוס
    try:
        characters = fetch_filtered_characters()
        return jsonify(characters), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # הרצה על 0.0.0.0 כדי שיהיה נגיש מחוץ ל-Container בהמשך
    app.run(host='0.0.0.0', port=5000)