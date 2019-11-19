import psycopg2, requests, time
from bs4 import BeautifulSoup
try:

    ##create relation between region and province
    connection = psycopg2.connect(user = "postgres",
                                  password = "281094",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "gobierno")

    cursor = connection.cursor()

    urlsregions=["https://infogob.jne.gob.pe/Localidad/Peru/tumbes_procesos-electorales_YB3y3ZIJ5Eo%3d3Z",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura_procesos-electorales_4Yk40iZw0%2bM%3dki",
    "https://infogob.jne.gob.pe/Localidad/Peru/lambayeque_procesos-electorales_QtGacCvkvw%3d%3dM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca_procesos-electorales_SHD5KdvhNg%3d%3d72",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas_procesos-electorales_6%2b%400ElOxMA%3d%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto_procesos-electorales_jp5dTJU18lE%3d5J",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin_procesos-electorales_Gidr2ZmWBg%3d%3dpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad_procesos-electorales_tyRXas6Ang%3d%3d7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash_procesos-electorales_vSVfI5WDSjI%3dV5",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco_procesos-electorales_Vf9s%407S25fM%3d97",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali_procesos-electorales_k9fCuVKnNQc%3dfV",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima_procesos-electorales_HzGaFcJbgN8%3dGc",
    "https://infogob.jne.gob.pe/Localidad/Peru/pasco_procesos-electorales_wsJDUFcy3IM%3dJF",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin_procesos-electorales_p6lvGTJpDDA%3dlT",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica_procesos-electorales_FACDH52llu4%3dC5",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica_procesos-electorales_14QCLCLkpg%3d%3dei",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho_procesos-electorales_6%2b%400ElOxMA%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac_procesos-electorales_6%2b%400ElOxMA%3d%3dqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco_procesos-electorales_Jm30C5wvkZc%3d35",
    "https://infogob.jne.gob.pe/Localidad/Peru/madre-de-dios_procesos-electorales_n8Vxc%40DZGQ%3d%3dA2",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa_procesos-electorales_6%2b%400ElOxMA%3d%3dHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno_procesos-electorales_oKzUifBsMHI%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/moquegua_procesos-electorales_6%2b%400ElOxMA%3d%3d1%40",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna_procesos-electorales_rtoGjYiUciM%3doY",
    "https://infogob.jne.gob.pe/Localidad/Peru/callao_procesos-electorales_ewhD5iRlGbk%3dhi"]

    urlsprovinces=["https://infogob.jne.gob.pe/Localidad/Peru/tumbes/contralmirante-villar_procesos-electorales_G2KvFYuVJxE%3d8T",
    "https://infogob.jne.gob.pe/Localidad/Peru/tumbes/tumbes_procesos-electorales_Bz%40ibVOShQ%3d%3dC3",
    "https://infogob.jne.gob.pe/Localidad/Peru/tumbes/zarumilla_procesos-electorales_gIERwAoaUg%3d%3dum",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/talara_procesos-electorales_zx3pbHYdlw%3d%3dvl",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/sullana_procesos-electorales_fRuSNIrKYg%3d%3dcC",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/paita_procesos-electorales_XW3XhNxb4w%3d%3d2C",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/piura_procesos-electorales_5rFopKl4KA%3d%3dwn",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/sechura_procesos-electorales_6IYN4hYz7A%3d%3dBa",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/morropon_procesos-electorales_hhMkaVfifw%3d%3dPs",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/huancabamba_procesos-electorales_gRzr7%40QSU7Ewvb",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura/ayabaca_procesos-electorales_cBY%40AFyRBA%3d%3dME",
    "https://infogob.jne.gob.pe/Localidad/Peru/lambayeque/lambayeque_procesos-electorales_ew4gPAzV%40k3rM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/lambayeque/ferre%C3%B1afe_procesos-electorales_3VQNFDoJ2V9CM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/lambayeque/chiclayo_procesos-electorales_XjbcBHdJ%2bNwzM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/san-ignacio_procesos-electorales_HHsw7tdcROky72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/jaen_procesos-electorales_dulD%2baPyiA%3d%3d72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/cutervo_procesos-electorales_hBzr7%40QSU7Ew72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/chota_procesos-electorales_OvT5wBzuxQ%3d%3d72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/santa-cruz_procesos-electorales_7Pa%2bxVp7Oyke72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/san-miguel_procesos-electorales_ku5Hs7awdEtu72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/san-pablo_procesos-electorales_NxR5UFbrLk1972",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/contumaza_procesos-electorales_TKs1KFdwcBsi72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/hualgayoc_procesos-electorales_0%40MBKybAVreo72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/celendin_procesos-electorales_1XdlESwUK4Z272",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/cajamarca_procesos-electorales_%40bVRS3Nn4YHA72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/san-marcos_procesos-electorales_Kq%40gwT7xVfzD72",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca/cajabamba_procesos-electorales_4%40O%2bMV7%403Dj%2b72",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/condorcanqui_procesos-electorales_gyltg8T1ESOMzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/bagua_procesos-electorales_DwBwtyzfTw%3d%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/utcubamba_procesos-electorales_SN1IcPkp2%2bE2zf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/bongara_procesos-electorales_77zXluNc3Q%3d%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/luya_procesos-electorales_%40OE7ri%2bpQg%3d%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/chachapoyas_procesos-electorales_sbG6KfMPK2Hszf",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas/rodriguez-de-mendoza_procesos-electorales_ELA7zcLR7m4%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/datem-del-mara%C3%B1on_procesos-electorales_HOvv9BJTsTA%3dYu",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/alto-amazonas_procesos-electorales_GlkvYftrCMCqvv",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/loreto_procesos-electorales_Hc3vsrwBlQ%3d%3dCo",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/requena_procesos-electorales_HuMCX56qBw%3d%3dWz",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/ucayali_procesos-electorales_iOfjA3t6eg%3d%3drS",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/maynas_procesos-electorales_URpIgsVUPA%3d%3dG9",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/putumayo_procesos-electorales_3pA11yslxA%3d%3dCg",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto/mariscal-ramon-castilla_procesos-electorales_PMrxd3vT7%40k%3dG9",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/rioja_procesos-electorales_UJI5rs3vHA%3d%3dpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/moyobamba_procesos-electorales_p5AAYS1CzpSTpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/lamas_procesos-electorales_nD3Wy%2b0oiQ%3d%3dpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/el-dorado_procesos-electorales_5F9VgQZFmwFXpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/huallaga_procesos-electorales_P9NkQlh3Jplwpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/mariscal-caceres_procesos-electorales_YH46PrEm%2bys%3dpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/tocache_procesos-electorales_IJhbMqi1l5qRpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/bellavista_procesos-electorales_mE1KlxWof9Qbpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/picota_procesos-electorales_Axzr7%40QSU7Ewpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin/san-martin_procesos-electorales_Jce5Jee9onpypd",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/chepen_procesos-electorales_Z3dlESwUK4Z27X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/pacasmayo_procesos-electorales_7qyX0cMrsw3m7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/ascope_procesos-electorales_wphbMqi1l5qR7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/trujillo_procesos-electorales_HcnnOmP03I8c7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/viru_procesos-electorales_1rezSB2STg%3d%3d7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/julcan_procesos-electorales_CHdlESwUK4Z27X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/santiago-de-chuco_procesos-electorales_rkFsrrQ8sIo%3d7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/sanchez-carrion_procesos-electorales_5B4PP4uZJ8Q%3d7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/pataz_procesos-electorales_TRzr7%40QSU7Ew7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/bolivar_procesos-electorales_6jSe6isMdk8b7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/otuzco_procesos-electorales_1ZLDKvOcPD1i7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad/gran-chimu_procesos-electorales_75a%407dl3f%2bZL7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/pallasca_procesos-electorales_BxwXrfjZvw%3d%3dlb",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/sihuas_procesos-electorales_mFNA5UlgYg%3d%3d1H",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/corongo_procesos-electorales_UUgAqvcbcw%3d%3dNP",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/santa_procesos-electorales_UsLjH1O58A%3d%3dsV",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/huaylas_procesos-electorales_c8TTujiLQg%3d%3dWD",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/pomabamba_procesos-electorales_pTCNjBrAUA%3d%3dc6",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/mariscal-luzuriaga_procesos-electorales_HOvv9BJTsTA%3dRQ",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/yungay_procesos-electorales_GDOEhI7YWw%3d%3dDY",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/casma_procesos-electorales_kNVcpckmIQ%3d%3doM",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/carhuaz_procesos-electorales_Q%2bV8FswFmw%3d%3doM",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/asuncion_procesos-electorales_%40b13V0%40M6w%3d%3dLf",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/carlos-fermin-fitzcarrald_procesos-electorales_YLSnVEzmYEw%3doM",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/huaraz_procesos-electorales_wiZZ0LKPdA%3d%3dWD",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/huari_procesos-electorales_aA1tqO5U8w%3d%3dWD",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/aija_procesos-electorales_5rBrCGa6nA%3d%3ddG",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/huarmey_procesos-electorales_zU9t%2biEuJw%3d%3dWD",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/recuay_procesos-electorales_M1%40gRDmCcw%3d%3d1P",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/bolognesi_procesos-electorales_SkHHUUSS5w%3d%3d9K",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/ocros_procesos-electorales_Umv5XuhODA%3d%3dSc",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash/antonio-raimondi_procesos-electorales_F8mRLy2ZaflMqG",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/mara%C3%B1on_procesos-electorales_KBuyTCNhKQ%3d%3d2j",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/huacaybamba_procesos-electorales_kfO%2bMV7%403Dj%2bCf",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/huamalies_procesos-electorales_Gxzr7%40QSU7EwCf",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/dos-de-mayo_procesos-electorales_LTbcBHdJ%2bNwzfQ",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/yarowilca_procesos-electorales_GBzr7%40QSU7EwIE",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/lauricocha_procesos-electorales_ud1IcPkp2%2bE2bF",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/huanuco_procesos-electorales_7qBHbdoReg%3d%3dCf",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/ambo_procesos-electorales_lNPgSU75ig%3d%3dIv",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/pachitea_procesos-electorales_bV2hIoGC3w%3d%3deC",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/puerto-inca_procesos-electorales_ubVRS3Nn4YHAeC",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco/leoncio-prado_procesos-electorales_G1hFXhAzC4G2bF",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali/padre-abad_procesos-electorales_qn6SwPpoDJJkUT",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali/coronel-portillo_procesos-electorales_1c%40wr9E%2bcv3FZr",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali/atalaya_procesos-electorales_YRrHJaNMKA%3d%3d1B",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali/purus_procesos-electorales_WSW1equa3w%3d%3dUT",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/barranca_procesos-electorales_ruGIQt1a4A%3d%3dN5",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/huaura_procesos-electorales_5rFopKl4KA%3d%3d9Q",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/cajatambo_procesos-electorales_BeLmcQJz4Q%3d%3dsE",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/oyon_procesos-electorales_6%2b%400ElOxMA%3d%3d8U",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/huaral_procesos-electorales_0w0Wfz8pIA%3d%3dno",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/canta_procesos-electorales_SHD5KdvhNg%3d%3dBy",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/lima_procesos-electorales_6%2b%400ElOxMA%3d%3dR3",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/huarochiri_procesos-electorales_HG%40iEkCMng%3d%3dno",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/ca%C3%B1ete_procesos-electorales_rvQvtviDOQ%3d%3d%40U",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima/yauyos_procesos-electorales_FvUxadQiyw%3d%3dG%2b",
    "https://infogob.jne.gob.pe/Localidad/Peru/pasco/daniel-alcides-carrion_procesos-electorales_ppyEbavnZkk%3d4t",
    "https://infogob.jne.gob.pe/Localidad/Peru/pasco/pasco_procesos-electorales_IS7x5ErLeg%3d%3d8Q",
    "https://infogob.jne.gob.pe/Localidad/Peru/pasco/oxapampa_procesos-electorales_9N%2b0O9ZdRQ%3d%3doq",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/yauli_procesos-electorales_4VqeD%40%2bpMA%3d%3dfC",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/junin_procesos-electorales_Gidr2ZmWBg%3d%3dku",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/tarma_procesos-electorales_LUz3dbd3hQ%3d%3dDN",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/jauja_procesos-electorales_5rBrCGa6nA%3d%3dM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/concepcion_procesos-electorales_2STPlFDlTg%3d%3dr8",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/chupaca_procesos-electorales_L%2bZ9bNwt3A%3d%3dCc",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/huancayo_procesos-electorales_pFyPG77JPw%3d%3d5n",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/satipo_procesos-electorales_JhPI3y84Tw%3d%3dMQ",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin/chanchamayo_procesos-electorales_iRzr7%40QSU7EwgV",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica/chincha_procesos-electorales_ewSUlIsnDQ%3d%3dcm",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica/pisco_procesos-electorales_6%2b%400ElOxMA%3d%3d8D",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica/ica_procesos-electorales_UzYK4Rbg0ek%3dYR",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica/palpa_procesos-electorales_6%2b%400ElOxMA%3d%3diJ",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica/nasca_procesos-electorales_6%2b%400ElOxMA%3d%3dFu",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/tayacaja_procesos-electorales_QntPIG96fo3tei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/churcampa_procesos-electorales_MUlIuGnyAkLxei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/huancavelica_procesos-electorales_HOvv9BJTsTA%3dei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/acobamba_procesos-electorales_YcHtTWj7KdYAei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/angaraes_procesos-electorales_X74FtEgUJ%409qei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/castrovirreyna_procesos-electorales_eEe%40qOFE8mo%3dei",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica/huaytara_procesos-electorales_ftMAUpKaCp2xei",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/huanta_procesos-electorales_JlL6tniTug%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/la-mar_procesos-electorales_WW4lsoJHvg%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/huamanga_procesos-electorales_8Rzr7%40QSU7EwUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/cangallo_procesos-electorales_Zxzr7%40QSU7EwUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/vilcas-huaman_procesos-electorales_BRww0gBPlnx7UL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/victor-fajardo_procesos-electorales_0KxElyEd7PhrUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/huanca-sancos_procesos-electorales_wG23v1eo5yaHUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/sucre_procesos-electorales_D0AhTDjQKQ%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/lucanas_procesos-electorales_t2dmNztejQ%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/parinacochas_procesos-electorales_e5aVWTdylUd8UL",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho/paucar-del-sara-sara_procesos-electorales_lseMLwAjvuM%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/chincheros_procesos-electorales_5LsW9TFp1CLLqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/andahuaylas_procesos-electorales_%40j0ldih8XmQZqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/aymaraes_procesos-electorales_CBzr7%40QSU7Ewqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/abancay_procesos-electorales_NH6xEKcBiQ%3d%3dqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/grau_procesos-electorales_YxkFXsEulw%3d%3dqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/antabamba_procesos-electorales_%40d1IcPkp2%2bE2qf",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac/cotabambas_procesos-electorales_%2b6iovpVoaz2Fqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/la-convencion_procesos-electorales_jeQeDz%2bLmSfEn9",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/calca_procesos-electorales_UUtzZ%2bGBwA%3d%3d4b",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/urubamba_procesos-electorales_fB0cFuxsfA%3d%3dIM",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/anta_procesos-electorales_SHD5KdvhNg%3d%3drO",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/cusco_procesos-electorales_IS7x5ErLeg%3d%3dcE",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/paruro_procesos-electorales_HPxNrNphhA%3d%3dRd",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/chumbivilcas_procesos-electorales_i%40cD50B7veCAKe",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/espinar_procesos-electorales_6htEM5sjtw%3d%3dOe",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/canas_procesos-electorales_qL6VaGs9hQ%3d%3d6w",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/canchis_procesos-electorales_edtwKdLHHQ%3d%3d6w",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/quispicanchi_procesos-electorales_dE5w4sP3l5lKSa",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/paucartambo_procesos-electorales_Cxzr7%40QSU7Ew2c",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco/acomayo_procesos-electorales_l9HDK7MN5g%3d%3dj1",
    "https://infogob.jne.gob.pe/Localidad/Peru/madre-de-dios/tahuamanu_procesos-electorales_6diiEqSrIv0nA2",
    "https://infogob.jne.gob.pe/Localidad/Peru/madre-de-dios/tambopata_procesos-electorales_uqvNTq6d0rLTA2",
    "https://infogob.jne.gob.pe/Localidad/Peru/madre-de-dios/manu_procesos-electorales_6Z%40n2nJOJBMsA2",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/caraveli_procesos-electorales_Xxzr7%40QSU7EwHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/la-union_procesos-electorales_bBzr7%40QSU7EwHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/condesuyos_procesos-electorales_dbsW9TFp1CLLHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/camana_procesos-electorales_K8iTdC9FbQ%3d%3dHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/islay_procesos-electorales_Uq9%40HV4%2b7Q%3d%3dHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/arequipa_procesos-electorales_Ehzr7%40QSU7EwHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/caylloma_procesos-electorales_ORzr7%40QSU7EwHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa/castilla_procesos-electorales_thzr7%40QSU7EwHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/carabaya_procesos-electorales_2NQAHqomhw%3d%3d%40G",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/sandia_procesos-electorales_jygswWIqIQ%3d%3diO",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/melgar_procesos-electorales_nuorDHZPGw%3d%3dGG",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/azangaro_procesos-electorales_eXDpJRRqEw%3d%3dVR",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/san-antonio-de-putina_procesos-electorales_3Uhw%2bSnb4TY%3d8C",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/huancane_procesos-electorales_4uljr%40GgWA%3d%3d9W",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/moho_procesos-electorales_6%2b%400ElOxMA%3d%3dKt",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/lampa_procesos-electorales_SHD5KdvhNg%3d%3dND",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/san-roman_procesos-electorales_wfL4pJ46Iw%3d%3d8C",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/puno_procesos-electorales_6%2b%400ElOxMA%3d%3dJH",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/el-collao_procesos-electorales_8Lz0V0Wn7Q%3d%3dTk",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/chucuito_procesos-electorales_6NP9pxlyIw%3d%3d8r",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno/el-collao_procesos-electorales_8Lz0V0Wn7Q%3d%3dTk",
    "https://infogob.jne.gob.pe/Localidad/Peru/moquegua/general-sanchez-cerro_procesos-electorales_EO6PlJuwAdU%3d1%40",
    "https://infogob.jne.gob.pe/Localidad/Peru/moquegua/mariscal-nieto_procesos-electorales_WLz0QkOf9YqG1%40",
    "https://infogob.jne.gob.pe/Localidad/Peru/moquegua/ilo_procesos-electorales_8ntsij66yQ%3d%3d1%40",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna/candarave_procesos-electorales_%40QWAfLUo3g%3d%3dLb",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna/jorge-basadre_procesos-electorales_ReJzxziAJjfcxr",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna/tacna_procesos-electorales_R7%2bo4UTyag%3d%3dui",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna/tarata_procesos-electorales_TW02xdQbhA%3d%3dvn",
    "https://infogob.jne.gob.pe/Localidad/Peru/callao/callao_procesos-electorales_4pmWlC3vqg%3d%3d%40w"

]


    j=1
    def extraction (urls, type):
        global j
        for url in urls:
            result = requests.get(url)
            src = result.content
            soup = BeautifulSoup(src, 'lxml')

            links = soup.find_all("input")
            for link in links:
                if (link.attrs['id']=='TxRegion'):
                    region=str(link.attrs['value'])
                elif (link.attrs['id']=='TxProvincia'):
                    province=str(link.attrs['value'])


            tag = soup.find_all('tr')[2]
            tag2 = tag.find_all('td') [0] #puesto
            tag3 = tag.find_all('td') [1] #nombre
            if (type == 'TxRegion'):
                postgres_insert_query = """ INSERT INTO gobiernoapp_region (id, reg_name, authority) VALUES (%s,%s,%s)"""
                record_to_insert = (j, region, str(tag3.text))
            else:
                postgres_insert_query = """ INSERT INTO gobiernoapp_province (id, prov_name, authority, region) VALUES (%s,%s,%s,%s)"""
                record_to_insert = (j, province, str(tag3.text), region)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into table")



            postgres_insert_query = """ INSERT INTO gobiernoapp_politician (poli_name, job, location_id, photo_url) VALUES (%s,%s,%s,%s)"""
            fulllist = soup.find_all('tr')
            i=2
            while (i<(len(fulllist))):
                tag = soup.find_all('tr')[i]
                tag2 = tag.find_all('td') [0] #puesto
                tag3 = tag.find_all('td') [1] #nombre
                tag4 = tag.find_all('td') [2] #url de la foto
                record_to_insert = (str(tag3.text), str(tag2.text), j, "https://infogob.jne.gob.pe" + str(tag4.text))
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count = cursor.rowcount
                print (count, "Record inserted successfully into table")
                i+=1

            j+=1
            time.sleep(1)


    extraction(urlsregions, "TxRegion")
    extraction(urlsprovinces, "TxProvincia")



except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
