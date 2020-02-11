# -*- encoding: utf-8 -*-

from vncorenlp import VnCoreNLP
from flask import Flask, request
from flask import jsonify
import json
import unicodedata



vncorenlp_file = 'VnCoreNLP-1.1.1.jar'
postagger = VnCoreNLP(vncorenlp_file, annotators='wseg, pos')


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/get_postag', methods = ['POST'])
def get_posttag():
    global vncorenlp_file, postagger

    data = unicodedata.normalize('NFKC', request.data.decode())
    data = json.loads(data)['data']

    pos = postagger.pos_tag(data)
    response = {'result' : pos}
    return jsonify(response)




if __name__ == '__main__':
    sen = u'nâng_cao ý_thức phòng, chống dịch do virus_corona gây_ra'
    print(get_posttag(sen))
    postagger.close()