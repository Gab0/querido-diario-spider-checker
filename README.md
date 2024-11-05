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

Found 11 different intermediate classes on Spiders with redundant 'allowed_domains'. Summary:
BaseAdiariosV1Spider:
  - pb_marizopolis.py
  - ce_itaitinga.py
  - ce_crateus.py
  - pb_serraria.py
  - ce_aurora.py
  - ce_jaguaribe.py
  - ce_caucaia.py
  - pb_sao_jose_dos_ramos.py
  - pb_riachao.py
  - ce_caririacu.py
  - ce_general_sampaio.py
  - pb_jacarau.py
  - ce_caninde.py
  - rn_pau_dos_ferros_2022.py
  - pb_tacima.py
  - ce_cedro.py
  - ma_itapecuru_mirim.py
  - ce_juazeiro_do_norte.py
  - pb_sertaozinho.py
  - ce_coreau.py
  - ma_buriticupu.py
  - pb_jerico.py
  - pb_piloezinhos.py
  - ce_hidrolandia.py

BaseAdiariosV2Spider:
  - rj_armacao_dos_buzios.py

BaseAplusSpider:
  - ma_codo.py
  - ma_peritoro.py
  - ma_bacabal.py
  - ma_santo_antonio_dos_lopes.py

BaseBarcoDigitalSpider:
  - to_tupirama.py
  - to_araguaina.py
  - to_recursolandia.py
  - to_tocantinopolis.py
  - to_lagoa_de_tocantins.py

BaseDiarioOficialBRSpider:
  - to_aguiarnopolis.py

BaseDionetSpider:
  - ro_jaru.py
  - es_serra.py
  - sp_sao_jose_dos_campos.py
  - rj_rio_de_janeiro.py
  - es_associacao_municipios.py

BaseGazetteSpider:
  - pr_foz_do_iguacu.py
  - ma_aldeias_altas.py
  - mt_rondonopolis.py
  - rj_marica.py
  - es_vila_velha.py
  - sp_sao_paulo.py
  - ms_campo_grande.py
  - mt_cuiaba.py
  - pr_sao_jose_pinhais.py
  - ma_caxias_2017.py
  - ba_barreiras.py
  - pa_belem.py
  - ma_sao_jose_dos_basilios.py
  - ap_macapa.py
  - sp_guarulhos.py
  - al_maragogi.py
  - ce_fortaleza.py

BaseImprensaOficialSpider:
  - ba_saude.py
  - ba_sao_felipe.py
  - ba_sao_felix.py
  - ba_gentio_do_ouro.py
  - ba_vera_cruz.py
  - ba_sao_francisco_do_conde.py
  - ba_amelia_rodrigues.py
  - ba_wenceslau_guimaraes.py
  - ba_pe_de_serra.py
  - ba_muniz_ferreira.py
  - ba_serrinha.py
  - ba_paratinga.py
  - ba_gongogi.py
  - ba_governador_mangabeira.py
  - ba_jaguarari.py
  - ba_xique_xique.py

BaseInstarSpider:
  - sp_alvares_florence.py
  - sp_pontes_gestal.py
  - ms_inocencia.py
  - rs_cachoeira_do_sul.py
  - pr_santo_antonio_do_paraiso.py
  - ms_costa_rica.py
  - sp_itaporanga.py
  - rs_sao_francisco_de_paula.py
  - sp_terra_roxa.py
  - sp_dracena.py
  - sp_itariri.py
  - mg_campo_belo.py
  - mg_nova_serrana.py
  - mg_itauna.py
  - sp_valinhos.py
  - mg_crucilandia.py
  - mg_salinas.py
  - mg_varzea_da_palma.py
  - sp_arapei.py
  - sp_coronel_macedo.py
  - sp_ibitinga.py
  - sp_sao_manuel.py
  - sp_marilia.py
  - sp_joao_ramalho.py
  - sp_lavinia.py
  - sp_uniao_paulista.py
  - mg_betim.py
  - sp_alto_alegre.py
  - sp_iracemapolis.py
  - sp_planalto.py
  - pr_sao_mateus_do_sul.py
  - sp_joanopolis.py
  - ms_maracaju.py
  - mg_onca_de_pitangui.py
  - sp_junqueiropolis.py
  - sp_santa_maria_da_serra.py
  - sp_nova_castilho.py
  - rs_vera_cruz.py
  - sp_irapuru.py
  - mg_carmo_da_cachoeira.py
  - sp_barbosa.py
  - sp_santa_ernestina.py
  - mg_piranguinho.py
  - sp_sao_pedro.py
  - sp_glicerio.py
  - sp_penapolis.py
  - sp_itapolis.py
  - sp_patrocinio_paulista.py
  - mg_candeias.py
  - pr_jaboti.py
  - sp_pratania.py
  - sp_vera_cruz.py
  - mg_juatuba.py
  - sp_valparaiso.py
  - sp_parisi.py
  - sp_jaboticabal.py
  - sp_igaracu_do_tiete.py
  - sp_pindorama.py
  - sp_votorantim.py
  - rs_cerrito.py
  - mt_cotriguacu.py
  - rs_camaqua.py
  - sp_itapirapua_paulista.py
  - mg_taiobeiras.py
  - sp_nova_luzitania.py
  - sp_piedade.py
  - sp_avanhandava.py
  - sp_itapui.py
  - sp_taquaral.py
  - sp_itobi.py
  - sp_andradina.py
  - sp_lagoinha.py
  - sp_aparecida.py
  - sp_eldorado.py
  - sp_general_salgado.py
  - sp_tapirai.py
  - sp_poloni.py
  - sp_barao_de_antonina.py
  - ms_bela_vista.py
  - sp_sarutaia.py
  - sp_porangaba.py
  - sp_turiuba.py
  - sp_luiziania.py
  - sp_monte_alto_2017.py
  - sp_monte_mor.py
  - sp_santo_andre.py
  - sp_charqueada.py
  - mg_januaria.py
  - sp_paulinia.py
  - sp_sebastianopolis_do_sul.py
  - sp_vinhedo.py
  - sp_iepe.py
  - sp_presidente_epitacio.py
  - sp_sao_roque.py
  - mg_carmo_do_rio_claro.py
  - pr_primeiro_de_maio.py
  - sp_aracariguama.py
  - sp_floreal.py
  - sp_brejo_alegre.py
  - rj_cabo_frio.py
  - sp_aguas_de_sao_pedro.py
  - sp_potirendaba.py
  - pr_antonio_olinto.py
  - sp_nhandeara.py
  - sp_mira_estrela.py
  - sp_ourinhos.py
  - sp_palmital.py
  - sp_macaubal.py
  - sp_mirante_do_paranapanema.py

BaseSaiSpider:
  - ba_apuarema.py
  - ba_anage.py
  - ba_correntina.py
  - ba_antas.py
  - al_igaci.py
  - ba_maragogipe.py
  - ba_abare.py
  - ba_riachao_das_neves.py
  - ba_aracas.py
  - ba_adustina.py
  - ba_jaborandi.py
  - ba_jeremoabo.py
  - ba_arataca.py
  - ba_aramari.py
  - ba_almadina.py
  - ba_lauro_de_freitas.py
  - se_estancia.py
  - ba_santa_luzia_2024.py
  - ba_andorinha.py
  - ba_luis_eduardo_magalhaes.py

BaseSiganetSpider:
  - ma_centro_do_guilherme.py
  - ma_ze_doca.py
  - ma_axixa.py
  - ma_viana.py
  - ma_boa_vista_do_gurupi.py
  - ma_coroata.py
  - ma_sao_vicente_ferrer.py

Variações para a variável 'base_url': ['base_url', 'url_base', 'BASE_URL']
Quantidade de Spiders com 'allowed_domains' redundante: 219
Quantidade de Spiders possivelmente afetadas: 18
Quantidade de Spiders que declaram 'allowed_domains', mas com 'base_url' desconhecida: 60
Quantidade de Spiders sem 'allowed_domains' que usam a BaseGazetteSpider diretamente: 9
Quantidade de Spiders sem 'allowed_domains' que usam alguma subclasse de spider: 144
Quantidade total de spiders: 501
```
