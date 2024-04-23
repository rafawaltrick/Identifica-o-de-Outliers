---

# Identificação de Outliers em Transações Bancárias

Este é um programa simples em Python para identificar outliers em dados de transações bancárias. O código utiliza o método do Intervalo Interquartil (IQR) para identificar valores que estão significativamente diferentes do restante dos dados.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixar e instalar o Python a partir do [site oficial](https://www.python.org/).

2. Clone este repositório em sua máquina local usando o seguinte comando:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

3. Navegue até o diretório do projeto:

    ```
    cd nome-do-repositorio
    ```

4. Execute o script Python `analise.py`:

    ```
    python3 analise.py
    ```

5. O resultado será exibido no terminal, indicando se há outliers nos dados das transações bancárias ou não.

## Explicação do Código

O código Python `analise.py` realiza as seguintes etapas:

1. Define os dados das transações bancárias em uma lista.

2. Calcula os quartis Q1 e Q3 dos dados.

3. Calcula o Intervalo Interquartil (IQR).

4. Define limites inferior e superior para identificar outliers.

5. Identifica e lista os outliers, se houver, com base nos limites definidos.


