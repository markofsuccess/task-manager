{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":62,"column":0},"end":{"row":66,"column":59},"action":"insert","lines":["@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","                           category=mongo.db.categories.find_one(","                           {'_id': ObjectId(category_id)}))"],"id":2}],[{"start":{"row":67,"column":0},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":68,"column":0},"end":{"row":73,"column":46},"action":"insert","lines":["@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))"],"id":4}],[{"start":{"row":73,"column":46},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]},{"start":{"row":74,"column":4},"end":{"row":75,"column":0},"action":"insert","lines":["",""]},{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":75,"column":0},"end":{"row":78,"column":46},"action":"insert","lines":["@app.route('/delete_category/<category_id>')","def delete_category(category_id):","    mongo.db.categories.remove({'_id': ObjectId(category_id)})","    return redirect(url_for('get_categories'))"],"id":7}]]},"ace":{"folds":[],"scrolltop":952,"scrollleft":0,"selection":{"start":{"row":78,"column":46},"end":{"row":78,"column":46},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1573827674831,"hash":"a660371055ee95d0f6368d90c175b20e4929ef4a"}