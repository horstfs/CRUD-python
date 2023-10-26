import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    marca = Column(String(255))
    preco_compra = Column(Float)
    preco_venda = Column(Float)
    data_compra = Column(Date)
    quantidade_estoque = Column(Integer)

class ProductEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Editor de Produtos')
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Nome', 'Marca', 'Preço Compra', 'Preço Venda', 'Data Compra', 'Quantidade Estoque'])

        self.edit_button = QPushButton('Editar')
        self.edit_button.clicked.connect(self.edit_product)

        self.delete_button = QPushButton('Excluir')
        self.delete_button.clicked.connect(self.delete_product)

        self.layout.addWidget(self.table)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)

        self.central_widget.setLayout(self.layout)

    def load_data(self):
        engine = create_engine('mysql://root:@localhost/estoque_db')
        Session = sessionmaker(bind=engine)
        session = Session()

        products = session.query(Product).all()

        self.table.setRowCount(len(products))
        for row, product in enumerate(products):
            self.table.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.table.setItem(row, 1, QTableWidgetItem(product.nome))
            self.table.setItem(row, 2, QTableWidgetItem(product.marca))
            self.table.setItem(row, 3, QTableWidgetItem(str(product.preco_compra)))
            self.table.setItem(row, 4, QTableWidgetItem(str(product.preco_venda)))
            self.table.setItem(row, 5, QTableWidgetItem(str(product.data_compra)))
            self.table.setItem(row, 6, QTableWidgetItem(str(product.quantidade_estoque)))

    def edit_product(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            product_id = int(self.table.item(selected_row, 0).text())
            dialog = ProductDialog(product_id)
            if dialog.exec_():
                self.load_data()

    def delete_product(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            product_id = int(self.table.item(selected_row, 0).text())

            engine = create_engine('mysql://root:@localhost/estoque_db')
            Session = sessionmaker(bind=engine)
            session = Session()

            product = session.query(Product).filter_by(id=product_id).first()
            if product:
                session.delete(product)
                session.commit()
                self.load_data()

class ProductDialog(QDialog):
    def __init__(self, product_id):
        super().__init__()

        self.product_id = product_id

        self.setWindowTitle('Editar Produto')
        self.setGeometry(200, 200, 400, 200)

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.name_label = QLabel('Nome:')
        self.name_input = QLineEdit()

        self.brand_label = QLabel('Marca:')
        self.brand_input = QLineEdit()

        self.purchase_price_label = QLabel('Preço Compra:')
        self.purchase_price_input = QLineEdit()

        self.sale_price_label = QLabel('Preço Venda:')
        self.sale_price_input = QLineEdit()

        self.purchase_date_label = QLabel('Data Compra:')
        self.purchase_date_input = QLineEdit()

        self.stock_quantity_label = QLabel('Quantidade Estoque:')
        self.stock_quantity_input = QLineEdit()

        self.save_button = QPushButton('Salvar')
        self.save_button.clicked.connect(self.save_product)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.brand_label)
        self.layout.addWidget(self.brand_input)
        self.layout.addWidget(self.purchase_price_label)
        self.layout.addWidget(self.purchase_price_input)
        self.layout.addWidget(self.sale_price_label)
        self.layout.addWidget(self.sale_price_input)
        self.layout.addWidget(self.purchase_date_label)
        self.layout.addWidget(self.purchase_date_input)
        self.layout.addWidget(self.stock_quantity_label)
        self.layout.addWidget(self.stock_quantity_input)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def load_data(self):
        engine = create_engine('mysql://root:@localhost/estoque_db')
        Session = sessionmaker(bind=engine)
        session = Session()

        product = session.query(Product).filter_by(id=self.product_id).first()

        if product:
            self.name_input.setText(product.nome)
            self.brand_input.setText(product.marca)
            self.purchase_price_input.setText(str(product.preco_compra))
            self.sale_price_input.setText(str(product.preco_venda))
            self.purchase_date_input.setText(str(product.data_compra))
            self.stock_quantity_input.setText(str(product.quantidade_estoque))

    def save_product(self):
        name = self.name_input.text()
        brand = self.brand_input.text()
        purchase_price = float(self.purchase_price_input.text())
        sale_price = float(self.sale_price_input.text())
        purchase_date = self.purchase_date_input.text()
        stock_quantity = int(self.stock_quantity_input.text())

        engine = create_engine('mysql://root:@localhost/estoque_db')
        Session = sessionmaker(bind=engine)
        session = Session()

        product = session.query(Product).filter_by(id=self.product_id).first()

        if product:
            product.nome = name
            product.marca = brand
            product.preco_compra = purchase_price
            product.preco_venda = sale_price
            product.data_compra = purchase_date
            product.quantidade_estoque = stock_quantity

            session.commit()
            self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ProductEditor()
    editor.show()
    sys.exit(app.exec_())
