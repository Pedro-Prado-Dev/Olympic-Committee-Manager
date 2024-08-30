from app import create_app
from flask_session import Session

app = create_app()
Session(app)

if __name__ == '__main__':
    app.run(debug=True)

'''
Um Blueprint é uma forma de organizar e estruturar o código da sua aplicação Flask em componentes menores e reutilizáveis. 
Pense nele como um módulo ou uma parte da sua aplicação que pode conter suas próprias rotas, templates, e outros recursos. 
É especialmente útil para aplicações maiores, onde você quer manter o código limpo e organizado.

Por Que Usar Blueprints?
Organização: Mantém o código separado em módulos menores, facilitando a manutenção.
Reutilização: Você pode reutilizar um Blueprint em diferentes partes da aplicação ou até mesmo em diferentes projetos.
Modularidade: Permite que você divida a aplicação em partes lógicas, como "usuarios", "produtos", "pedidos", etc.
Como Funciona?
Definição: Você define um Blueprint para uma parte específica da sua aplicação.
Registro: Depois, você registra esse Blueprint na aplicação principal.

Benefícios
Separação de Preocupações: Cada Blueprint pode se concentrar em um aspecto específico da aplicação, como gerenciamento de usuários ou produtos.
Facilidade de Manutenção: O código é mais fácil de entender e modificar, pois está bem organizado.
Escalabilidade: Com a aplicação crescendo, você pode adicionar novos Blueprints sem complicar a estrutura existente.

'''