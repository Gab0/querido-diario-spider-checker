## About

Ferramenta simples projetada para examinar os Spiders do projeto [Querido Diário](https://github.com/okfn-brasil/querido-diario).

Ela abre o arquivo `.py` de cada spider e verifica duas coisas principais:

1. A propriedade `base_url` (ou algum nome alternativo conhecido) está declarada? 
2. A propriedade `allowed_domains` está declarada?

Então a ferramenta conta quantos Spiders estão na seguinte situação: 
sua propriedade `allowed_domains` declarada poderia ter sido extraída automaticamente de sua `base_url`.
Outras métricas secundárias também são computadas.


## Uso

Esse script não possui dependências, use com Python>=3.9;

Execute o script informando o caminho para a pasta 'spiders' do projeto `querido-diario`,
conforme o exemplo abaixo já com os logs para esse [commit](https://github.com/okfn-brasil/querido-diario/tree/cd9c37fc5117402c8191b59a51b7bba89bfc780e).

```
$ python spider_checker.py --spider-dir ../querido-diario/data_collection/gazette/spiders

Variações para a variável 'base_url': ['base_url', 'url_base', 'BASE_URL']
Quantidade de Spiders com 'allowed_domains' redundante: 219
Quantidade de Spiders possivelmente afetadas: 18
Quantidade de Spiders que declaram 'allowed_domains', mas com 'base_url' desconhecida: 60
Quantidade de Spiders sem 'allowed_domains' que usam a BaseGazetteSpider diretamente: 9
Quantidade de Spiders sem 'allowed_domains' que usam alguma subclasse de spider: 144
Quantidade total de spiders: 501
```
