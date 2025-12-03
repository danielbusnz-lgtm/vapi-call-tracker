from flask import Flask, request, jsonify, render_template
from database import init_db, save_call, get_all_calls


app= Flask(__name__)
init_db()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data.get('message', {}).get('type') == 'end-of-call-report':
        call_info = {
            'call_id': data['message']['call']['id'],
            'phone_number': data['message']['call'].get('phoneNumber', 'Unknown'),
            'duration': data['message']['call'].get('duration', 0),
            'transcript': data['message'].get('transcript', ''),
            'summary': data['message'].get('summary', ''),
            'cost': data['message']['call'].get('cost', 0)
        }

        save_call(call_info)
        print(f"Saved call {call_info['call_id']}")

    return jsonify({'status': 'success'})


@app.route('/dashboard')
def dashboard():
    calls = get_all_calls()
    return render_template('dashboard.html', calls=calls)



if __name__=="__main__":
    import os 
    port = int(os.environ.get('PORT',3000))
    app.run(host='0.0.0.0',port=port,debug=False)













