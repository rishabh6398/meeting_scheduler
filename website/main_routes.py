# website/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from . import db
from .models import Meeting, Attendee
from datetime import datetime

# Create a Blueprint instance
users_bp = Blueprint('users', __name__)

# Define routes for this Blueprint
@users_bp.route('/')
def index():
    print("Index route accessed")
    meetings = Meeting.query.all()
    return render_template('index.html', meetings=meetings)


@users_bp.route('/register_users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400

    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    existing_user = Attendee.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'User with this email already exists'}), 400

    new_user = Attendee(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@users_bp.route('/add', methods=['POST'])
def add_meeting():
    if request.method == 'POST':
        print("Add meeting route accessed")
        title = request.form.get('title')
        description = request.form.get('description')
        date_time = datetime.strptime(request.form.get('date_time'), '%Y-%m-%d %H:%M:%S')
        room_id = request.form.get('room_id')
        attendees = request.form.getlist('attendees')

        # Check for collisions
        existing_meetings = Meeting.query.filter_by(date_time=date_time).all()
        if existing_meetings:
            for meeting in existing_meetings:
                if meeting.room_id == room_id:
                    flash('Meeting conflicts with existing meeting')
                    return redirect(url_for('users.index'))

        # Check attendee availability
        for attendee in attendees:
            attendee_obj = Attendee.query.get(attendee)
            if not attendee_obj or not attendee_obj.is_available(date_time):
                flash('Attendee not available')
                return redirect(url_for('users.index'))

        new_meeting = Meeting(title=title, description=description, date_time=date_time, room_id=room_id, attendees=attendees)
        db.session.add(new_meeting)
        db.session.commit()
        flash('Meeting added successfully!')

        return redirect(url_for('users.index'))
    return render_template('add_meeting.html')

@users_bp.route('/delete/<int:id>', methods=['POST'])
def delete_meeting(id):
    print(f"Delete meeting route accessed with ID: {id}")
    meeting = Meeting.query.get(id)
    if meeting:
        db.session.delete(meeting)
        db.session.commit()
        flash('Meeting deleted successfully!')
    
    return redirect(url_for('users.index'))
