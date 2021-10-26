from flask import Flask, render_template,url_for,request,redirect
import customer_controller
import invoice_controller

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    customers = customer_controller.get_customers()
    return render_template('index.html',customers= customers)

@app.route('/form_add_customer')
def form_add_customer():
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:id>')
def edit_customer(id):
    customer = customer_controller.get_customer_id(id)
    return render_template('edit_customer.html', customer=customer)

@app.route('/delete_customer', methods=["POST"])
def delete_customer():
    customer_controller.delete_customer(request.form["id"])
    return redirect("/index")

@app.route('/save_customer', methods=['POST'])
def save_customer():
    name = request.form['name']
    document = request.form['document']
    status = request.form['status']
    phone = request.form['phone']
    customer_controller.add_customer(name, document, status, phone)
    return redirect('/')

@app.route('/update_customer', methods=['POST'])
def update_customer():
    id = request.form['id']
    name = request.form['name']
    document = request.form['document']
    status = request.form['status']
    phone = request.form['phone']
    customer_controller.update_customer(name, document, status, phone, id)
    return redirect('/')

@app.route('/invoices')
def invoices():
    invoices = invoice_controller.get_invoices()
    return render_template('invoices.html',invoices=invoices)

@app.route('/form_add_invoice')
def form_add_invoice():
    return render_template('add_invoice.html')

@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    number = request.form['number']
    document = request.form['document']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    invoice_controller.add_invoice(number,document, date, price, balance)
    return redirect('/invoices')

@app.route('/edit_invoice/<int:id>')
def edit_invoice(id):
    invoice = invoice_controller.get_invoice_id(id)
    return render_template('edit_invoice.html', invoice=invoice)

@app.route('/update_invoice', methods=['POST'])
def update_invoice():
    id = request.form['id']
    number = request.form['number']
    document = request.form['document']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    invoice_controller.update_invoice(number, document,  date, price, balance, id)
    return redirect('/invoices')

@app.route('/delete_invoice', methods=["POST"])
def delete_invoice():
    invoice_controller.delete_invoice(request.form["id"])
    return redirect("/invoices")

if __name__ == "__main__":
    app.run(port = 4500, debug=True)