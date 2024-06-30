from flask import Flask
from flask import request
from file_handler import FileHandler

app = Flask(__name__)
file_handler = FileHandler()


# IMAGES
@app.route('/controller/tablestruct/img', methods=['POST'])
def get_table_struct_img():
    file = request.form['data']
    cols_list, drawed_page = file_handler.extract_cells_from_img(file)
    d = {'cells': cols_list, 'image': drawed_page}
    return d


@app.route('/controller/recognise/easyocr/img', methods=['POST'])
def recognise_table_img():
    file = request.form['data']
    return file_handler.read_from_img(file)


# PDFs
@app.route('/controller/tablestruct/pdf', methods=['POST'])
def get_table_structure_pdf():
    file = request.form['data']
    cols_list, drawed_pages = file_handler.extract_cells_from_pdf(file)
    d = {'cells': cols_list, 'image': drawed_pages}
    return d


@app.route('/controller/recognise/easyocr/pdf', methods=['POST'])
def recognise_table_pdf():
    file = request.form['data']
    tables = file_handler.read_from_pdf(file)
    d = {'tables': tables}
    return d


if __name__ == "__main__":
    app.run(debug=True)
