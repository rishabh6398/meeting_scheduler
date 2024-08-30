from . import db
    
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('meetings', lazy=True))
    attendees = db.relationship('Attendee', secondary='meeting_attendee', backref=db.backref('meetings', lazy=True))

    def __repr__(self):
        return f'<Meeting {self.title}>'

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class MeetingAttendee(db.Model):
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), primary_key=True)
    attendee_id = db.Column(db.Integer, db.ForeignKey('attendee.id'), primary_key=True)
    meeting = db.relationship('Meeting', backref=db.backref('meeting_attendees', lazy=True))
    attendee = db.relationship('Attendee', backref=db.backref('meeting_attendees', lazy=True))