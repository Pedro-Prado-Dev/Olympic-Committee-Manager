from app import db

athlete_medals = db.Table('athlete_medals',
                          db.Column('athlete_id', db.Integer, db.ForeignKey('athlete.id'), primary_key=True),
                          db.Column('medal_id', db.Integer, db.ForeignKey('medal.id'), primary_key=True)
                          )


class Medal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # 'Gold', 'Silver', 'Bronze'
    event = db.Column(db.String(100), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    athletes = db.relationship('Athlete', secondary=athlete_medals, backref=db.backref('medals', lazy=True))


'''
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    Nessa linha podemos ver uma relação 1 -> muitos onde cada medalha irá conter apenas um páis 
    enquanto Cada pais poderá ter diversas medalhas 
    athletes = db.relationship('Athlete', secondary=athlete_medals, backref=db.backref('medals', lazy=True)
    Nessa Linha vemos uma relação muitos -> muitos onde secundary seria a tabela de relação onde atletas e medalhas podem ter varias
    backref(O parâmetro backref na função relationship do SQLAlchemy cria uma relação bidirecional entre duas tabelas. Ele adiciona um atributo na classe relacionada que pode ser usado para acessar a tabela original.
No seu caso, backref=db.backref('medals', lazy=True) faz com que cada instância de Athlete tenha um atributo medals, permitindo acessar os medalhas associadas a um atleta diretamente a partir da instância de Athlete.)
'''
