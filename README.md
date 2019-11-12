# Atividade de Busca de Similaridade de imagem
## Busca de similaridade de uma imagem dentro de um "Diretório de busca"

## Introdução
Atividade de "Computação gráfica e Jogos Digitais". O objetivo é utilizar um modelo de reconhecimento de imagem para:
1. Obter uma imagem e usa-la como template
2. Buscar dentro de todos os arquivos .jpg e .mp4 similaridades com o template
3. Exibir ao final uma lista ordenada imagens e frames de vídeos encontrados, em ordem de similaridade

## Instalação
```
pip install -u requirements.txt
```
## Como iniciar o projeto:
Como padrão ele inicialmente procura um arquivo chamado "serie_face_4.jpg", o parâmetro de similaridade é de 0.71% e o diretório de busca é "Diretorio de Busca".
Se for desejo, é só alterar as variáveis match_value(parâmetro de similaridade), template_name(Nome de arquivo de parametro para busca), directory(Nome do diretório de busca) e *se necessário(for desejo)* print_similar para usar o plt do matplotlib para printar a imagem 
```
python searcher.py
```
