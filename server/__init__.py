from flask import Flask, render_template, request, redirect
import knowledge_extractor as ke
import MySQLdb
import json

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        qw = ke.lists
        a=[]
        #print 'qw type',type(qw)
        for every in qw:
            '''
            entity1 = every["entity1"]
            relation = every["relation"]
            entity2 = every["entity2"]
            '''
            #print '*****************888888888',every
            #print '###########',type(every)
            a.append(every)
        return render_template("semi.html",every=a)

@app.route('/save_er', methods=['POST'])
def saveEntityRelation():
    data = request.form.keys()[0]
    values = json.loads(data)
    if values:
        entity1 = values['e1']
        relation = values['rel']
        entity2 = values['e2']
        db = MySQLdb.connect("localhost", "keerthi", "test123", "testdb")
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO SEMI (entity1, relation, entity2) VALUES (%s,%s,%s);",(entity1,relation,entity2))
            db.commit()
            response = {'success':True}
        except:
            db.rollback()
            response = {'success':False}
    return json.dumps(response)





