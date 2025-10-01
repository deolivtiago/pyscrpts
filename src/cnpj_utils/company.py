from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class QSA:
    nome_socio: str
    cnpj_cpf_socio: str
    qualificacao_socio: str
    data_entrada_sociedade: str
    identificador_socio: str
    faixa_etaria: str

    @staticmethod
    def from_dict(obj: Any) -> 'QSA':
        _nome_socio = str(obj.get("nome_socio"))
        _cnpj_cpf_socio = str(obj.get("cnpj_cpf_socio"))
        _qualificacao_socio = str(obj.get("qualificacao_socio"))
        _data_entrada_sociedade = str(obj.get("data_entrada_sociedade"))
        _identificador_socio = str(obj.get("identificador_socio"))
        _faixa_etaria = str(obj.get("faixa_etaria"))
        return QSA(_nome_socio, _cnpj_cpf_socio, _qualificacao_socio, _data_entrada_sociedade, _identificador_socio, _faixa_etaria)

@dataclass
class Empresa:
    cnpj: str
    razao_social: str
    nome_fantasia: str
    situacao_cadastral: str
    data_situacao_cadastral: str
    matriz_filial: str
    data_inicio_atividade: str
    cnae_principal: str
    cnaes_secundarios: List[str]
    natureza_juridica: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cep: str
    uf: str
    municipio: str
    email: str
    telefones: List['Telefone']
    capital_social: str
    porte_empresa: str
    opcao_simples: str
    data_opcao_simples: str
    opcao_mei: str
    data_opcao_mei: str
    QSA: List[QSA]

    @staticmethod
    def from_dict(obj: Any) -> 'Empresa':
        _cnpj = str(obj.get("cnpj"))
        _razao_social = str(obj.get("razao_social"))
        _nome_fantasia = str(obj.get("nome_fantasia"))
        _situacao_cadastral = str(obj.get("situacao_cadastral"))
        _data_situacao_cadastral = str(obj.get("data_situacao_cadastral"))
        _matriz_filial = str(obj.get("matriz_filial"))
        _data_inicio_atividade = str(obj.get("data_inicio_atividade"))
        _cnae_principal = str(obj.get("cnae_principal"))
        _cnaes_secundarios = [y for y in obj.get("cnaes_secundarios")]
        _natureza_juridica = str(obj.get("natureza_juridica"))
        _logradouro = str(obj.get("logradouro"))
        _numero = str(obj.get("numero"))
        _complemento = str(obj.get("complemento"))
        _bairro = str(obj.get("bairro"))
        _cep = str(obj.get("cep"))
        _uf = str(obj.get("uf"))
        _municipio = str(obj.get("municipio"))
        _email = str(obj.get("email"))
        _telefones = [Telefone.from_dict(y) for y in obj.get("telefones")]
        _capital_social = str(obj.get("capital_social"))
        _porte_empresa = str(obj.get("porte_empresa"))
        _opcao_simples = str(obj.get("opcao_simples"))
        _data_opcao_simples = str(obj.get("data_opcao_simples"))
        _opcao_mei = str(obj.get("opcao_mei"))
        _data_opcao_mei = str(obj.get("data_opcao_mei"))
        _QSA = [QSA.from_dict(y) for y in obj.get("QSA")]
        return Empresa(_cnpj, _razao_social, _nome_fantasia, _situacao_cadastral, _data_situacao_cadastral, _matriz_filial, _data_inicio_atividade, _cnae_principal, _cnaes_secundarios, _natureza_juridica, _logradouro, _numero, _complemento, _bairro, _cep, _uf, _municipio, _email, _telefones, _capital_social, _porte_empresa, _opcao_simples, _data_opcao_simples, _opcao_mei, _data_opcao_mei, _QSA)

@dataclass
class Telefone:
    ddd: str
    numero: str
    is_fax: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Telefone':
        _ddd = str(obj.get("ddd"))
        _numero = str(obj.get("numero"))
        _is_fax = bool(obj.get("is_fax"))
        return Telefone(_ddd, _numero, _is_fax)

if __name__ == "__main__":
    json_file = "output.json"

    with open(json_file, "r", encoding="utf-8") as f:
        json_content = f.read()

    companies = [Empresa.from_dict(company) for company in json.loads(json_content)]

    data_list = [f'"{company.cnpj}";"{company.razao_social}";"{company.data_inicio_atividade}";{company.capital_social}' for company in companies]

    with open("output.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(data_list))
