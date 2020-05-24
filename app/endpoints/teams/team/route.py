from flask import request
from app import db
from app.model.teams import TeamModel
from flask import current_app as app


@app.route('/api/v1/teams/<team_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def handle_team(team_id):
    team = TeamModel.query.get_or_404(team_id)

    if request.method == 'GET':
        response = {
            "id": team.id,
            "name": team.name,
            "location": team.location,
        }
        return {"message": "success", "team": response}

    elif request.method == 'PUT':
        data = request.get_json()
        team.name = data['name']
        team.location = data['location']
        team.premierships = data['premierships']
        team.wooden_spoons = data['wooden_spoons']
        team.years_in_afl = data['years_in_afl']
        db.session.add(team)
        db.session.commit()
        return {"message": f"Team {team.name} successfully updated"}

    elif request.method == 'PATCH':
        data = request.get_json()
        if 'name' in data : team.name = data['name']
        if 'location' in data: team.location = data['location']
        if 'premierships' in data: team.premierships = data['premierships']
        if 'wooden_spoons' in data: team.wooden_spoons = data['wooden_spoons']
        if 'years_in_afl' in data: team.years_in_afl = data['years_in_afl']
        db.session.add(team)
        db.session.commit()
        return {"message": f"Team {team.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Team {team.name} successfully deleted."}