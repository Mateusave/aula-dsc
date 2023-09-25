class Produto:
    def __init__(self, nome, tipo_unidade, quantidade, preco):
        self.nome=nome
        self.tipo_unidade=tipo_unidade
        self.quantidade=quantidade
        self._preco=preco

    @property # getter
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, vl):
        if isinstance(vl, str):
            valor = vl.replace(' ','')
            valor = float(valor.replace('R$',''))
            self._preco = valor
        else:
            self._preco = vl

    def venda(self):
        quantidade = int(input('Digite a quantidade que você quer:'))
        print(f'produto {self.nome} x {quantidade} = {self.preco*quantidade}')

    def exibeProduto(self):
        print(f'produto: {self.nome}')
        print(f'quantidade: {self.quantidade} {self.tipo_unidade}')
        print(f'valor: R$ {self.preco: .2f}')

if __name__ == '__main__':
    prod1 = Produto('Coca-Cola', 'ml', 600 , 6.00)
    prod1.exibeProduto()
    prod1.venda()
