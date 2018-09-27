from app import db

# Address field - needed to check if request is duplicate
# Time since last request - compare to this value before sending payload, limiting to 1 address per day
class AssetsRequest(db.Model):
    __tablename__ = "neo_faucet"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(64), index=True, unique=True, nullable=False)
    last_request_date = db.Column(db.DateTime(timezone=False), nullable=False)

    def __repr__(self):
        return '<Address {addr} last requested {dt}'.format(addr=self.address, dt=self.last_request_date)
