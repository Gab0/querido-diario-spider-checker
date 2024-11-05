#!/bin/python

import argparse
import os
import re
import pyaml
from urllib.parse import urlparse


known_base_spiders_with_allowed_urls = [
    "BaseAtendeV2Spider",
    "BaseDospSpider"
]


def parse_arguments():
    parser = argparse.ArgumentParser(description="Search for specific terms in files within a directory.")

    # Argument for list of search terms
    parser.add_argument(
        "--terms",
        nargs='+',
        default=["base_url", "url_base", "BASE_URL"],
        help="List of search terms (default: ['base_url', 'url_base', 'BASE_URL'])"
    )

    # Argument for root directory
    parser.add_argument(
        "--spider-dir",
        default='.',
        help="Root directory to start the search (default: current directory '.')"
    )

    return parser.parse_args()


def contar_ocorrencias(diretorio, terms):
    counter_names = {
        "confirmed_redundant_ad",
        "possible_redundant_ad",
        "has_ad_not_url",
        "missing",
        "total_spider_count",
        "no_ad_base_gazette",
        "no_ad_base_subclass"
    }
    seen_base_classes = {}
    counters = {c: 0 for c in counter_names}

    # Percorre todos os arquivos e subdiretórios
    for root, dirs, files in os.walk(diretorio):
        if "base" in root:
            continue
        for file in files:
            if "spider_checker" in file:
                continue

            counters["total_spider_count"] += 1

            # Verifica se o arquivo é um arquivo Python
            if file.endswith('.py'):
                caminho_arquivo = os.path.join(root, file)

                # Lê o conteúdo do arquivo
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()

                # Análise de cada arquivo:
                # Conta se a declaração de variável está presente ou não
                base_url = None
                for term in terms:
                    declaration = re.findall(rf"{term}\s*=\s*(.*)\n", conteudo)
                    if declaration:
                        base_url = declaration[0].strip("\"'")

                #T = any(x in conteudo for x in termos)
                allowed_domains_raw = re.findall(
                    r"allowed_domains\s*=\s*([^\]]+\])",
                    conteudo,
                    flags=re.MULTILINE
                )

                base_class = re.findall(r"Spider\((\w+)\):", conteudo)

                allowed_domains = []
                if allowed_domains_raw:
                    allowed_domains = eval(allowed_domains_raw[0])
                #print(f"{caminho_arquivo}\t{T}")
                if base_url and len(allowed_domains) == 1:
                    A = allowed_domains[0]
                    B = urlparse(base_url)
                    if A == B.netloc.replace("www.", ""):
                        counters["confirmed_redundant_ad"] += 1

                        if base_class:
                            bc = base_class[0]
                            if bc not in seen_base_classes:
                                seen_base_classes[bc] = set()
                            seen_base_classes[bc].add(file)
                    else:
                        counters["possible_redundant_ad"] += 1
                        # w = "-" * 10
                        # print(f"{w} Bad domain comparison:")
                        # print(f"{T} -> {B}")
                        # print(A)
                        # print(w)
                elif allowed_domains:
                    counters["has_ad_not_url"] += 1
                elif any(bc in conteudo for bc in known_base_spiders_with_allowed_urls):
                    pass
                elif "BaseGazetteSpider" in conteudo:
                    counters["no_ad_base_gazette"] += 1
                else:
                    counters["no_ad_base_subclass"] += 1

    print(
        f"Found {len(seen_base_classes)} different "
        "intermediate classes on Spiders with redundant 'allowed_domains'. "
        "Summary:"
    )
    print(pyaml.dumps(seen_base_classes))

    return counters


if __name__ == "__main__":
    arguments = parse_arguments()
    counters = contar_ocorrencias(arguments.spider_dir, arguments.terms)
    print(f"Variações para a variável 'base_url': {arguments.terms}")
    print(f"Quantidade de Spiders com 'allowed_domains' redundante: {counters['confirmed_redundant_ad']}")
    print(f"Quantidade de Spiders possivelmente afetadas: {counters['possible_redundant_ad']}")
    print(f"Quantidade de Spiders que declaram 'allowed_domains', mas com 'base_url' desconhecida: {counters['has_ad_not_url']}")
    print(f"Quantidade de Spiders sem 'allowed_domains' que usam a BaseGazetteSpider diretamente: {counters['no_ad_base_gazette']}")
    print(f"Quantidade de Spiders sem 'allowed_domains' que usam alguma subclasse de spider: {counters['no_ad_base_subclass']}")
    print(f"Quantidade total de spiders: {counters['total_spider_count']}")
