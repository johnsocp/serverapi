from flask import Flask, jsonify, abort
import salt.client

app = Flask(__name__)

@app.route('/v1.0/minions')
def list_minions():
	client = salt.client.LocalClient()
	ret = client.cmd('*', 'grains.items', ['--out json'])
	return ret

@app.route('/v1.0/users', methods = ['GET'])
def get_users():
	
    return jsonify( {'tasks': tasks} )

@app.route('/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': task[0] } )

if __name__ == '__main__':
	app.run(debug = True, host='10.177.38.20', port=8000)
