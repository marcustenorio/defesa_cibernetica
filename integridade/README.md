# Aplicação de Integridade da Informação

Este projeto demonstra como utilizar funções hash para verificar a integridade de uma informação.

## Objetivo
Garantir que uma mensagem armazenada não tenha sido alterada.

## Funcionamento
1. O usuário digita uma mensagem.
2. A aplicação salva a mensagem em `mensagem.txt`.
3. A aplicação calcula o hash SHA-256 da mensagem.
4. O hash é salvo em `hash.txt`.
5. Posteriormente, a aplicação recalcula o hash da mensagem atual e compara com o hash original.

## Execução

```bash
python app.py

## Exemplo
Mensagem original: Ataque detectado no servidor
Hash gerado: 8f3b...

Se a mensagem for alterada, o novo hash será diferente, indicando quebra de integridade.
