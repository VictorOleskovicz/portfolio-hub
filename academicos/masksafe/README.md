# MaskSafe — Mascaramento de Dados Sensíveis

> Projeto Integrador III — Ciência da Computação, UniCEUB

**Repositório do código:** https://github.com/VictorOleskovicz/masksafe
**Equipe:** Victor Oleskovicz e Pedro

## Problema

Bases de desenvolvimento, teste e análise costumam receber cópias de dados de produção com informações pessoais (CPF, e-mail, telefone, nome). Isso expõe a organização a vazamentos e a não conformidades com a LGPD.

## Solução

O MaskSafe aplica regras de mascaramento a dados sensíveis. O formato do dado continua útil para testes, e a pessoa real deixa de ser identificável.

Exemplos de regras:

| Dado | Original | Mascarado |
|---|---|---|
| CPF | 123.456.789-09 | \*\*\*.456.\*\*\*-\*\* |
| E-mail | joao.silva@email.com | j\*\*\*\*@email.com |
| Telefone | (61) 99876-5432 | (61) \*\*\*\*\*-5432 |

## Minha contribuição

- Modelagem e implementação do **banco de dados**
- Desenvolvimento do **backend** (regras de mascaramento e persistência)

## Status

Em desenvolvimento. Esta versão é a evolução do projeto SafeMask, feito em grupo no semestre anterior ([Safe-Mask/SafeMask](https://github.com/Safe-Mask/SafeMask)).

## Aprendizados

- Classificação de dados pessoais e sensíveis segundo a LGPD
- Técnicas de anonimização e pseudonimização
- Organização de um repositório institucional (documentação) separado do repositório de código
